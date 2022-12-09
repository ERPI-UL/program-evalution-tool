<template>
  <v-container>
    <!-- <v-tabs v-model="tab" fixed-tabs color="blue">
      <v-tab v-for="wp in project.workpackage" :value="wp.name">{{
        wp.name
      }}</v-tab>
    </v-tabs> -->
    <v-row justify="space-between">
      <v-col cols="12" md="5">
        <v-range-slider
          v-model="year_range"
          :max="year_max"
          :min="year_min"
          step="1"
          strict
          thumb-label="always"
          label="Années selectionnées"
        ></v-range-slider>
      </v-col>
      <v-col cols="12" md="5">
        <v-select
          v-model="selectedIndicator"
          :items="indicators"
          item-title="label"
          item-value="var_name"
          :rules="[(v) => !!v || 'Item is required']"
          label="Indicateur"
        ></v-select>
      </v-col>
    </v-row>
    <div v-if="selected_project == null">Please selecte a project.</div>

    <v-window v-model="dashboard_tab" v-if="selected_project != null">
      <v-window-item :value="wp.name" v-for="wp in projects.find(project => project.id == selected_project).workpackage">
        <v-container>
          <v-row align-content="center">
            <v-col cols="12" lg="6">
              <apexchart
            type="bar"
            :options="options"
            :series="filtered_series"
          ></apexchart>
          </v-col>
        </v-row>
          
          
        </v-container>
      </v-window-item>
    </v-window>
  </v-container>
</template>
<script>
import VueApexCharts from "vue3-apexcharts";
import { useAppStore} from "@/stores/AppStore";
import { useProjectStore} from "@/stores/ProjectStore";
import { mapState, mapWritableState} from "pinia";

import stats from "@/data/4sh.json";
export default {
  props: ["dashid"],
  setup(){
    const projectStore = useProjectStore();
    return {projectStore}
  },
  data() {
    return {
      selectedIndicator: "all",
      year_min: 2022,
      year_max: 2029,
      year_range: [2022, 2029],
      indicators: [
        { label: "Tous", var_name: "all" },
        { label: "Nb innovations testé", var_name: "nbTestedInnovation" },
        { label: "Nb de visites d'espace", var_name: "nbFederatedIS" },
        { label: "Nb visite", var_name: "nbVisits" },
      ],
      data: stats,
    };
  },
  computed: {
    //...mapState(useAppStore, ["selected_project"]),
    ...mapState(useProjectStore, ["projects"]),
    ...mapWritableState(useAppStore, ["selected_project","dashboard_tab"]),
    stats_year_filtered: function () {
      return this.data.filter(function (u) {
        return u.year > this.year_range[0] && u.year < this.year_range[1];
      });
    },
    categories: function () {
      var year_cat = [];
      for (var i = this.year_range[0]; i <= this.year_range[1]; i++) {
        year_cat.push(i);
      }
      return year_cat;
    },
    options: function () {
      return {
        chart: { id: "yearly indicator" },
        xaxis: { categories: this.categories },
      };
    },
    series_conversion: function () {
      var temp_series = [];
      var year_min = this.year_range[0];
      var year_max = this.year_range[1];
      this.indicators.forEach(function (indicator) {
        var temp_serie = [];
        // for(var i = year_min; i <= year_max; i++ ){
        if (indicator.var_name != "all") {
          for (var i = year_min; i <= year_max; i++) {
            var aggr = 0;
            stats.forEach(function (item) {
              if (item.year == i) {
                aggr = aggr + item[indicator.var_name];
              }
            });
            temp_serie.push(aggr);
          }
          temp_series.push({
            name: indicator.label,
            data: temp_serie,
            id: indicator.var_name,
          });
        }
      });
      return temp_series;
    },
    filtered_series: function () {
      var selected_ind = this.selectedIndicator;
      if (selected_ind != "all") {
        console.log(selected_ind);
        var series = this.series_conversion
        return series.filter(function (serie) {
          return serie.id == selected_ind;
        });
      } else {
        return this.series_conversion;
      }
    },
  },
};
</script>

<style scoped>
#chart {
  max-width: 760px;
  margin: 35px auto;
  opacity: 0.9;
}
</style>