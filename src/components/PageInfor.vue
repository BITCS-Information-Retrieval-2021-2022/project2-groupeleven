<template>
  <div>
    <el-header class="container hc_header">
      <el-row :gutter="20" style="z-index: 10">
        <el-col :span="4" style="margin-top: 10px">
          <span
            @click="returnIndexPage"
            style="float: left; font-size: 25px; font-weight: bold"
            >Paper Search
          </span>
        </el-col>
        <el-col :span="5" style="margin-top: 10px">
          <el-input
            id="searchInput"
            v-model="wd"
            @keyup.enter.native="returnResultPage"
          >
            <el-button slot="append" @click="returnResultPage"
              >搜一下</el-button
            >
          </el-input>
        </el-col>
      </el-row>
    </el-header>

    <el-container class="container" direction="	horizontal">
      <el-aside width="10%"></el-aside>
      <el-container class="container" direction="vertical">
        <el-main>
          <!-- 文章标题和作者姓名，作者姓名可能为空值 -->
          <el-row>
            <h2 id="papertitle">
              <a>{{ title }}</a>
            </h2>
            <div id="paperauthors" v-if="authors">
              <div id="authordiv">
                <li id="authorli">{{ authors }}</li>
              </div>
            </div>
            <el-divider content-position="center"></el-divider>
          </el-row>
        </el-main>

        <el-main
          ><!-- 文章视频和标题，根据是否有视频url判断是否显示-->
          <div class="grid-content bg-purple">
            <!-- 文章视频 判断是否为本地-->
            <div id="vidiosize" v-if="this.localvideo" class="content_video">
              <!-- 使用组件video-player -->
              <video-player
                class="video-player vjs-custom-skin"
                ref="videoPlayer"
                :playsinline="true"
                :options="playerOptions"
              ></video-player>
            </div>
            <!-- 如果不是本地 展示视频链接 -->
            <h2 v-if="!this.localvideo">
              <a>视频链接:{{ this.playerOptions.sources[0].src }}</a>
            </h2>
          </div>
          <div class="grid-content bg-purple">
            <!-- 文章视频-->
            <el-row>
              <div id="vediotitle" v-if="VedioTitle">{{ VedioTitle }}</div>
            </el-row>

            <el-row
              ><!-- 视频发布时间和关键字-->

              <el-col :span="24"
                ><!-- 视频关键字-->
                <div id="keywordsinvedio" v-if="KeywordsinVedio">
                  <div id="keyword" v-for="word in KeywordsinVedio">
                    <div id="keywordli">
                      {{ word.keyword }}&nbsp&nbsp&nbsp&nbsp
                    </div>
                  </div>
                </div>
              </el-col>
            </el-row>
            <el-divider content-position="center"></el-divider>
          </div>
        </el-main>

        <el-main
          ><!-- 文章摘要 -->
          <el-row>
            <el-col :span="24">
              <div class="grid-content bg-purple">
                <!-- 根据传值是否为空显示文章摘要-->
                <el-card class="box-card" shadow="hover">
                  <div v-if="abstract" class="clearfix">
                    <span><strong>ABSTRACT</strong></span>
                    <el-divider content-position="center"></el-divider>
                    <div>{{ abstract }}</div>
                  </div>
                  <div v-else="abstract" class="clearfix">
                    <span>ABSTRACT</span>
                    <el-divider content-position="center"></el-divider>
                    <div>------</div>
                  </div>
                </el-card>
              </div>
            </el-col>
          </el-row>
        </el-main>

        <el-main
          ><!-- 出版社、PDF按钮、代码链接按钮、数据集按钮 -->
          <el-row>
            <el-col :span="19"
              ><!-- 根据传值是否为空显示文章摘要、出版社等内容-->
              <el-divider content-position="center"></el-divider>
              <div id="paperInfordiv1">
                <div id="paperinfordetail1"><strong>AnthologyID:</strong></div>
                <div id="paperinfordetail2" v-if="AnthologyID">
                  {{ AnthologyID }}
                </div>
                <div id="paperinfordetail3" v-else="AnthologyID">------</div>
              </div>
              <el-divider content-position="center"></el-divider>
              <div id="paperInfordiv2">
                <div id="paperinfordetail4"><strong>Pulisher:</strong></div>
                <div id="paperinfordetail5" v-if="Pulisher">{{ Pulisher }}</div>
                <div id="paperinfordetail6" v-else="Pulisher">------</div>
              </div>
              <el-divider content-position="center"></el-divider>
              <div id="paperInfordiv3">
                <div id="paperinfordetail7"><strong>DOI:</strong></div>
                <div id="paperinfordetail8" v-if="DOI">{{ DOI }}</div>
                <div id="paperinfordetail9" v-else="DOI">------</div>
              </div>
              <el-divider content-position="center"></el-divider>
              <div id="paperInfordiv4">
                <div id="paperinfordetail10"><strong>PublishAt:</strong></div>
                <div id="paperinfordetail11" v-if="PublishAt">
                  {{ PublishAt }}
                </div>
                <div id="paperinfordetail12" v-else="PublishAt">------</div>
              </div>
              <el-divider content-position="center"></el-divider>
            </el-col>

            <el-col :span="5"
              ><!-- 根据传值是否为空动态调整显示PDF按钮、代码链接按钮、数据集按钮的显示和跳转 -->
              <div class="grid-content bg-purple-light">
                <el-container direction="vertical">
                  <el-main class="linkbutn" v-if="PDF"
                    ><el-button
                      icon="el-icon-files"
                      v-on:click="jump_to_url(PDF)"
                      class="linkbutton"
                      type="primary"
                      >PDF</el-button
                    ></el-main
                  >
                  <el-main class="linkbutn" v-if="Source_url"
                    ><el-button
                      v-on:click="jump_to_url(Source_url)"
                      class="linkbutton"
                      type="primary"
                      >Codes</el-button
                    ></el-main
                  >
                  <el-main class="linkbutn" v-if="Dataset_url"
                    ><el-button
                      icon="el-icon-s-data"
                      v-on:click="jump_to_url(Dataset_url)"
                      class="linkbutton"
                      type="primary"
                      >Data</el-button
                    ></el-main
                  >
                </el-container>
              </div>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
      <el-aside width="10%"></el-aside>
    </el-container>
  </div>
</template>

<script>
import { videoPlayer } from "vue-video-player";
import "video.js/dist/video-js.css";
export default {
  name: "PageInfor",
  data() {
    return {
      info: this.$route.query.Infos, //传递过来的参数
      wd: "", //检索关键字
      localvideo: "", //是否本地视频 1 本地视频 0 别的视频
      title: "",
      authors: [],
      PDF: "",
      Source_url: "", //代码
      Dataset_url: "", //数据集
      abstract: "",
      AnthologyID: "",
      Pulisher: "",
      DOI: "",
      PublishAt: "",
      VedioTitle: "",
      KeywordsinVedio: [{ keyword: "keyword1" }, { keyword: "keyword2" }],
      playerOptions: {
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        playbackRates: [0.7, 1.0, 1.5, 2.0], // 播放速度
        autoplay: false, // 如果true,浏览器准备好时开始回放。
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 导致视频一结束就重新开始。
        preload: "auto", // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        sources: [
          {
            src: "", // 路径
            type: "video/mp4", // 类型
          },
          {
            src: "", //路径
            type: "video/webm", //类型
          },
          {
            src: "", //路径
            type: "rtmp/flv",
          },
        ],
        // width: document.documentElement.clientWidth,
        notSupportedMessage: "此视频暂无法播放，请稍后再试", // 允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true, // 全屏按钮
        },
      },
    };
  },
  components: {
    videoPlayer,
  },
  methods: {
    returnIndexPage() {
      this.$router.push({ path: "/" });
    },
    returnResultPage() {
      if (this.wd === "" || this.wd === undefined || this.wd === null) {
        this.$message("搜索关键字不能为空。");
        return;
      }

      this.$router.push({
        path: "/search",
        query: {
          keyword: this.wd,
          theme: "",
        },
      });
    },
    jump_to_url: function (message) {
      window.open(message, "_blank");
    },
  },
  mounted: function () {
    console.log("传过来的参数" + this.info, this.info.title); //需要触发的函数
    this.title = this.info.title;
    this.authors = this.info.author;
    this.PDF = this.info.pdf;
    this.Dataset_url = this.info.dataset_url;
    this.abstract = this.info.abstract;
    this.Pulisher = this.info.publisher;
    this.PublishAt = this.info.publish_at;
    this.KeywordsinVedio = this.info.keyword_in_video_time;
    this.playerOptions.sources[0].src = this.info.video;
    if (this.info.video.search("39.96.43.48") != -1) {
      this.localvideo = 1; //本地视频 字段为1
    } else {
      this.localvideo = 0;
    }
  },
};
</script>

<style scoped>
.container hc_header {
  width: 100%;
  height: 100%;
  position: fixed;
  z-index: 1;
}
.container {
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
  margin-right: auto;
  margin-left: auto;
}
em {
  color: brown;
}
.hc_header {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12);
  height: 65px;
  background-color: white;
}
.hc_logo {
  width: 100px;
  float: left;
  margin-top: -7px;
  padding-left: 10px;
  padding-right: 25px;
}
#paperauthors {
  height: 15px;
  color: #409eff;
  font-size: large;
  line-break: strict;
}
h2 {
  display: block;
  font-size: 1.5em;
  margin-block-start: 0.83em;
  margin-block-end: 0.83em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
}
h2#papertitle {
  font-size: 2rem !important;
  color: #409eff;
}
.linkbutton {
  width: 60%;
  margin-top: 5px;
}
#authorli {
  list-style-type: none;
  margin-right: 10px;
}
#authordiv {
  float: left;
}
#paperInfordiv1 {
  width: 100%;
  display: table;
}
#paperinfordetail1 {
  width: 20%;
  text-align: right;
  display: table-cell;
}
#paperinfordetail2 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#paperinfordetail3 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#paperInfordiv2 {
  width: 100%;
  display: table;
}
#paperinfordetail4 {
  width: 20%;
  text-align: right;
  display: table-cell;
}
#paperinfordetail5 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#paperinfordetail6 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#paperInfordiv3 {
  width: 100%;
  display: table;
}
#paperinfordetail7 {
  width: 20%;
  text-align: right;
  display: table-cell;
}
#paperinfordetail8 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#paperinfordetail9 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#paperInfordiv4 {
  width: 100%;
  display: table;
}
#paperinfordetail10 {
  width: 20%;
  text-align: right;
  display: table-cell;
}
#paperinfordetail11 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#paperinfordetail12 {
  width: 80%;
  text-align: center;
  display: table-cell;
}
#vediotitle {
  display: block;
  font-weight: bold;
  font-size: 1.9em;
  text-align: left;
  margin-top: 15px;
}
#keyword {
  float: left;
}
#keywordsinvedio {
  font-size: 1.1em;
  margin-top: 9px;
}

.linkbutn {
  text-align: center;
}
.box-card {
  background: #f3faff;
}
#vidiosize {
  text-align: center;
  height: 90%;
  width: 90%;
  margin: auto;
}
</style>
