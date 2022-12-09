<template>
  <v-container>
    <v-tabs v-model="tab" fixed-tabs align-tabs="true" color="blue">
      <v-tab value="all">All</v-tab>
      <v-tab value="perStep">Per Step</v-tab>
    </v-tabs>
    <h1>Indicators</h1>
    <p>
      List of the indicators that are commonly used to evaluate program based on
      the triple/quadruple helix program.
    </p>
    <v-window v-model="tab">
      <v-window-item value="all"
        ><v-table>
          <thead>
            <tr>
              <th class="text-left">ID</th>
              <th class="text-left">Description</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in indicators" :key="item.name">
              <td>{{ item.name }}</td>
              <td>{{ item.description }}</td>
            </tr>
          </tbody>
        </v-table>
      </v-window-item>
      <v-window-item value="perStep">
        <v-row >
          <v-col xs="12" sm="6" md="4" lg="2" cols="12">
            <h3>Input</h3>
            <v-list>
              <v-list-item
                v-for="ind in input"
                :key="ind.name"
                :title="ind.name"
                :subtitle="ind.description"
                :value="ind.name"
                :to="{name : 'Indicator-Detail', params: {indid: ind.name }}"
              ></v-list-item>
            </v-list>
          </v-col>
          <v-col xs="12" sm="6" md="4" lg="2" cols="12">
            <h3>Activity</h3>
            <v-list>
              <v-list-item
                v-for="ind in activity"
                :key="ind.name"
                :title="ind.name"
                :subtitle="ind.description"
                :value="ind.name"
              ></v-list-item>
            </v-list>
          </v-col>
          <v-col xs="12" sm="6" md="4" lg="2" cols="12">
            <h3>Output</h3>
            <v-list>
              <v-list-item
                v-for="ind in output"
                :key="ind.name"
                :title="ind.name"
                :subtitle="ind.description"
                :value="ind.name"
              ></v-list-item>
            </v-list>
          </v-col>
          <v-col xs="12" sm="6" md="4" lg="2" cols="12">
            <h3>Outcome</h3>
            <v-list>
              <v-list-item
                v-for="ind in outcome"
                :key="ind.name"
                :title="ind.name"
                :subtitle="ind.description"
                :value="ind.name"
              ></v-list-item>
            </v-list>
          </v-col>
          <v-col xs="12" sm="6" md="4" lg="2" cols="12">
            <h3>Final Outcome</h3>
            <v-list>
              <v-list-item
                v-for="ind in finalOutcome"
                :key="ind.name"
                :title="ind.name"
                :subtitle="ind.description"
                :value="ind.name"
              ></v-list-item>
            </v-list>
          </v-col>
        </v-row>
      </v-window-item>
    </v-window>
  </v-container>
</template>
  
  
  <script>
export default {
  data() {
    return {
      tab: null,
      indicators: [
        {
          name: "IND 1",
          step: "input",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        },
        {
          name: "IND 2",
          step: "input",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        },
        {
          name: "IND 3",
          step: "activity",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        },
        {
          name: "IND 4",
          step: "outcome",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        },
        {
          name: "IND 5",
          step: "final outcome",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        },
        {
          name: "IND 6",
          step: "output",
          description:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        },
      ],
    };
  },
  computed: {
    input: function () {
      return this.indicators.filter(function (u) {
        return u.step == "input";
      });
    },
    activity: function () {
      return this.indicators.filter(function (u) {
        return u.step == "activity";
      });
    },
    output: function () {
      return this.indicators.filter(function (u) {
        return u.step == "output";
      });
    },
    outcome: function () {
      return this.indicators.filter(function (u) {
        return u.step == "outcome";
      });
    },
    finalOutcome: function () {
      return this.indicators.filter(function (u) {
        return u.step == "final outcome";
      });
    },
  },
};
</script>