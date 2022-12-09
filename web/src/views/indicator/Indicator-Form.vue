<template>
  <v-container>
    <v-row>
      <v-col
        ><h2>Nouvel Indicateur</h2>
        <p>Formulaire d'ajout d'un indicateur dans la base de donnée.</p>
      </v-col>
    </v-row>

    <v-form ref="form" v-model="valid" lazy-validation> </v-form>
    <v-text-field
      v-model="name"
      :rules="nameRules"
      label="Name"
      required
    ></v-text-field>
    <v-text-field v-model="source" label="Source"></v-text-field>
    <v-text-field v-model="question" label="Question"></v-text-field>
    <v-select
      multiple
      v-model="select"
      :items="items"
      :rules="[(v) => !!v || 'Item is required']"
      label="Etapes"
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
    source: null,
    select: null,
    question: null,
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length > 4) || "Name must be larger than 4 characters",
    ],
    items: [
      { label: "Intrant", value: "input" },
      { label: "Activité", value: "activity" },
      { label: "Production", value: "output" },
      { label: "Resultat", value: "outcome" },
      { label: "Resultat final", value: "finalOutcome" },
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
