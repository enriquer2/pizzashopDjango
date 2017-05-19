import { App } from './module';

config.$inject = ["$stateProvider", "$urlRouterProvider", "$httpProvider"];
export function config(stateProvider, urlRouterProvider, httpProvider) {
    urlRouterProvider.otherwise('/pizzas');
    stateProvider
        .state('app', {
            url: '/',
            component: 'ilApp'
        })
        .state('pizzalist', {
            parent: 'app',
            url: 'pizzas',
            component: 'ilPizzaList'
        })
        .state('pizzas', {
            parent: 'app',
            url: 'pizzas/:id',
            component: 'ilPizza'
        })
        .state('addpizza', {
            parent: 'app',
            url: 'pizzas/add',
            component: 'ilAddPizza'
        });
}

App.config(config);  