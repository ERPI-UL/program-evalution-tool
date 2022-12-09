<template>
  <div class="home" >
    <v-parallax :src="crowdImg"  height="300"  >
    <div class="d-flex flex-column fill-height justify-center align-center text-white">
      <h2 class="text-h2 font-weight-bold mb-4 text-blue-lighten-1">
        Program Evaluation Tool
      </h2>
      <p class="subheading font-weight-medium text-blue-lighten-1">
        Outil d'évaluation de l'impact des programmes basés sur le modèle d'innovation Triple helices.
      </p>
    </div>
  </v-parallax>
  <v-container>
    <v-row>
      <v-col align-self="center">
        <h2>Objectif</h2>
  <p class="">Cette outil à pour ambition de structurer la démarche d'évaluation de l'impact d'un programme pour choisir la démarche et les indicateurs les plus adaptés. L'outil tend a acompagner la formalisation du programme pour cerner au mieux les indicateurs et ainsi generer les formulaires de collècte d'information ainsi que les tableaux de bords pour suivre l'avancement du programme dans le temps. Les infromations présentes dans cet outils proviennt de la literature scientifique, notament les indicateurs.</p>
  <h2>Fonctionnalités</h2>
  <v-list lines="two">
    <v-list-item title="Espace individual" subtitle="Possiblité de créer un compte pour créer et gerer autant de programme souhaité."></v-list-item>
    <v-list-item title="Approche structuré" subtitle="Formalisation du programme et des indicateurs selon le principe de la chaine de résultats."></v-list-item> 
    <v-list-item title="Base de données d'indicateur" subtitle="Exploration des indicateurs et de leur porté dans la mise en oeuvre d'un programme."></v-list-item>
    <v-list-item title="Formulaire de collecte" subtitle="Création semi-automatique de formulaire de collecte de données pour evaluer les indicateurs associé au programme."></v-list-item>
    <v-list-item title="Tableau de board" subtitle="Génération de tableau de bord pour suivre la progression du programme en fonction des données collectées."></v-list-item>
    <v-list-item title="Structuration du programme" subtitle="Décomposition du programme à évaluer en volet si besoin avec indicateurs, tableau de bords et formulaire respectif."></v-list-item> 
  </v-list>
      </v-col>
    </v-row>
  </v-container>
  
  </div>
</template>

<script setup>
import crowdImg from '@/assets/crowd.jpg'

</script>
