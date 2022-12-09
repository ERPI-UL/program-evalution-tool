<template>
  <v-card width="400" class="mx-auto mt-5" title="Register">
    <v-card-text>
      <v-form>
        <v-text-field
          label="Username"
          prepend-icon="mdi-account-circle"
          v-model="username"
        />
        <v-text-field label="Email" prepend-icon="mdi-email" v-model="email" />
        <v-text-field
          :type="showPassword ? 'text' : 'password'"
          label="Password"
          prepend-icon="mdi-lock"
          :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append-inner="showPassword = !showPassword"
          v-model="password"
        />
      </v-form>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-btn color="success" to="/login">Login</v-btn>
      <v-spacer></v-spacer>
      <v-btn color="info" @click="register">Register</v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
import { account } from "@/plugins/appwrite";
import { ID } from "appwrite";
import router from '@/router';

export default {
  data() {
    return {
      showPassword: false,
      username: null,
      email: null,
      password: null,
    };
  },
  computed: {
    usernameIsValid() {
      return !!this.username;
    },
    passwordvalid() {
      return this.password.len;
    },
  },
  methods: {
    register() {
      console.log("Register");
      account
        .create(ID.unique(), this.email, this.password, this.username)
        .then(
          (response) => {
            console.log(response);
            account.createEmailSession(this.email, this.password);
            router.push({name: "Programs"})
          },
          (error) => {
            console.log(error);
          }
        );
    },
  },
};
</script>