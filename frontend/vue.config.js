const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  // devserver: {
  //   proxy: {
  //      "^/api/.*": {
  //       target: "http://localhost:5000/",
  //       changeOrigin: true,
  //       rewrite: (path) => path.replace("/api/", ""),
  //      },
  //   },
  // }
})


