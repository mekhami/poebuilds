<template>
  <div id="app">
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link to="/" class="hero-link">Path of Guides</router-link>
        <router-link class="navbar-item is-tab" to="/guides/builder">
          <div class="link-card">
            <span class="has-text-weight-bold">Create Guide</span>
            <span class="subtext">The Guide Builder</span>
          </div>
        </router-link>
        <router-link class="navbar-item is-tab" to="/guides">
          <div class="link-card">
            <span class="has-text-weight-bold">Browse Guides</span>
            <span class="subtext">PoE Character Guides</span>
          </div>
        </router-link>
        <a @click="navMenuOpened = !navMenuOpened" role="button" class="navbar-burger" aria-label="menu" aria-expanded="false">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" :class="{ 'is-active': navMenuOpened }">
        <div class="navbar-start">
          <router-link class="navbar-item is-tab" to="/stats">
            <div class="link-card">
              <span class="has-text-weight-bold">Build Stats</span>
              <span class="subtext">Explore the Meta</span>
            </div>
          </router-link>
          <router-link class="navbar-item is-tab" to="/search">
            <div class="link-card">
              <span class="has-text-weight-bold"><i class="material-icons">search</i> Search</span>
              <span class="subtext">Find a Guide</span>
            </div>
          </router-link>
        </div>
        <div class="navbar-end">

        </div>
      </div>
    </nav>
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      navMenuOpened: false
    }
  },
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
@import "./assets/scss/_variables.scss";
a {
  text-decoration: none;
  color: white;
  &:hover, &:active {
    color: $primary-red;
  }
}
html {
  height: 100%;
}
body {
  height: 100%;
  background-color: $black;
  margin: 0;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
}
.link-card {
  i {
    font-size: 20px;
    position: relative;
    top: 5px;
    left: 4px;
  }
  text-align: center;
  display: inline-block;
  padding: 20;
  &:hover {
    background-color: $primary-red;
  }
  span {
    display: block;
    &.subtext {
      color: #e5e5e5;
      font-size: 14px;
      font-weight: normal;
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
