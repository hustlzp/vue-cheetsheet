<template>
  <div>
    <h1>登录</h1>

    <el-dialog title="提示" v-model="showDialog" size="tiny">
      <span>用户名或密码错误</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="showDialog = false">确 定</el-button>
      </span>
    </el-dialog>

    <el-form ref="form" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="username"></el-input>
      </el-form-item>

      <el-form-item label="密码">
        <el-input v-model="password" type="password"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmit">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import AV from 'leancloud-storage'
  import router from '../router'

  export default {
    name: 'SignIn',
    created() {

    },
    data() {
      return {
        username: "",
        password: "",
        showDialog: false
      }
    },
    methods: {
      onSubmit() {
        AV.User.logIn(this.username, this.password).then((loginedUser) => {
          if (loginedUser.get('isAdmin')) {
            router.push('/')
          } else {
            AV.User.logOut()
            this.showDialog = true
          }
        }, (error) => {
          this.showDialog = true
        })
      }
    },
    components: {
    }
  }

</script>

<style scoped>
  form {
    width: 600px;
  }
</style>