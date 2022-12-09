/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'
import router from './router'

// Composables
import { createApp } from 'vue'


// Plugins
import { registerPlugins } from '@/plugins'
import { markRaw } from 'vue'
import vuetify from './plugins/vuetify'
import VueApexCharts from 'vue3-apexcharts'

import store from "@/stores/Store";

const app = createApp(App);

registerPlugins(app);

store.use(({ store }) => { store.router = markRaw(router) });

app.use(store);
app.use(router)
  .use(vuetify)
  .use(VueApexCharts);

  router.isReady().then(() => {
    app.mount("#app");
  });