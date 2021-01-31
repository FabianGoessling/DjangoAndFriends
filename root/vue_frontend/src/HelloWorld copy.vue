<template>
  <div
    class="bg-white shadow-xl hover:shadow-2xl dark:bg-gray-800 dark:border-gray-800 p-4 rounded-md border w-6/12 md:w-3/12"
  >
    <div class="flex justify-between">
      <div class="flex items-center">
        <img
          class="h-30 w-30 rounded-full"
          src="https://pbs.twimg.com/profile_images/1287562748562309122/4RLk5A_U_x96.jpg"
        />
        <div class="ml-3.5 text-xl leading-tight">
          <span class="text-black dark:text-white font-bold block">{{
            title
          }}</span>
        </div>
      </div>
    </div>
    <p
      class="text-black dark:text-white block text-sm sm:text-sm leading-snug mt-3"
    >
      {{ msg }}
    </p>
    <div
      class="border-gray-200 dark:border-gray-600 border border-b-0 my-1"
    ></div>
    <div class="text-gray-500 dark:text-gray-400 flex mt-3"></div>
    <div class="flex justify-end">
      <div class="mt-1 py-1 px-1 rounded-sm text-sm text-gray-400">v 0.0.1</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: ["msg", "title"],
};
</script>

