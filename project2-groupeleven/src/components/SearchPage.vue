<template>
  <!-- 此页面用来展示搜索结果 需要展示姓名、机构、职称、领域、照片-->
  <div :style="backgroundDiv" style="height: 100%">
    <el-container style="height: 100%">
      <el-header class="container hc_header">
        <el-row :gutter="10" style="z-index: 10">
          <el-col :span="4" style="margin-top: 10px">
            <img src='../../static/images/hat.jpg' width="45" height="30">
            <span
              @click="returnIndexPage"
              style="float: left; font-size: 25px; font-weight: bold"
            >Scholar Search
            </span>
          </el-col>

          <el-col :span="6" style="margin-top: 10px">
            <el-input
              id="searchInput"
              v-model="wd"
              @keyup.enter.native="submitWd"
            >44分
              <el-button slot="append" @click="submitWd_thispage"
              >搜索</el-button
              >
            </el-input>
          </el-col>

        </el-row>
      </el-header>
      <!-- 检索范围选择 -->
      <div
        style="
          clear: both;
          padding: 2px;
          margin-left: 20px;
          margin-right: 20px;
        "
      >
        <!-- <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="All" name="first">All</el-tab-pane>
          >
        </el-tabs> -->
      </div>
      <!-- 排序方式选项 -->
      <div>
        <div
          style="
            clear: both;
            padding: 3px;
            margin-left: 20px;
            margin-right: 180px;
          "
        >
          <span style="float: right">About {{ this.total }} results ({{
              this.returntime
            }}
            seconds)</span>
        </div>
      </div>


      <el-main>
        <el-card class="box-card" v-for="(result, index) in info">
          <el-row>
            <el-col :span="2"> <img src='../../static/images/avator.jpg' width="50" height="60"></el-col>
            <el-col :span="19">
              <el-row>
                <el-col :span="3">
                  <a style="
                    text-align: left;
                    color: #2196f3;
                    max-width: 70%;
                    font-weight: bold;
                    font-size: 22px;
                  " @click="jump2info(result)">{{ result.name }}</a>
                </el-col>
                <el-col :span="3">
                  <p style="
                    padding-top: 2px;
                    font-size: 16px;
                    margin-top: 5px;
                  ">
                    <span style="color: #ff5722">职称:&nbsp;</span>
                    <span>{{ result.title }}</span>
                  </p>
                </el-col>
                <el-col :span="13">
                  <p style="
                    padding-top: 2px;
                    font-size: 16px;
                    margin-top: 5px;
                  ">
                    <span style="color: #009688">研究机构:&nbsp;</span>{{ result.mechanism }}
                  </p>
                </el-col>
              </el-row>
              <el-row>
                <p style="padding-top: 10px; font-size: 16px;margin-top: 5px;">
                  <span style="color: #ff5722">研究领域:&nbsp;</span>
                  <span v-for="fd in result.field">{{ fd }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
                </p>
              </el-row>



            </el-col>
          </el-row>

        </el-card>

      </el-main>
      <!--</el-container>-->

      <!--    下方的页码导航条 page-size规定每页的结果个数 page-count为总共的页数-->
      <div class="block hc_page" v-if="showPage">
        <el-pagination
          background
          :page-size="pageSize"
          :page-count="pageCount"
          :current-page.sync="currentPage"
          layout="prev, pager, next"
          @current-change="judge"
        >
        </el-pagination>

      </div>


    </el-container>
    <div
      v-loading="loading"
      :style="loadingBox"
      v-if="loading == true ? true : false"
    ></div>
  </div>
</template>

<script>

export default {
  name: "SearchPage",
  data() {
    return {
      backgroundDiv: {
        backgroundImage: 'url(' + require('../../static/images/cool-background.png') + ')',
        backgroundRepeat: 'no-repeat',
        backgroundSize: "cover",
      },
      hotwd: ["1", "2", "3", "4", "5", "6"],
      wd: this.$route.query.keyword, //传来的keyword
      theme: this.$route.query.theme, //传来的theme
      order: "", //排序0 1 2，
      year: "", //检索年份 多个用，隔开
      pagefrom: "", //来自哪个页面 1普通搜索 2高级搜索
      form: this.$route.query.form,
      getWd: "",
      total: "",
      returntime: "",
      pageSize: 10,
      pageCount: 100,
      currentPage: 0,
      showPage: false,
      info: [],
      loading: false,
      loadingBox: {
        position: "fixed",
        top: "65px",
        width: "100%",
        height: "",
      },
      // flag:true // 判定是否是初次加载
    };
  },
  watch: {
    order: function (val, oldVal) {
      console.log('order watch:'+val);
      if (this.pagefrom === "1") {
        this.submitWd();
      } else {
        this.advancedSearch(this.form);
      }
    },
  },
  created() {
    this.getHeight();
  },
  mounted: function () {
    // 页面加载时需要触发的函数
    this.judge();
  },
  methods: {
    judge() {
      if (this.$route.query.keyword != undefined) {
        console.log("跳转来自：普通检索");
        this.pagefrom = "1";
        this.submitWd();
      }
    },
    getHeight() {
      this.loadingBox.height = window.innerHeight - 65 + "px";
    },
    jump2info(thispageparams) {
      this.$router.push({
        path: "/profile",
        query: { Infos: thispageparams },
      });
    },
    returnIndexPage() {
      this.$router.push({ path: "/" });
    },
    submitWd_thispage() {
      //此界面为普通搜索 把其他条件都清空
      console.log('在本页进行搜索');
      this.theme = "";
      this.submitWd();
    },

    //后台请求数据
    submitWd() {
      this.goTop();
      // 如果检索词为空
      if (this.wd == "") {
        this.info = [];
        this.getWd = "";
        this.showPage = false;
      } else {
        console.log('this.wd '+this.wd)
        this.loading = true;
        this.getWd = this.wd;
        this.page = 0;
        let date1 = new Date();
        let second1 = date1.getSeconds();
        let millisecond1 = date1.getMilliseconds();
        this.axios
        .get(
         "http://127.0.0.1:8000/search?query=" +
                      this.getWd +
                      "&theme=" +
                      this.theme +
                      "&page=" +
                      this.currentPage
                     // '../../static/mock/index.json'
          )
          .then((response) => {
            //alert("ok");
            //console.log('response:'+response.data);
            //console.log('response0 stringify:'+JSON.stringify(response.data[0]));
            //console.log('response0 name:'+response.data[0]["name"]);
            //console.log('response info:'+response.data[0].name);
            //console.log('response total:'+response.data.length);
            //console.log('total:'+response.data.total)
            //this.total = response.data.length;
            if (response.data.length % 10 != 0) {
              this.pageCount = Math.floor(response.data.value / 10) + 1;
              this.showPage = true;
            } else {
              this.pageCount = response.data.value/ 10;
              this.showPage = true;
            }
            // this.info = JSON.parse(response.data);
            this.info = response.data.data;//Belle
            //this.info = response.data
            this.loading = false;
            let date2 = new Date();
            let second2 = date2.getSeconds();
            let millisecond2 = date2.getMilliseconds();
            console.log(second1);
            console.log;
            //检索时间
            if (second2 - second1 > 0) {
              this.returntime = second2 - second1;
            } else if (second2 === second1) {
              if (millisecond2 - millisecond1 > 0) {
                this.returntime = (millisecond2 - millisecond1) / 1000;
              } else {
                this.returntime = (1000 + millisecond2 - millisecond1) / 1000;
              }
            }
          })
          .catch((err) => {
            // alert("error");
            console.log("err:"+err);
            this.info = [];
            this.showPage = false;
            this.loading = false;
          })
          .finally(() => {});
      }
    },
    //请求第val页的结果 接口接收keyword+val 返回page-size个第val页的检索结果
    submitPage(val) {
      if (this.wd == "") {
        if (this.getWd != "") {
          this.wd = this.getWd;
          this.submitRealForPage(val);
        } else {
          this.info = [];
        }
      } else {
        this.submitRealForPage(val);
      }
    },
    submitRealForPage(val) {
      this.loading = true;
      this.submitWd();
    },
    goTop() {
      // 回到顶部
      document.body.scrollTop = document.documentElement.scrollTop = 0;
    },
  },
};
</script>

<style>
/* 解决body和div之间间隔 */
* {
  margin: 0px;
  padding: 0px;
}
.container {
  width: 100%;
  height: 100%;
  z-index: 1;
}
.el-input__inner {
  border-bottom: 2px #cccccc solid;
  border-top: 2px #cccccc solid;
  border-left: 2px #cccccc solid;
  border-right: none;
  border-bottom-left-radius: 10px;
  border-top-left-radius: 10px;
}
.el-input__inner:focus {
  border-bottom: 2px #4e6ef2 solid;
  border-top: 2px #4e6ef2 solid;
  border-left: 2px #4e6ef2 solid;
}
.el-input-group__append {
  border: none !important;
  background-color: white;
}
.el-button {
  color: white !important;
  border-left: none !important;
  border-bottom-left-radius: 0px;
  border-top-left-radius: 0px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  border: 1px #4e6ef2 solid !important;
  background-color: #4e6ef2 !important;
}
.el-button:hover {
  background-color: #4662d9 !important;
}
.t {
  font-weight: 400;
  font-size: medium;
  margin-bottom: 1px;
  line-height: 1.54;
}
.hot {
  color: #666666;
}
.hot:hover {
  color: blue;
}
em {
  color: brown;
}
.hc_header {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12);
  height: 100px;
  background-color: white;
}
.hc_logo {
  float: left;
  margin-top: -7px;
  padding-left: 10px;
  padding-right: 25px;
}
.hc_hotwd {
  text-align: right;
  padding-top: 35px;
  font-size: 13px;
}
.navbar-collapse {
  flex-basis: 100%;
  flex-grow: 1;
  align-items: center;
}
.navbar-nav {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
.mr-auto,
.mx-auto {
  margin-right: auto !important;
}
.nav-link {
  display: block;
  padding: 0.5rem 1rem;
}
.navbar-nav {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}
.hc_contentfooter {
  font-size: 13px;
  text-align: left;
  margin-top: 10px;
}
.hc_page {
  float: left;
  margin-bottom: 40px;
  margin-top: 10px;
  margin-left: 140px;
}
.hc_footer {
  width: 100%;
  background: rgba(0, 0, 0, 0.1);
  height: 40px;
  clear: both;
  color: #666;
  padding-top: 10px;
  font-size: 13px;
  /* position: fixed; */
  bottom: 0px;
  text-align: center;
}
.box-card {
  margin-bottom: 20px;
  margin-left: 20px;
  padding-left:30px;
  width: 95%;
}
</style>
