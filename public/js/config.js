'user strict';

var AppConfiguration = (function() {
    // Init module configuration options
    var app_module_name = 'club';
    var app_module_dependencies = ['ngResource', 'ui.router', 'ngSanitize',
        'ui.bootstrap'];

    // Add a new vertical module
    var registerModule = function(module_name, dependencies) {
        // Create angular module
        angular.module(module_name, dependencies || []);

        // Add the module to the AngularJS configuration file
        angular.module(app_module_name).requires.push(module_name);
    };

    return {
        app_module_name: app_module_name,
        app_module_dependencies: app_module_dependencies,
        registerModule: registerModule
    };
})();