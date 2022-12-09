<template>
  <v-container>
    <h1>{{ program.name }}</h1>
    <v-row>
      <v-col cols="2"><p>Start Date</p></v-col>
      <v-col cols="2">{{ program.start }}</v-col></v-row
    >
    <v-row>
      <v-col cols="2"><p>End Date</p></v-col>
      <v-col cols="2">{{ program.start }}</v-col></v-row
    >
    <h2>Description</h2>
    <p>{{ program.description}}</p>
    <h2>Objectives</h2>
    <v-list dense>
      <v-list-item v-for="(item, i) in program.objectif" :key="i" :title="item">
      </v-list-item>
    </v-list>
    <h2>Workpackages</h2>
    <v-list dense>
      <v-list-item v-for="(item, i) in program.workpackage" :key="i" :title="item">
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script>
export default {
  props: ["progid"],
  data() {
    return {
      program: {
        name: "SIRIUS",
        start: "02/2022",
        end: "12/2029",
        description:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non ipsum sagittis, fringilla nisl et, scelerisque dui. Nunc pellentesque, velit sed lobortis fermentum, nisi dolor commodo erat, a mollis orci orci ac orci. Nunc augue ipsum, suscipit vel auctor in, blandit id ligula. Ut pretium pellentesque arcu in lacinia. Mauris fringilla cursus commodo. Suspendisse potenti. Nullam tempus auctor vehicula. Cras et ex vel urna gravida maximus. Morbi sed blandit urna. Etiam convallis dui in nunc sagittis, sit amet aliquet massa eleifend. Maecenas vel massa massa. Sed fringilla sed lorem et tincidunt. Sed consequat ante sit amet neque accumsan, nec dictum elit rhoncus. Donec ac ipsum non eros commodo sodales. ",
        objectif: [
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales tortor lorem, et pharetra nibh.",
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales tortor lorem, et pharetra nibh. ",
        ],
        workpackage: ["Lorem 1", "Lorem 2", "Lorem 3"],
      },
    };
  },
};
</script>
