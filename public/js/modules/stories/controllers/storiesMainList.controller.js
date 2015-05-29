'use strict';

angular.module('stories')
    .controller('StoriesMainListController', StoriesMainListController);

StoriesMainListController.$inject = ['StoriesService'];

function StoriesMainListController(StoriesService) {
    var vm = this;

    vm.stories = StoriesService.query();
}