'use strict';

angular.module(
    AppConfiguration.app_module_name,
    AppConfiguration.app_module_dependencies);

angular.module(AppConfiguration.app_module_name)
    .config(config)
    .run(run);

config.$inject = ['$locationProvider', '$resourceProvider'];
run.$inject = ['$http'];

function config($locationProvider, $resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}

function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
}