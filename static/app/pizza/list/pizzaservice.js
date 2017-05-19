import { App } from '../../module';

export class PizzaService {
    constructor(http) {
        this.http = http;
    }
    getPizza(id) {
        return this.http.get(
            `/api/v1/pizzas/${id}`
        );
    }
    submitComment(data) {
        console.log(data);
        return this.http.post(
            '/api/v1/comments/',
            data
        );
    }
}

PizzaService.$inject = ['$http'];
App.service('pizzaService', PizzaService);