const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');

const isDevelopment = process.env.NODE_ENV !== 'production';

module.exports = {
    mode: isDevelopment ? "development": 'production',
    performance: {
        hints: false,
        maxEntrypointSize: 512000,
        maxAssetSize: 512000
    },
    entry: path.join(__dirname, "src", "index.js"),
    output: {
        path:path.resolve(__dirname, "dist"),
        filename: 'bundle.js',
    },
    devtool: isDevelopment ? 'inline-source-map' : 'source-map',
    module: {
        rules: [
        {
            test: /\.?js$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader",
                options: {
                    presets: ['@babel/preset-env', '@babel/preset-react'],
                    plugins: [
                        isDevelopment && require.resolve('react-refresh/babel')
                    ].filter(Boolean)
                }
            }
        },
        {
            test: /\.css$/i,
            use: ["style-loader", "css-loader"],
        },
        {
            test: /\.(png|jp(e*)g|svg|gif)$/,
            use: ['file-loader'],
        },
        {
            test: /\.svg$/,
            use: ['@svgr/webpack'],
        }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
        template: path.join(__dirname, "src", "index.html"),
        }),
        isDevelopment && new ReactRefreshWebpackPlugin()
    ].filter(Boolean),
    devServer: {
        static: {
            directory: path.join(__dirname, 'dist'),
        },
        hot: true, // Enable HMR
        liveReload: true, // Enable live reloading
        allowedHosts: 'all',
        watchFiles: {
            poll: 1000,
        }
    },
    // devServer: {
    //     host: '0.0.0.0',
    //     hot: true,
    //     client: {
    //         webSocketURL: {
    //             port: 443
    //         }
    //     },
    //     allowedHosts: 'all',
    //     watchFiles: {
    //         poll: true
    //     }
    // },
}
