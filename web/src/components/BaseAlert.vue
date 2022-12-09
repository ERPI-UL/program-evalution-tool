<template>
  <v-alert
    dense
    outlined
    :type="alertobj.type"
    closable
    transition="scale-transition"
    close-label="Close Alert"
    @click="removeAlert(alertobj.id)"
  >
    {{ alertobj.msg }}
    <!-- <v-row align="center" justify="center">
      <v-col class="grow">{{alertobj.msg}}</v-col>
      <v-col class="shrink">
        <v-btn icon @click="removeToast">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-col>
    </v-row> -->
  </v-alert>
</template>

<script>
import { useAlertStore } from "@/stores/AlertStore";
import { mapActions } from "pinia";
export default {
  name: "Alert",
  setup(){
    const useAlert = useAlertStore();
    return {useAlert}
  },
  props: {
    alertobj: {
      type: Object,
      required: true,
    },
  },
  methods: {
    ...mapActions(useAlertStore, ["removeAlert"]),
    // removeToast(id) {
    //   this.$store.dispatch("deleteAlert", id);
    // }
  },
  mounted() {
    if (this.alertobj.duration) {
      
      setTimeout(() => {
        this.useAlert.removeAlert(this.alertobj.id);
      }, this.alertobj.duration);
    }
    // var duration = 4000;
    // if (this.alertobj.duration) {
    //   duration = this.alertobj.duration;
    // }
    // setTimeout(() => {
    //   this.removeToast(this.alertobj.id);
    // }, duration);
  },
};
</script>