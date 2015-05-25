'use strict';

angular.module('stories')
    .controller('StoryController', StoryController);

StoryController.$inject = ['$stateParams', 'StoriesService'];

function StoryController($stateParams, StoriesService) {

    var vm = this;
    var id_story = $stateParams.id;

    vm.today = new Date();
    vm.story = StoriesService.get({id: id_story});

    vm.toggleComments = toggleComments;


    function toggleComments(index) {
        vm.story.segments[index]
            .show_comments = !vm.story.segments[index].show_comments;
    }

    function addSegment(segment) {
        // body...
    }
}