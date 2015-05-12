'user strict';

var AppConfiguration = (function() {
    var app_module_name = 'club';
    var app_module_dependencies = ['ngResource', 'ui.router', 'ngSanitize',
        'ui.bootstrap'];

    var registerModule = function(module_name, dependencies) {
        angular.module(module_name, dependencies || []);
        angular.module(app_module_name).requires.push(module_name);
    };

    return {
        app_module_name: app_module_name,
        app_module_dependencies: app_module_dependencies,
        registerModule: registerModule
    };
})();