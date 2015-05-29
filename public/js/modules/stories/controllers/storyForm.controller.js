'use strict';

angular.module('stories')
    .controller('StoryFormController', StoryFormController);

StoryFormController.$inject = ['$state', 'StoriesService'];

function StoryFormController($state, StoriesService) {

    var vm = this;

    vm.save = save;
    vm.story = {};
    vm.story.public = true;

    function save(story) {
        console.debug(story);
        var new_story = new StoriesService(story)

        new_story.$save(success, fail);

        function success(response) {
            $state.go('app.stories.single', {id: response.id_story});
        }

        function fail(response) {
            console.error(response);
        }
    }

}