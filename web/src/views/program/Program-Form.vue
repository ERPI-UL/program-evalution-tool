<template>
    <v-container>
      <v-row>
        <v-col
          ><h2>Nouveau Programme</h2>
          <p>Formulaire de création d'un nouveau programme.</p>
        </v-col>
      </v-row>
  
      <v-form ref="form" v-model="valid" lazy-validation> </v-form>
      <v-text-field
        v-model="name"
        :rules="nameRules"
        label="Name"
        required
      ></v-text-field>
      <v-text-field v-model="startDate" label="Date de début du programme"></v-text-field>
      <v-text-field v-model="endDate" label="Date de fin du programme"></v-text-field>
      <v-textarea  v-model="description" label="Description"></v-textarea>
      <v-text-field v-model="objective" label="Objectif"></v-text-field>
      <v-text-field v-model="workpackage" label="Volet"></v-text-field>
      <v-select
        multiple
        v-model="freq"
        :items="items"
        :rules="[(v) => !!v || 'Item is required']"
        label="Féquence d'évaluation"
        required
      ></v-select>
      <v-btn color="success" class="mr-4" @click="validate"> Enregister </v-btn>
    </v-container>
  </template>
  <script>
  export default {
    data: () => ({
      valid: true,
      name: null,
      startDate: null,
      endDate:null,
      freq: null,
      description: null,
      objective:null,
      workpackage:null,
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length > 3) || "Name must be larger than 3 characters",
      ],
      items: [
        { label: "Hebdo", value: "weekly" },
        { label: "Mensuel", value: "monthly" },
      ],
    }),
    methods: {
      async validate() {
        const { valid } = await this.$refs.form.validate();
  
        if (valid) alert("Form is valid");
      },
    },
  };
  </script>
  