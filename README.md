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

install Element:

```js
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'

Vue.use(ElementUI)
```

init LeanCloud:

```js
import AV from 'leancloud-storage'

AV.init({
  appId: "",
  appKey: ""
})
```

### Docs

* [leancloud doc](https://leancloud.cn/docs/leanstorage-started-js.html)
* [Element doc](http://element.eleme.io/#/zh-CN/component/quickstart)
* [Vue doc](https://vuejs.org/v2/guide/)

### Example project

* [luoying-admin](https://coding.net/u/hustlzp/p/luoying-admin)

## .vue

```vue
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
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
  },
  methods: {
  
  }
}
</script>

<style scoped>
a {
  color: #42b983;
}
</style>
```

## Template Syntax

```html
<span>Message: {{ msg }}</span>

<div v-html="rawHtml"></div>

<div v-bind:id="dynamicId"></div>
<div :id="dynamicId"></div>

{{ message | capitalize }}
<div v-bind:id="rawId | formatId"></div>

<p v-if="seen">Now you see me</p>

<!-- event -->
<a v-on:click="doSomething"></a>
<!-- shorthand -->
<a @click="doSomething"></a>

<li v-for="item in items" :key="item.id">
  {{ item.message }}
</li>

<li v-for="(item, index) in items" :key="item.id">
  {{ parentMessage }} - {{ index }} - {{ item.message }}
</li>

<span v-for="n in 10" :key="n">{{ n }}</span>
```

## Data Change

Array:

```js
push()
pop()
shift()
unshift()
splice()
sort()
reverse()
```

not work:

```js
vm.items[indexOfItem] = newValue

vm.items.length = newLength
```

solutions:

```js
Vue.set(example1.items, indexOfItem, newValue)
example1.items.splice(indexOfItem, 1, newValue)

example1.items.splice(newLength)
```

## Event

```vue
<button v-on:click="greet">Greet</button>
```

```js
var example2 = new Vue({
  el: '#example-2',
  data: {
    name: 'Vue.js'
  },
  // define methods under the `methods` object
  methods: {
    greet: function (event) {
      // `this` inside methods points to the Vue instance
      alert('Hello ' + this.name + '!')
      // `event` is the native DOM event
      if (event) {
        alert(event.target.tagName)
      }
    }
  }
})
```

or:

```html
<div id="example-3">
  <button v-on:click="say('hi')">Say hi</button>
  <button v-on:click="say('what')">Say what</button>
</div>
```

```js
new Vue({
  el: '#example-3',
  methods: {
    say: function (message) {
      alert(message)
    }
  }
})
```

you can pass `$event`:

```html
<button v-on:click="warn('Form cannot be submitted yet.', $event)">Submit</button>
```

```js
methods: {
  warn: function (message, event) {
    // now we have access to the native event
    if (event) event.preventDefault()
    alert(message)
  }
}
```
