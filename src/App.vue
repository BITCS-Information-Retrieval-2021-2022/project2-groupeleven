<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  /* margin-top: 60px; */
  width: 100%;
  height: 100%;
}
html{
  width: 100%;
  height: 100%;
}
body {
  height: 100%;
  width: 100%;

}
a {
  text-decoration: none;
}
a:hover,
a:visited,
a:link,
a:active {
  text-decoration: none;
  color: inherit;
}
</style>
