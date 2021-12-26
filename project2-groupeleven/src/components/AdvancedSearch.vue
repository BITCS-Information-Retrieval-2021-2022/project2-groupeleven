<template>
  <div>

      <el-card class="box-card">
         <div slot="header" class="clearfix">
                 <span><b>请输入搜索信息</b></span>    
          </div>

        <el-form ref="form" :model="form" label-width="80px" :rules="rules">
       <table>
                        <tr>
                                  <td><el-form-item label="姓名" style="margin-top: 18px;width:275px" prop="name">
                                           <el-input v-model="form.name"></el-input>
                                          </el-form-item>
                               </td>
                               <td><el-form-item label="机构" style="margin-top: 18px;width:275px" prop="institution">
                                           <el-input v-model="form.institution"></el-input>
                                          </el-form-item>
                              </td>
                       </tr>
          </table>        
          <el-form-item label="研究领域" prop="field">
            <el-input v-model="form.field"></el-input>
          </el-form-item>
           <el-form-item label="论文" prop="paper">
            <el-input v-model="form.paper"></el-input>
          </el-form-item>
          <el-form-item label="逻辑关系" prop="status">
            <el-radio-group v-model="form.status">
              <el-radio label="and"></el-radio>
              <el-radio label="or"></el-radio>
            </el-radio-group>
          </el-form-item>

 

<hr style="height:1px;border:none;border-top:1px solid cornflowerblue;" />
          <el-form-item>
             <div style="text-align:right;margin-top:5px">
            <el-button type="primary"  size="medium" @click="onSubmit('form')">搜索</el-button>&nbsp;&nbsp;&nbsp;
            <el-button @click="reset">重置</el-button>
           </div> 
          </el-form-item>
       
        </el-form>
         

      </el-card>

  </div>
</template>


<script>
export default {
  name: "advancedsearch",
  data() {
    return {
      form: {
        name: "",
        institution: "",
        field: "",
        paper: "",
        status:""
      },
      rules: {
        name: [{ required: true, message: "请输入学者姓名", trigger: "blur" }],
        institution: [{ required: true, message: "请输入学者所属机构", trigger: "blur" }],
        field: [{ required: true, message: "请输入学者研究领域", trigger: "blur" }],
        paper: [{ required: true, message: "请输入学者的论著", trigger: "blur" }],
        status: [{ required: true, message: "请选择逻辑", trigger: "change" }],
      },
    };
  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // alert("submit!");
          this.$router.push({
            path: "/search",
            query: { form: this.form },
          });
        } else {
           alert("输入不合法，请重新输入!");
        }
      });
    },
    reset() {
      this.form.name=""
      this.form.institution=""
      this.form.paper=""
      this.form.field=""
      this.form.status=""
    },
    search() {},
    getList() {
      // addDateRange 方法在 main.js中全局挂载
      listUser(this.addDateRange(this.queryParams, this.dateRange)).then(
        (response) => {
          this.userList = response.rows;
          this.total = response.total;
          // this.loading = false;
        }
      );
    },
    /** 搜索按钮操作 */
    handleQuery() {
      console.log(this.queryParams);
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.dateRange = [];
      this.resetForm("queryForm");
      console.log;
    },
  },
  created() {
    this.getList();
    this.getDicts("sys_normal_disable").then((response) => {
      this.statusOptions = response.data;
    });
  },
  mounted() {},
};
</script>
<style scoped>


.clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

.box-card {
  margin: auto;
  width: 600px;
}
.app-container {
  width: 100%;
  max-width: 1000px;
  margin: auto;
  padding: 0%;
}
</style>
