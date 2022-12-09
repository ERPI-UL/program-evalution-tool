<template>
  <v-card width="400" class="mx-auto mt-5" title="Récupération du compte">
    <v-card-text><div><p>Vous allez recevoir une email pour récuperer vote compte.</p></div>
      <v-form>
        <v-text-field label="Email" prepend-icon="mdi-email" :rules="emailRules" v-model="email"/>
      </v-form>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="info" @click="login">Envoyer l'email</v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
import { useUserStore } from "@/stores/UserStore";
import { useProjectStore } from "@/stores/ProjectStore";

export default {
  // props: {errorId: [Number, String]},
  setup(){
    const useUser = useUserStore();
    const useProject = useProjectStore();
    return {useUser, useProject}
  },
  data() {
    return {
      email:null,
      emailRules: [
        value => !!value || "Email is required",
        value => value.indexOf("@") !== 0 || "Email should have a username",
        value => value.includes("@") || "Email should include an @ symbol.",
        value =>
        value.indexOf(".") - value.indexOf("@") > 1 ||
        "Email should contain a valid domain.",
      value =>
        value.indexOf(".") <= value.lenght - 3 ||
        "Email should contain a valid domain extension."
      ],
    };
  },
  computed:{
    emailIsValid(){
        return !!this.email
    }
  },
  methods: {
    login () {
      //console.log("Login - email: "+ this.email);
      this.useUser.accountRecovery(this.email);
    },
  },
/*   mounted() {
    if(this.errorId ){
        this.alert = true
        this.message = this.errorMsgs.find(error => error.id == this.errorId).msg;
      }else{
        this.alert = false
      }
  } */
};
</script>