import serve from 'rollup-plugin-serve';
import livereload from 'rollup-plugin-livereload';
import config from './rollup.config.js';

config.plugins.pop(); //remove uglify
config.plugins.unshift(
    serve({
        open: true,
        contentBase: ['.', 'static/templates/pizzashop'],
        port: 8080
    }),
    livereload({
        watch: 'static/dist',
        delay: 5000
    })
);

export default config;