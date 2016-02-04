angular.module('userApp', [ 'userApp.controllers', 'userApp.services', 'ui-router'])
.config(function($stateProvider, $urlRouterProvider){

	$stateProvider
	.state('dashboard', {
		url: '/dashboard/',
		templateUrl: '/dashboard/',
		controller: 'dashboardController'
	});

});
