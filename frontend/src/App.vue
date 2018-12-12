<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  mounted () {
    fetch('csrf_get/', {
      credentials: 'include'
    })
      .then((resp) => {
        let cookie = this.getCookie('csrftoken')
        fetch('accounts/login/', {
          method: 'POST',
          body: JSON.stringify({ username: 'mek', password: 'jsems4ti' }),
          credentials: 'include',
          headers: {
            'X-CSRFToken': cookie,
            'Content-Type': 'application/json; charset=utf-8'
          }
        })
      })
  },
  methods: {
    getCookie (cname) {
      var name = cname + '='
      var decodedCookie = decodeURIComponent(document.cookie)
      var ca = decodedCookie.split(';')
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i]
        while (c.charAt(0) === ' ') {
          c = c.substring(1)
        }
        if (c.indexOf(name) === 0) {
          return c.substring(name.length, c.length)
        }
      }
      return ''
    }
  }
}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
* {
  box-sizing: border-box;
}
.rack-item {
  display: inline-block;
}
</style>
