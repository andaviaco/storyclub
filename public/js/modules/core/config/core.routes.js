'use strict';

angular.module('core').config(routes);

routes.$inject = ['$stateProvider', '$urlRouterProvider'];

function routes($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('app', {
            url: '/',
            templateUrl: 'public/templates/core/main.html'
        });



}