<template>
  <div id="app">
    <div id="supernav">
      <div class="left-pad">
        <router-link to="/login">Login</router-link> |
        <router-link to="/about"> About</router-link> |
        <router-link to="/about"> Contact</router-link>
      </div>
    </div>
    <div id="nav">
      <div class="hero">
        <router-link to="/" class="hero-link">Path of Guides</router-link>
      </div>
      <div class="links">
        <router-link to="/guides/builder">
          <div class="link-card">
            <span>Create Guide</span>
            <span class="subtext">The Guide Builder</span>
          </div>
        </router-link>
        <router-link to="/guides">
          <div class="link-card">
            <span>Browse Guides</span>
            <span class="subtext">PoE Character Guides</span>
          </div>
        </router-link>
        <router-link to="/stats">
          <div class="link-card">
            <span>Build Stats</span>
            <span class="subtext">Explore the Meta</span>
          </div>
        </router-link>
        <router-link to="/search">
          <div class="link-card">
            <span><i class="material-icons">search</i> Search</span>
            <span class="subtext">Find a Guide</span>
          </div>
        </router-link>
      </div>
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
@import "./assets/scss/_variables.scss";
a {
  text-decoration: none;
  color: white;
  &:hover, &:active {
    color: $primary-red;
  }
}

body {
  font-family: 'Open Sans', sans-serif;
  background-color: $black;
  margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
}
.left-pad {
  margin-left: 18px;
}
#supernav {
  text-align: right;
  color: white;
  padding: 6px 10px;
  background-color: $dark-red;
}
#nav {
  padding: 0 30px;
  .links {
    display: inline-block;
  }
  .hero {
    display: inline-block;
    font-size: 28px;
    font-weight: bold;
  }
  .link-card {
    i {
      font-size: 24px;
      position: relative;
      top: 4px;
      left: 4px;
    }
    text-align: center;
    display: inline-block;
    padding: 28px;
    border-bottom: 3px solid transparent;
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
  background-color: $secondary-red;
  font-size: 24px;
  border-bottom: 14px solid $primary-red;
  a {
    padding-bottom: 22px;
    font-weight: bold;
    color: white;
    &.router-link-exact-active  {
      &:not(.hero-link) {
        border-bottom: 3px solid $primary-red;
      }
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
