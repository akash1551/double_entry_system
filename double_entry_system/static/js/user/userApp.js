angular.module('userApp', [ 'userApp.controllers', 'userApp.services', 'ui.router', 'ui-notification'])
.config(function($stateProvider, $urlRouterProvider, NotificationProvider){

	NotificationProvider.setOptions({
        delay: 3000,
        startTop: 20,
        startRight: 10,
        verticalSpacing: 20,
        horizontalSpacing: 20,
        positionX: 'right',
        positionY: 'top'
    });

	$urlRouterProvider.otherwise('/dashboard');

	$stateProvider
	.state('userHome', {
        url: '/'
    })
	.state('dashboard', {
		url: '/dashboard',
		templateUrl: '/menu',
		controller: 'dashboardController'
	});

});
