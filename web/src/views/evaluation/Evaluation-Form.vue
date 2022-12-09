<template>
    <v-container>
      <v-row>
        <v-col
          ><h2>Formulaire d'évaluation</h2>
          <p>Formulaire d'ajout d'un indicateur dans la base de donnée.</p>
        </v-col>
      </v-row>
  
      <v-form ref="form" v-model="valid" lazy-validation> 
        <div v-for="quest in questions">
          <v-text-field v-if="quest.type =='text-number'" :label="quest.label" type="number"></v-text-field>
          <v-text-field v-if="quest.type =='text'" :label="quest.label" type="text"></v-text-field>
        </div>
        <v-btn color="success" class="mr-4" @click="validate"> Enregister </v-btn>
      </v-form>
    </v-container>
  </template>
  <script>
  export default {
    data: () => ({
      valid: true,
      questions: [
        {id:"32", label: "Quel est le nombre d'innovation testé sur l'ensemble des lab d'innovation?", type: "text-number" },
        { id:"38", label: "Quel est le nombre total de visite dans l'ensemble des lab d'innovation?", type: "text-number" },
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
  