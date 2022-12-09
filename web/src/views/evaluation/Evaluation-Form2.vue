<template>
  <v-container>
    <v-row>
      <v-col>
        <h2>Formulaire d'évaluation</h2>
      </v-col>
    </v-row>

    <v-window v-model="dashboard_tab" v-if="selected_project != null">
      <v-window-item
        :value="wp.id"
        v-for="wp in questions.find((project) => project.id == selected_project).workpackage"
      >
        <v-form ref="form" v-model="valid" lazy-validation>
          <div v-for="quest in wp.questions">
            <p>{{ quest.label }}</p>
            <v-text-field
              v-if="quest.type == 'text-number'"
              
              type="number"
            ></v-text-field>
            <v-text-field
              v-if="quest.type == 'text'"
              type="text"
            ></v-text-field>
            <v-textarea
              auto-grow
              v-if="quest.type == 'textarea'"
            ></v-textarea>
          </div>
          <v-btn color="success" class="mr-4" @click="validate">
            Enregister
          </v-btn>
        </v-form>
      </v-window-item>
    </v-window>
  </v-container>
</template>
  <script>
import questions from "@/data/questions.json";
import { useAppStore } from "@/stores/AppStore";
import { useProjectStore } from "@/stores/ProjectStore";
import { mapState, mapWritableState } from "pinia";

export default {
  props: {
    projid: { type: String, default: null },
    // wpid: { type: String, default: null },
  },
  setup() {
    const appStore = useAppStore();
    const projectStore = useProjectStore();
    return { projectStore, appStore };
  },
  data: () => ({
    valid: false,
    questions: questions,
  }),
  mounted() {
    if (this.projid) {
      this.appStore.defineSelectedProject(this.projid);
    }
    // if (this.wpid) {
    //   this.appStore.defineSelectedWp(this.wpid);
    // }
    // utiliser une action sur Appstore pour modifier
  },
  computed:{
    ...mapState(useProjectStore, ["projects"]),
    ...mapWritableState(useAppStore, ["selected_project", "dashboard_tab"]),
    wpQuestions: function () {
      var project =  questions.find(program => program.id == this.selected_project);
      var wp = project.workpackage.find(wp => wp.id == this.dashboard_tab);
      return wp.questions
    },
  },
  methods: {
    async validate() {
      const { valid } = await this.$refs.form.validate();

      if (valid) alert("Form is valid");
    },
  },
};
</script>
  