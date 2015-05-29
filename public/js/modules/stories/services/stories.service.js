'use strict';

angular.module('stories')
    .factory('StoriesService', StoriesService);

StoriesService.$inject = ['$resource', '$http']

function StoriesService($resource, $http) {

    var res = $resource('/api/stories/:id/:action/', {
        id: '@id'
    }, {
        update: {
            method: 'PUT'
        },
        fav: {
            method: 'POST',
            params: {
                action: 'fav'
            }
        },
        follow: {
            method: 'POST',
            params: {
                action: 'follow'
            }
        }
    });

    return res;
}
