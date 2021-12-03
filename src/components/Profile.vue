<template>
  <div :style="backgroundDiv" style="width: 100%; min-height: 100%; ">
    <div >
      <el-container>

        <!--页面头部-->
        <el-header class="container hc_header">
          <el-row :gutter="20" style="z-index: 10">
            <!--页面logo-->
            <el-col :span="4" style="margin-top: 10px" >
              <img src='../../static/images/hat.jpg' width="45" height="30">
              <span
                @click="returnIndexPage"
                style="float: left; font-size: 25px; font-weight: bold"
              >Scholar Search
            </span>
            </el-col>
            <!--页面搜索框-->
            <el-col :span="5" style="margin-top: 10px;float: right;">
              <el-input
                id="searchInput"
                v-model="keyword"
                placeholder="搜索"
                @keyup.enter.native="returnSearchPage"
              >
                <!--页面搜索按钮-->
                <el-button style="background-color:cornflowerblue;color:cornsilk;width:60px" @click="returnSearchPage" slot="append" icon="el-icon-search">
                </el-button>
              </el-input>
            </el-col>
          </el-row>
        </el-header>
        <br/>
        <el-container class="container" direction="	horizontal">
          <!--内容侧边栏-->
          <el-aside width="10%"></el-aside>
          <el-container class="container" direction="vertical" style="background:#FFF">

            <el-main>
              <!--添加学者、照片、职称、所属机构、论文列表名称、研究领域-->

              <el-row>
                <!--作者名-->
                <div class="post-block">
                  <span class="title">{{name}}</span>

                </div>
              </el-row>
            </el-main>
            <!--<el-main>-->
            <el-container class="container" >
              <el-aside width="10%"></el-aside>
              <!-- <el-row :gutter="20">-->
                 <!--<el-col :span="8">-->
                  <el-aside width="10%"></el-aside>
                  <!--学者头像-->
                  <div class="eee2">
                    <div  class="eee"  v-bind:style="{backgroundImage:'url(' + photo + ')'}">
                      <img class="eee1" src="../../static/images/border.png"/>
                    </div>
                  </div>

                  <!--<div style="overflow: hidden; clear: both; height: 300px">
                                 <img
                                   style="float: left; width: 20%"
                                   src="../../static/images/19100122420C335-0-lp.jpg"
                                 />
                 </div>-->
<!--                </el-col>-->
<!--                <el-col :span="12" style="padding-top: 30px;text-align:center;" >-->

                  <!--<div>

                        <p style="padding-top: 2px;font-size: 10px;margin-top: 5px;">
                             <span v-for="(titleq, index) in title">{{titleq}}</span>
                             <span style="color: #009688">{{mechanism}}</span>
                             <span v-for="(paper, index) in papers">{{paper}}</span>
                              <span style="color: #009688">{{field}}</span>


                        </p>
                  </div>-->
                  <!--<div class="text1" >
                    title：<span v-for="(titleq, index) in title">{{titleq}}   </span>
                    <br/>
                    mechanism：<span style="color: #009688">{{mechanism}}</span>
                    <br/>
                    field：<span style="color: #009688">{{field}}   </span>
                  </div>-->
                  <!--label-->
                  <div style="padding-left: 60px;text-align:left;width:700px;overflow: hidden;zoom:1;">

                    <div style="margin-bottom: 1px"><font size="4px">职称：<el-tag type="success" size="medium" >
                    {{title}}
                    </el-tag></font></div>

                    <br/>
                    <div style="margin-bottom: 1px"><font size="4px">研究机构：</font><el-tag type="warning" size="medium">{{mechanism}}</el-tag></div>

                    <br/>
                    <div style="margin-bottom: 5px"><font size="4px">研究领域:</font></div><div style=" overflow: hidden;zoom:1;"><div style="float:left" v-for="(fieldq, index) in field"><el-tag size="medium" >{{fieldq}}</el-tag>&nbsp</div></div>

                  </div>
<!--                </el-col>-->



<!--              </el-row>-->


            </el-container>
            <!--<el-main>-->
            <br/>
            <!--<el-divider ><span style="font-weight: bold;font-size: 15px;margin-bottom: 10px;font-family:黑体-简;">文章列表</span></el-divider>-->

            <div
              style="
          clear: both;
          padding: 20px;
          margin-left: 20px;
          margin-right: 20px;
        "
            ></div>

            <div class="tableTitle"><span class="midText">文章列表</span></div>
            <div
              style="
          clear: both;
          padding: 20px;
          margin-left: 20px;
          margin-right: 20px;
        "
            ></div>
            <br/>
            <br/>



            <!--有发表日期的的文章-->
            <!--<div class="block">
              <div class="radio">
                排序：
                <el-radio-group v-model="reverse">
                  <el-radio :label="true">倒序</el-radio>
                  <el-radio :label="false">正序</el-radio>
                </el-radio-group>
              </div>

              <el-timeline :reverse="reverse">
                <el-timeline-item
                  v-for="(activity, index) in activities"
                  :key="index"
                  :timestamp="activity.timestamp">
                  {{activity.content}}
                </el-timeline-item>
              </el-timeline>
            </div>-->
            <!--没有时间的文章-->
            <div class="block" style="padding-left:100px" >
              <el-timeline>
                <el-timeline-item
                  v-for="(paper, index) in papers">
                  {{paper}}
                </el-timeline-item>
              </el-timeline>
            </div>
            <!--将influenced和influenced_by利用echarts做图形展示-->
            <el-main>
              人物关系图网
              <div>
                <el-tabs>
                  <el-tab-pane>
                    <span slot="label"> influenced</span>
                    <div>
                      <div id="main" style="width: 600px;height:400px;"></div>

                    </div>
                  </el-tab-pane>
                  <el-tab-pane label="influenced_by">
                    <div c>
                      <div id="main2" style="width: 600px;height:400px;"></div>
                    </div>
                  </el-tab-pane>


                </el-tabs>
              </div>




            </el-main>
          </el-container>
          <el-aside width="10%"></el-aside>
        </el-container>
      </el-container>
    </div>
  </div>
</template>





<script>
export default {
  name: 'Profile',
  data: function(){
    return{


      backgroundDiv: {
        backgroundImage: 'url(' + require('../../static/images/cool-background.png') + ')',
        backgroundRepeat: 'no-repeat',
        backgroundSize: "cover",

      },
      info: this.$route.query.Infos, //传递过来的参数
      keyword: "",
      theme: "不限",
      name: "",
      photo: "",
      title: "",
      mechanism: "",
      papers: [],
      field: [],
      influenced:[],
      influenced_by:[],
      labList:[]
      /*
      influenced: [[100,"爸爸"],[200,"妈妈"]],
      influenced_by: [[100,"小明"],[200,"小红"]],
      labList:[
      {"value":100,"name":"爸爸"},
      {"value":200,"name":"妈妈"}
              ],
      */


      /* keyword:'',
       theme: "不限",
      name: "小乐",
      photo: "../../static/images/19100122420C335-0-lp.jpg",
      title: "班主任",
      mechanism: "家里蹲大学",
      papers: ["今天吃什么","今天喝什么"],
      field: "食堂专家",
      influenced: [[100,"爸爸"],[200,"妈妈"]],
      influenced_by: [[100,"小明"],[200,"小红"]],
      labList:[
      {"value":100,"name":"爸爸"},
      {"value":200,"name":"妈妈"}
              ],
      */


    }
  },
  /*监听搜索栏
  watch: {
        keyword: function(val, oldVal) {
          console.log("new: %s, old: %s", val, oldVal);
          this.getsuggests();
        },
      },
  */
  //方法集
  methods:{
    //返回首页
    returnIndexPage() {
      this.$router.push({ path: "/" });
    },
    //返回搜索列表页
    returnSearchPage() {
      if (this.keyword === "" || this.keyword === undefined || this.keyword === null) {
        this.$message("请输入搜索关键字");
        return;
      }

      this.$router.push({
        path: "/search",
        query: {
          keyword: this.keyword,
          theme: this.theme,
        },
      });
    },
    myEcharts(){
      // 基于准备好的dom，初始化echarts实例
      var myChart = this.$echarts.init(document.getElementById('main'));

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption({
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: []
          }
        ]
      });

      myChart.setOption({
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data:this.influenced
          }
        ]
      })


    },


    myEcharts2(){
      // 基于准备好的dom，初始化echarts实例
      var myChart2 = this.$echarts.init(document.getElementById('main2'));

      // 使用刚指定的配置项和数据显示图表。
      myChart2.setOption({
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: []
          }
        ]
      });
      // this.influenced_by=info.influenced_by;
      // console.log(influenced_by);
      myChart2.setOption({
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data:this.influenced_by
          }
        ]
      })




    }

  },



  mounted: function () {


    console.log("传过来的参数" + this.info); //需要触发的函数
    this.name = this.info.name;//姓名
    this.photo = this.info.photo;//照片
    this.title = this.info.title;//职称
    this.mechanism = this.info.mechanism;//所属机构
    this.papers = this.info.papers;//论文名称列表
    this.field = this.info.field;//研究领域
    this.influenced = this.info.influenced;//影响了该学者的人名
    this.influenced_by = this.info.influenced_by;//被该学者影响的人名
    //  console.log(influenced_by);
    this.myEcharts();
    this.myEcharts2();


  },
};
</script>


<style>


* {
  margin: 0;
  padding: 0;
  list-style: none;
}

.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
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
  margin-bottom: 20px;
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
.post-block {
  text-align: center;
  border-bottom: 1px solid #d2d6de;
  padding-bottom: 13px;
}
.title {
  font-size: 25px;
  text-align: center;
  font-weight: bold;

}
.eee{
  display: inline-block;
  background: no-repeat center center;
  background-size:150px 150px;


}
.eee1{
  width:170px ;
  height:170px;
  background: repeat center;


}
.eee2{
  display: inline-block;




}
.text1 {

  line-height: 45px;
  font-size:20px;
  color:#5ad099;
  font-family: 黑体-简;
}
.tableTitle {
  position: relative;
  margin: 0 auto;
  width: 600px;
  height: 1px;
  background-color: #d4d4d4;
  text-align: center;
  font-size: 16px;
  color: rgba(101, 101, 101, 1);
}
.midText {
  position: absolute;
  left: 50%;
  background-color: #ffffff;
  padding: 0 15px;
  transform: translateX(-50%) translateY(-50%);
}
.middle {
  height: 445px;
  width: 300px;
  background: no-repeat center top;
  background-size: contain;
}

</style>
