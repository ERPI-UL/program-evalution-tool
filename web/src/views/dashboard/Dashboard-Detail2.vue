<template>
  <v-container>
    <!-- <v-tabs v-model="tab" fixed-tabs color="blue">
      <v-tab v-for="wp in project.workpackage" :value="wp.name">{{
        wp.name
      }}</v-tab>
    </v-tabs> -->
    <div v-if="selected_project == null"><v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <p>Il faut selectionner une programme.</p>
        </v-col>
      </v-row></div>
    <div v-else>
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
    

    <v-window v-model="dashboard_tab" v-if="selected_project != null">
      <v-window-item
        :value="wp.id"
        v-for="wp in projects.find((project) => project.id == selected_project)
          .workpackage"
      >
        <v-container>
          <v-row class="d-flex align-center justify-center">
            <v-col cols="12" lg="6">
              <apexchart
                type="bar"
                :options="options"
                :series="filtered_series"
              ></apexchart>
            </v-col>
          </v-row>
          <v-row class="d-flex align-center justify-center">
            <v-col cols="12" lg="6">
              <apexchart
                type="bar"
                :options="options2"
                :series="objectives_filtered_series"
              ></apexchart>
            </v-col>
          </v-row>
        </v-container>
      </v-window-item>
    </v-window>
  </div>
  </v-container>
</template>
<script>
import VueApexCharts from "vue3-apexcharts";
import { useAppStore } from "@/stores/AppStore";
import { useProjectStore } from "@/stores/ProjectStore";
import { mapState, mapWritableState } from "pinia";

import stats from "@/data/4sh.json";
import ratio from "@/data/4sh_ratio.json";
export default {
  props: {projid : String},
  setup() {
    const appStore = useAppStore();
    const projectStore = useProjectStore();
    return { projectStore, appStore };
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
    };
  },
  mounted() {
    if(this.projid){
      this.appStore.defineSelectedProject(this.projid);
    }
    // utiliser une action sur Appstore pour modifier
  },
  computed: {
    ...mapState(useAppStore, ["selected_project"]),
    ...mapState(useProjectStore, ["projects"]),
    ...mapWritableState(useAppStore, ["dashboard_tab"]),
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
        chart: { id: "yearly indicator" , height:'800px'},
        xaxis: { categories: this.categories },
        title: {
          text: "Nb occurences annuelles par indicateur",
          align: "center",
        },
        tooltip: {
          shared: true,
          intersect: false,
        },
      };
    },
    options2: function () {
      return {
        chart: { id: "yearly objectifs", height:'800px'},
        xaxis: { categories: this.categories },
        title: {
          text: "Pourcentage de l'objectif atteint par année",
          align: "center",
        },
        tooltip: {
          shared: true,
          intersect: false,
        },
        fill: {
          colors: [function({ value, seriesIndex, w }) {
            if(value < 0.80) {
                return '#d23c1e'
            } else if (value >= 0.8 && value < 1) {
                return '#c8cb06'
            } else {
                return '#75cb06'
            }
          }]
        }
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
        var series = this.series_conversion;
        return series.filter(function (serie) {
          return serie.id == selected_ind;
        });
      } else {
        return this.series_conversion;
      }
    },
    objectives_series_conversion: function () {
      var temp_series = [];
      var year_min = this.year_range[0];
      var year_max = this.year_range[1];
      this.indicators.forEach(function (indicator) {
        var temp_serie = [];
        // for(var i = year_min; i <= year_max; i++ ){
        if (indicator.var_name != "all") {
          for (var i = year_min; i <= year_max; i++) {
            objectifs.forEach(function (item) {
              if (item.year == i) {
                temp_serie.push(item[indicator.var_name]);
              }
            });
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
    objectives_filtered_series: function(){
      var selected_ind = this.selectedIndicator;
      if (selected_ind != "all") {
        return ratio.filter(function (serie) {
          return serie.id == selected_ind;
        });
      } else {
        return ratio;
      }
    }
    // objectives_filtered_series: function () {
    //   var selected_ind = this.selectedIndicator;
    //   var ratio = [];
    //   this.indicators.forEach((indicator) =>{
    //     value = this.series_conversion.find((serie) => serie.id == indicator.var_name).data;
    //     obj = this.objectives_series_conversion.find((serie) => serie.id == indicator.var_name).data;
    //     temp_serie = [];
    //     if (value.lenght == obj.lenght) {
    //       for (x = 0; x < value.lenght; x++) {
    //         if (obj[x] <= 0 || obj[x] == null) {
    //           temp_serie.push(0);
    //         } else {
    //           temp_serie.push(value[0] / obj[x]);
    //         }
    //       }
    //     }
    //     ratio.push({
    //       name: indicator.label,
    //       data: temp_serie,
    //       id: indicator.var_name,
    //     });
    //   });
    //   if (selected_ind != "all") {
    //     //console.log(selected_ind);
    //     return ratio.filter(function (serie) {
    //       return serie.id == selected_ind;
    //     });
    //   } else {
    //     return ratio;
    //   }
    // },
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