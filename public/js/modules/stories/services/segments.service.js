'use strict';

angular.module('stories')
    .factory('SegmentsService', SegmentsService);

SegmentsService.$inject = ['$resource', '$http']

function SegmentsService($resource, $http) {

    var res = $resource('/api/segments/:id/', {
        id: '@id'
    }, {
        update: {
            method: 'PUT'
        }
    });

    return res;
}
