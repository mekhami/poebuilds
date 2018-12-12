module.exports = {
  devServer: {
    proxy: {
      '/csrf_get': {
        target: 'http://django:8000',
        changeOrigin: true
      },
      '/accounts': {
        target: 'http://django:8000',
        changeOrigin: true
      },
      '/graphql': {
        target: 'http://django:8000',
        changeOrigin: true
      }
    }
  }
}
