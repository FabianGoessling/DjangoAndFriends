<template>
  <div>
    {{ title }}
    <v-btn color="success" dark>
      <v-icon> mdi-check </v-icon>
    </v-btn>
    {{ msg }}
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["msg", "title"],
};
</script>
