import { App } from './module';

export const resolveUrl = function (URL) {
    return {
        resolve: function (path) {
            return `${URL}/${path}`;
        }
    };
}
resolveUrl.$inject['URL'];
App.factory('resolveUrl', resolveUrl);