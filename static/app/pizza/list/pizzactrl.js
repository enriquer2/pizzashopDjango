import { App } from '../../module';

export class PizzaCtrl {
    constructor(state, pizzaService) {
        this.state = state;
        this.id = state.params && state.params.id;
        this.pizzaService = pizzaService;
        this.name = null;
        this.img = null;
        this.ingredients = null;
        this.comments = null;
        this.comment = {};
        this.config(state);
    }
    config() {
        let _this = this;
        this.pizzaService.getPizza(this.id)
            .then(function (response) {
                let data = response.data;
                _this.name = data.name;
                _this.img = data.image;
                _this.ingredients = data.ingredients;
                _this.comments = data.comments;
            });
    }
    hasIngridients() {
        return this.ingredients && this.ingredients.length > 0;
    }
    submitComment() {
        this.comment.text = this.comment.text || "";
        this.comment.user = Document.userId;
        this.comment.pizza = parseInt(this.id);
        this.pizzaService.submitComment(this.comment);
        this.state.reload();
    }
}
PizzaCtrl.$inject = ['$state', 'pizzaService'];
App.controller('pizzaCtrl', PizzaCtrl);