const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./app/entry/index.js",
  mode: "development",
  module: {
    rules: [
      {
        test: /\.(js|jsx|tsx|ts)$/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel-loader",
        options: { presets: ["@babel/env"] }
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: 'file-loader',
          },
        ],
      }

    ]
  },
  resolve: { extensions: ["*", ".js", ".jsx", ".ts", ".tsx", ".json", ".png"] },
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
    publicPath: "/dist/",
  },
  devServer: {
    static: path.join(__dirname, "assets/"),
    port: 5050,
  },
  plugins: [new webpack.HotModuleReplacementPlugin()]
};