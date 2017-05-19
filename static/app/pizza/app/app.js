import { App } from '../../module';

const html =
  `<div layout="column" ng-cloak>
  <section layout="row" flex>

    <md-sidenav
        md-component-id="sidenav"
        class="md-sidenav-left"
        md-component-id="left"
        md-is-locked-open="$mdMedia('gt-md')"
        md-whiteframe="4">

      <md-toolbar class="md-theme-indigo">
        <img src="static/img/logo.png" alt>
        <h1 class="md-toolbar-tools">Pizza Shop</h1>
      </md-toolbar>

      <md-content layout="column" layout-padding>
        <md-button class="md-primary" ui-sref="pizzalist" ng-click="$ctrl.closeSideNav()">
          show pizzas
        </md-button>
        <md-button class="md-primary" ui-sref="addpizza" ng-click="$ctrl.closeSideNav()">
          Add pizza
        </md-button>
       
        <div style="text-align:center;">
        <form action="/logout/" method="post">
          <md-button class="md-primary" type="submit" ng-click="$ctrl.closeSideNav()">
            Logout
          </md-button>
        </form>
        </div>
        
      </md-content>

    </md-sidenav>

    <div layout="column" flex>
    <md-toolbar  layout-align="center center" layout="row" class="site-content-toolbar" ng-show="$ctrl.isSideNavClosed()">
        <img src="static/img/menu.png" class="md-icon-button md-button" ng-click="$ctrl.openSideNav()"></img>
        <h1 class="md-toolbar-tools">Pizza Shop</h1>
    </md-toolbar>
    <md-content flex layout-padding>
      <div ui-view flex></div>
    </md-content>
    </div>
  </section>
</div>`

export const ilApp = {
  template: html,
  controller: 'appCtrl'
}
App.component('ilApp', ilApp);
