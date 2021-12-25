<template>
  <el-container style="height: 100%">
    <el-header style="height: 40px" >
      <LocalHeaders />
    </el-header>
    <el-main class="search-center" v-if="this.switchvalue === false">
      <search-windows ref="searchwindows" style="padding-bottom: 0%" />
    </el-main>
    <el-main v-if="this.switchvalue === true">
      <advanced-search style="padding-bottom: 0%;padding-top: 12%" />
    </el-main>

  </el-container>
</template>
<script>
import SearchWindows from "./SearchWindows.vue";
import CopyRight from "./CopyRight.vue";
import LocalHeaders from "./LocalHeaders.vue";


export default {
  name: "index",
  components: {
    SearchWindows,
    CopyRight,
    LocalHeaders,

  },
  data() {
    return {
      switchvalue: false,
    };
  },
  created() {
    let body = document.querySelector("body");
    body.addEventListener(
      "click",
      (e) => {
        this.$refs.searchwindows.deletsuggestlist();
      },
      false
    );
  },
};
</script>
<style scoped>
.search-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
