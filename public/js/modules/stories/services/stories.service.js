'use strict';

angular.module('stories')
    .factory('StoriesService', StoriesService);

StoriesService.$inject = ['$resource', '$http']

function StoriesService($resource, $http) {

    var res = $resource('/api/stories/:id/', {
        id: '@id'
    }, {
        update: {
            method: 'PUT'
        }
    });

    return res;
}
