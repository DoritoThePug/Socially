const fs = require('fs');
const nodePolyfill = require('node-polyfill-webpack-plugin');


module.exports = {
  devServer: {
    https: {
      key: fs.readFileSync('./certs/key.pem'),
      cert: fs.readFileSync('./certs/cert.pem'),
      ca: fs.readFileSync('./certs/cert.pem'),
      passphrase: "Jadenjin904119"
    }
  },
  configureWebpack: {
    resolve: {
      fallback: {
        fs: false
      }
    },
    plugins: [
      new nodePolyfill()
    ]
  }
};


