'use strict';

angular.module('stories').config(routes);

routes.$inject = ['$stateProvider', '$urlRouterProvider'];

function routes($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('app.stories', {
            url: 'stories',
            abstract: true,
            template: '<ui-view/>'
        })

        .state('app.stories.main', {
            url: '/index',
            templateUrl: 'public/templates/stories/main_list.html'
        })

        .state('app.stories.form', {
            url: '/new',
            templateUrl: 'public/templates/stories/form.html'
        })

        .state('app.stories.single', {
            url: '/:id',
            controller: 'StoryController',
            controllerAs: 'vm',
            templateUrl: 'public/templates/stories/story.html'
        });
}