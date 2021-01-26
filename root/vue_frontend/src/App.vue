<template>
  <HelloWorld title="Title One" msg="Welcome to Your Vue.js App" />
  <HelloWorld title="Title 2" msg="This works" />
  <HelloWorld title="Title 3" msg="Pretty Easy" />
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