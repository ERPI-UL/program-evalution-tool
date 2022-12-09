<template>
  <v-container>
    <h1>Dashboard list</h1>
    <v-expansion-panels class="mb-6" multiple>
      <v-expansion-panel
        v-for="(item, i) in evaluations"
        :key="i"
        :title="item.name"
      >
      <v-expansion-panel-text>
        <v-list dense>
          <v-list-item v-for="(wp, i) in item.workpackage" :key="i" :value="i" :title="wp.name" :to="{name:'Project-Dashboard', params:{ projid: item.id} }" @click="updateTab(wp.id)">
          </v-list-item>
        </v-list>
      </v-expansion-panel-text>
        
      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>
</template>

<script>
import programs from "@/data/projects.json";
import { useAppStore } from "@/stores/AppStore";

export default {
  data() {
    return {
      evaluations: programs
    };
  },
  setup() {
    const appStore = useAppStore();
    return { appStore };
  },
  methods: {
    updateTab(wpid) {
      this.appStore.defineSelectedWp(wpid);
    },
  },
};
</script>