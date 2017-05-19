import { App } from '../../module';
import html from './addpizza.html';

export const ilAddPizza = {
    controller: 'addPizzaCtrl',
    template: html
};
App.component('ilAddPizza', ilAddPizza)
