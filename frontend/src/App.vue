<template>
 <v-app id="inspire">
  <HelloWorld title="Title One" msg="Welcome to Your Vue.js App" >
  </HelloWorld>

  <HelloWorld title="Title 2" msg="Wow" >
  </HelloWorld>
  
  <HelloWorld title="Title 3" msg="AHa" >
  </HelloWorld>
  
    <HelloWorld title="Gisela" msg="Hallo" >
  </HelloWorld>

   <v-card
      class="mx-auto"
      max-width="344"
      outlined
    >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">
            OVERLINE
          </div>
          <v-list-item-title class="headline mb-1">
            Headline 5
          </v-list-item-title>
          <v-list-item-subtitle>Greyhound divisely hello coldly fonwderfully</v-list-item-subtitle>
        </v-list-item-content>
  
        <v-list-item-avatar
          tile
          size="80"
          color="grey"
        ></v-list-item-avatar>
      </v-list-item>
  
      <v-card-actions>
        <v-btn
          outlined
          rounded
          text
        >
          Button
        </v-btn>
      </v-card-actions>
    </v-card>
   </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",

  components: {
    HelloWorld,
  },
};
</script>