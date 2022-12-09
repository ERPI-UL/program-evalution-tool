<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" absolute bottom temporary>
      <v-list-item title="Program Evaluation Tool"> </v-list-item>
      <v-divider></v-divider>
      <v-list v-if="isLogged">
        <v-list-item title="Accès rapide"> </v-list-item>
      <v-select
        clearable
        density="compact"
        v-model="selected_project"
        label="Programme"
        :items="projects"
        item-title="name"
        item-value="id"
      ></v-select>
    </v-list>
      
      <v-divider></v-divider>
      <v-list dense nav v-if="isLogged">
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.parameters ? { name: item.to, params: item.parameters }:{ name: item.to }"
          :prepend-icon="item.icon"
          :title="item.title"
        >
        </v-list-item>
      </v-list>
      <v-list dense nav v-else>
        <v-list-item key="accueil" link :to="{name: 'Home'}" prepend-icon="mdi-home" title="Accueil"></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <!-- <v-toolbar-title>Program Evaluation Tool</v-toolbar-title> -->
      <v-spacer></v-spacer>

      
      <v-tooltip
        location="bottom" 
        v-if="showProgAdd"
      ><template v-slot:activator="{ props }"><v-btn
        :to="{ name: 'Program-Form' }"
        v-bind="props"
        icon="mdi-plus-circle" 
      > </v-btn> </template>Creer un nouveau programme</v-tooltip>

      <v-tooltip
        location="bottom" 
        v-if="showIndAdd"
      ><template v-slot:activator="{ props }"><v-btn
        :to="{ name: 'Indicator-Add' }"
        v-bind="props"
        icon="mdi-plus-circle"
      ></v-btn></template>Ajouter un indicateur</v-tooltip>
      

      <v-btn v-if="!isLogged" :to="{ name: 'LogIn' }"> Log In </v-btn>
      <v-tooltip
        location="bottom"
        v-else
      > <template v-slot:activator="{ props }"> <v-btn v-bind="props" icon="mdi-logout" @click="logout"> </v-btn> </template> Se deconnecter</v-tooltip> 
      
      <template v-slot:extension v-if="(selected_project && showTabs)">
        <v-tabs v-model="dashboard_tab" color="blue" show-arrows>
          <v-tab v-for="wp in projects.find(project => project.id == selected_project).workpackage" :value="wp.id">{{
        wp.name
      }}</v-tab>
        </v-tabs>
      </template>
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <div v-if="hasAlert">
        <v-container>
          <BaseAlert
            v-for="alert in alerts"
            :alertobj="alert"
            :key="alert.id"
          ></BaseAlert>
        </v-container>
      </div>

      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
import { useUserStore } from "@/stores/UserStore";
import { useAlertStore } from "@/stores/AlertStore";
import { useProjectStore } from "@/stores/ProjectStore";
import { useAppStore} from "@/stores/AppStore";
import { mapState, mapWritableState} from "pinia";
import BaseAlert from "@/components/BaseAlert.vue";

export default {
  components: {
    BaseAlert,
  },
  setup() {
    const alertStore = useAlertStore();
    const projectStore = useProjectStore();
    const userStore = useUserStore();
    const appStore = useAppStore();
    return { alertStore, projectStore, userStore, appStore};
  },
  data() {
    return {
      drawer: false,
      items: [
        { title: "Programs", icon: "mdi-card-text", to: "Programs" , parameters: null},
        { title: "Indicators", icon: "mdi-gauge", to: "Indicators", parameters: null },
        { title: "Evaluation", icon: "mdi-clipboard-list", to: "Evaluations" , parameters: null},
        { title: "Dashboard", icon: "mdi-view-dashboard", to: "Dashboards", parameters: null },
      ],
    };
  },
  watch: {
    group() {
      this.drawer = false;
    },
    selected_project(newProj){
      console.log("new links")
      if(newProj != null){
        this.items = [
        { title: "Programs", icon: "mdi-card-text", to: "Programs", parameters: null},
        { title: "Indicators", icon: "mdi-gauge", to: "Indicators", parameters: null},
        { title: "Evaluation", icon: "mdi-clipboard-list", to: "Project-Evalution-Form", parameters: {projid: this.selected_project} },
        { title: "Dashboard", icon: "mdi-view-dashboard", to: "Project-Dashboard", parameters:{projid: this.selected_project} },
      ]
      }else{
        this.items = [
        { title: "Programs", icon: "mdi-card-text", to: "Programs" , parameters: null},
        { title: "Indicators", icon: "mdi-gauge", to: "Indicators" , parameters: null},
        { title: "Evaluation", icon: "mdi-clipboard-list", to: "Evaluations" , parameters: null},
        { title: "Dashboard", icon: "mdi-view-dashboard", to: "Dashboards", parameters: null },
      ]
      }
    }
  },
  methods: {
    logout () {
      console.log("Logout");
      this.userStore.logout();
    },
  },
  computed: {
    ...mapState(useUserStore, ["isLogged", "userData"]),
    ...mapState(useAlertStore, ["alerts"]),
    ...mapState(useProjectStore, ["projects"]),
    ...mapWritableState(useAppStore, ["selected_project","dashboard_tab"]),
    showTabs(){
      return this.$route.meta.showTabs;
    },
    hasProjects(){
      return this.projectStore.projects.length>0;},
    hasAlert() {
      return this.alertStore.alerts.length > 0;
    },
    showIndAdd() {
      return this.$route.meta.showAddIndBtn;
    },
    showProgAdd() {
      return this.$route.meta.showAddProgBtn;
    },
  },
};
</script>

