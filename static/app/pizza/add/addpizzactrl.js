import { App } from '../../module';

export class AddPizzaCtrl {
    constructor(addPizzaService) {
        this.addPizzaService = addPizzaService;
        this.ingredients = null;
        this.pizza = {
            name: null,
            ingredients: [],
            image: null
        }; 
        this.getIngridients();
    }
    savePizza() {
        this.addPizzaService.savePizza(this.pizza, this.picFile);
    }
    getIngridients() {
        let _this = this;
        this.addPizzaService.getIngridients()
            .then(c => _this.ingredients = c.data.results);
         
    }
}
AddPizzaCtrl.$inject = ['addPizzaService'];
App.controller('addPizzaCtrl', AddPizzaCtrl);