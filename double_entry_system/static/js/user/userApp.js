angular.module('userApp', [ 'userApp.controllers', 'userApp.services', 'ui.router', 'ui-notification', 'ui.bootstrap'])
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

	$urlRouterProvider.otherwise('/myAccMaster');

	$stateProvider
	.state('userHome', {
		url: '/'
	})
	// .state('dashboard', {
	// 	url: '/dashboard',
	// 	templateUrl: '/menu',
	// 	controller: 'dashboardController'
	// })
	.state('myAccMaster', {
		url: '/myAccMaster',
		templateUrl: '/myAcc',
		controller: 'myAccMasterController'
	})
	.state('accountingApp', {
		url: '/accountingApp',
		templateUrl: '/accounting',
		controller: 'accountingAppController'
	})
	.state('newUserAccount', {
		url: '/newUserAccount/:id',
		templateUrl: '/newUserAccount',
		controller: 'newUserAccountController'
	})
	// .state('accountMenu', {
	// 	url: '/accountMenu',
	// 	templateUrl: '/accountMenu',
	// 	controller: 'accountMenuController'
	// })
	.state('account', {
		url: '/account/:edit/:date',
		templateUrl: '/account',
		controller: 'accountController'
	})
	.state('activities', {
		url: '/activities',
		templateUrl: '/activities',
		controller: 'activitiesController'
	})
	.state('transactionDetails', {
		url: '/transactionDetails/:id/:date',
		templateUrl: '/transactionDetails',
		controller: 'transactionDetailsController'
	});

});
