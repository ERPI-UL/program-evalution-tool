<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-img contain height="400" :src="error" />

      <!-- <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>
  
        <h1 class="text-h2 font-weight-bold">Error</h1> -->

      <!-- <div class="py-14" /> -->

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            color="primary"
            :href="{ name: 'Home' }"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            target="_blank"
            variant="flat"
          >
            <v-icon icon="mdi-speedometer" size="large" start />Page d'accueil
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>
  
<script setup>
import error from "@/assets/error404.svg";
</script>
  