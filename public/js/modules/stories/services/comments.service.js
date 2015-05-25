'use strict';

angular.module('stories')
    .factory('CommentsService', CommentsService);

CommentsService.$inject = ['$resource', '$http']

function CommentsService($resource, $http) {

    var res = $resource('/api/comments/:id/', {
        id: '@id'
    }, {
        update: {
            method: 'PUT'
        }
    });

    return res;
}