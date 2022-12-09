<template>
  <v-container>
    <h1>Project evaluation</h1>
    <v-expansion-panels class="mb-6" multiple>
      <v-expansion-panel
        v-for="(item, i) in evaluations"
        :key="i"
        :title="item.name"
      >
        <v-expansion-panel-text>
          <v-list dense>
            <v-list-item
              v-for="(wp, j) in item.workpackage"
              :title="wp.name"
              :key="j"
              :value="j"
              :to="{ name: 'Project-Evalution-Form', params: { projid: item.id } }"
            >
              <template v-slot:append>
                <v-icon v-if="wp.done" color="green"
                  >mdi-check-circle-outline</v-icon>
                <v-icon v-else color="red">mdi-alert-circle-outline</v-icon>
              </template>
            </v-list-item>
          </v-list>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>
</template>

<script>
import evals from "@/data/projects.json";

export default {
  data() {
    return {
      evaluations: evals
    };
  },
};
</script>