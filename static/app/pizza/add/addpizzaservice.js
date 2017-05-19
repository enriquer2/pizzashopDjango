import { App } from '../../module';

export class AddPizzaService {
    constructor(http) {
        this.http = http;
    }
    savePizza(data, picFile) {
        return this.http({
            method: 'POST',
            headers: { 'Content-Type': undefined },
            url: '/api/v1/pizzas/',
            data: {
                name: data.name,
                ingredients: JSON.stringify(data.ingredients),
                image: picFile,
            },
            transformRequest: function (data, headersGetter) {
                let formData = new FormData();
                angular.forEach(data, function (value, key) {
                    if (key === 'image' && value) {
                        formData.append(key, value, value.name);
                    }
                    else formData.append(key, value);
                });
                return formData;
            }
        });
    }
    getIngridients() {
        return this.http.get(
            '/api/v1/ingredients'
        );
    }
}

AddPizzaService.$inject = ['$http'];
App.service('addPizzaService', AddPizzaService);