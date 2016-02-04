var loginApp = angular.module('loginApp', ['loginApp.service', 'ui.router'])
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

loginApp.controller('loginController', function($scope, networkCall){
	console.log('loginController is loaded');

	$scope.login = function(){
		var dataPromis = networkCall.loginRequest();
		dataPromis.then(function(result){
			console.log(result);
		});
	};


});

loginApp.controller('signUpController', function($scope, networkCall){
	console.log('signUpController is loaded');

	$scope.signUp = function(){
		var dataPromis = networkCall.signUpRequest();
		dataPromis.then(function(result){
			console.log(result);
		});
	};
});
