## Vue Cheetsheet

### Installation

Use [vue-cli](https://github.com/vuejs/vue-cli) to generate project.

```
npm install -g vue-cli
vue init webpack my-project
cd my-project
npm install
npm install leancloud-storage vue-router element-ui --save
npm run dev
```

### Docs

[leancloud doc](https://leancloud.cn/docs/leanstorage-started-js.html)

[Element doc](http://element.eleme.io/#/zh-CN/component/quickstart)

[Vue doc](https://vuejs.org/v2/guide/)

### Example project

[luoying-admin](https://coding.net/u/hustlzp/p/luoying-admin)

### .vue

```vue
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    
</template>

<script>
export default {
  name: 'home',
  created () {
    // do something
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>
a {
  color: #42b983;
}
</style>
```