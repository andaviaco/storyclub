'use strict';

angular.module('club').config(routes);

routes.$inject = ['$stateProvider', '$urlRouterProvider'];

function routes($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('app', {
            url: '/',
            templateUrl: 'public/templates/core/main.html'
        });



}