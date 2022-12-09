<template>
    
    <v-table>
    <thead>
      <tr>
        <th class="text-left">
          Name
        </th>
        <th class="text-left">
          Start Date
        </th>
        <th class="text-left">
          End Date
        </th>
        <th class="text-left">
          Action <v-btn icon variant="plain">
        <v-icon>mdi-plus-circle</v-icon>
      </v-btn>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in programs"
        :key="item.name"
      >
        <td>{{ item.name }}</td>
        <td>{{ item.start }}</td>
        <td>{{ item.end }}</td>
        <td><v-btn icon :to="{name:'ProgramDetail', params: {progid: item.name }}" variant="plain">
        <v-icon>mdi-eye</v-icon>
      </v-btn></td>
      </tr>
    </tbody>
  </v-table>
    
  </template>
  
  
  <script>
  export default {
    data() {
      return {
        programs: [
            {name:"SIRIUS",start:"02/2022",end:"12/2029"},
            {name:"Random",start:"07/2023",end:"06/2028"}
        ],
      };
    },
  };
  </script>