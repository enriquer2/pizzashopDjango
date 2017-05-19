import { App } from '../../module';

pizzaListService.$inject = ['$http']
function pizzaListService($http) {
    return {
        getPizzas: function () {
            return $http.get(
                '/api/v1/pizzas'
            );
        }
    };
}
App.service('pizzaListService', pizzaListService);
