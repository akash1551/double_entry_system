var loginApp = angular.module('loginApp', ['ui.router'])
.config(function($stateProvider, $urlRouterProvider){


	$stateProvider
	.state('userLogin', {
        url: '/'
    })
	.state ('login', {
		url: '/login/',
		templateUrl: '/userLogin/',
		controller: 'loginController'
	})
	.state ('signUp', {
		url: '/signUp/',
		templateUrl: '/registration/',
		controller: 'signUpController'
	});
});

loginApp.controller('loginMasterController', function($scope, $state, $timeout){
	console.log('loginMasterController is loaded');

	$scope.init = function(){
		$state.go('login');
	};
	$timeout($scope.init);
});

loginApp.controller('loginController', function($scope){
	console.log('loginController is loaded');
});

loginApp.controller('signUpController', function($scope){
	console.log('signUpController is loaded');
});
