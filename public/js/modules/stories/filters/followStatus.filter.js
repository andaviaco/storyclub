'use strict';

angular.module('stories')
    .filter('followStatus', followStatus);

followStatus.$inject = [];

function followStatus() {
    return function(status) {
        if (status) {
            return 'Unfollow';
        }

        return 'Follow';
    }
}