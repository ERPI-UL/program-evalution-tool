<template>
  <v-container>
    <h1>{{ indicator.name }}</h1>
    <v-row class="text-gey">
      <v-col cols="2"><p>Id</p></v-col>
      <v-col cols="2">{{ indid }}</v-col>
    </v-row>
    <v-row>
      <v-col cols="2"><p>Source</p></v-col>
      <v-col cols="2">{{ indicator.source }}</v-col>
    </v-row>
    <v-row>
      <v-col cols="2"><p>Step</p></v-col>
      <v-col cols="2">{{ indicator.step }}</v-col>
    </v-row>
    <v-row>
      <v-col>
        <h2>Description</h2>
        <p>{{ indicator.description }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: ["indid"],
  data() {
    return {
      indicator: {
        source: "(lorem ipsum, 2022)",
        id: 44444165,
        name: "IND 6",
        step: "output",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
      },
    };
  },
};
</script>