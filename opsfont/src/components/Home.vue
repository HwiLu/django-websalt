<template>
  <div class="home">
    <el-row display="margin-top:10px">
      <el-input
        v-model="input"
        placeholder="请输入操作系统版本"
        style="display:inline-table; width: 30%; float:left"
      ></el-input>
      <el-button type="primary" @click="addOsVersion(),showOs()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
      <el-table :data="osVersionList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template slot-scope="scope">{{ scope.row.pk }}</template>
        </el-table-column>
        <el-table-column prop="os_version" label="版本" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.os_version }}</template>
        </el-table-column>
        <el-table-column prop="os_num" label="版本号" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.os_num }}</template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {
      input: '',
      osVersionList: []
    }
  },
  mounted: function() {
    this.showOs()
  },
  methods: {
    addOsVersion() {
      this.$axios
        .get('http://127.0.0.1:8000/api/add_os?os_version=' + this.input).then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num == 0) {
            this.showOs()
          } else {
            this.$message.error('新增操作系统失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    showOs() {
      this.$axios.get('http://127.0.0.1:8000/api/show_os').then((res) => {
        var ress = res.data
        console.log(res)
        if (ress.error_num == 0) {
          this.osVersionList = ress['list']
        } else {
          this.$message.error('查询操作系统失败')
          console.log(ress['msg'])
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
