'use strict';

angular.module('stories')
    .controller('StoryController', StoryController);

StoryController.$inject = ['$scope', '$stateParams', 'StoriesService',
    'SegmentsService', 'CommentsService'];

function StoryController($scope, $stateParams, StoriesService, SegmentsService,
    CommentsService) {

    var vm = this;
    var id_story = $stateParams.id;

    vm.today = new Date();
    vm.story = StoriesService.get({id: id_story});

    vm.fav = fav;
    vm.toggleComments = toggleComments;
    vm.addSegment = addSegment;
    vm.addComment = addComment;
    vm.toggleFollow = toggleFollow;


    function toggleComments(index) {
        vm.story.segments.forEach(function(value) {
           value.show_comments = false;
        });

        vm.story.segments[index]
            .show_comments = true;
    }

    function addSegment(segment) {
        var new_segment = new SegmentsService(segment);

        new_segment.id_story = vm.story.id_story;
        new_segment.$save(success, fail);

        function success(response) {
            vm.story.segments.push(response);
            vm.new_segment.text = '';
            $scope.segment_form.text.$setPristine(true);
        }

        function fail(response) {
            console.error(response)
        }
    }

    function addComment(comment, segment) {
        var new_comment = new CommentsService(comment);

        new_comment.id_segment = segment.id_segment;
        new_comment.id_story = vm.story.id_story;
        new_comment.$save(success, fail);

        function success(response) {
            segment.comments.push(response);
            vm.new_comment.text = '';
        }

        function fail(response) {
            console.error(response)
        }
    }

    function fav() {
        StoriesService.fav({id: vm.story.id_story}, success, fail);
        vm.story.is_faved = !vm.story.is_faved;

        function success(response) {
            // body...
        }

        function fail(response) {
            vm.story.is_faved = !vm.story.is_faved;
        }
    }

    function toggleFollow() {
        StoriesService.follow({id: vm.story.id_story}, success, fail);
        vm.story.is_followed = !vm.story.is_followed;

        function success(response) {
            // body...
        }

        function fail(response) {
            vm.story.is_followed = !vm.story.is_followed;
        }
    }
}