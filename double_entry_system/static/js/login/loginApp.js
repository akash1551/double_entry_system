var loginApp = angular.module('loginApp', ['loginApp.service', 'ui.router', 'ui-notification'])
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

	$urlRouterProvider.otherwise('/login');

	$stateProvider
	.state('userLogin', {
        url: '/'
    })
	.state ('login', {
		url: '/login',
		templateUrl: '/userLogin',
		controller: 'loginController'
	})
	.state ('signUp', {
		url: '/signUp',
		templateUrl: '/registration',
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

loginApp.controller('loginController', function($scope, networkCall, Notification){
	console.log('loginController is loaded');

	$scope.userName = '';
	$scope.password = '';

	$scope.login = function(){
		var dataPromis = networkCall.loginRequest($scope.userName, $scope.password);
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				// Notification.success(result.validation);
				window.location.href = result.redirecturl;
			}
		});
	};


});

loginApp.controller('signUpController', function($scope, networkCall, Notification){
	console.log('signUpController is loaded');

		$scope.userInfo = {
			userName : '',
			password : '',
			confirmPassword : '',
			firstName : '',
			lastName : '',
			addressLine1 : '',
			addressLine2 : '',
			city : '',
			state : '',
			pincode : '',
			country : '',
			mobileNo0 : '',
			mobileNo1 : '',
			email : '',
		};

	function validateMono(number){
		var mob = /^[1-9]{1}[0-9]{9}$/;
		return mob.test(number);
	}

	function validateEmail(email) {
		var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
		return re.test(email);
	}

	function validatePin(pin){
		var pat1=/^\d{6}$/;
		return pat1.test(pin);
	}

	$scope.signUp = function(){
		if($scope.userInfo.mobileNo0 != '' && validateMono($scope.userInfo.mobileNo0) &&
			$scope.userInfo.mobileNo1 != '' && validateMono($scope.userInfo.mobileNo1) &&
			$scope.userInfo.email != '' && validateEmail($scope.userInfo.email) &&
			$scope.userInfo.pincode != '' && validatePin($scope.userInfo.pincode)){

			var dataPromis = networkCall.signUpRequest($scope.userInfo);
			dataPromis.then(function(result){
				console.log(result);
				if(!result.status){
					Notification.error({message: result.validation});
				}else{
					Notification.success(result.validation);
					window.location.href = result.redirecturl;
				}
			});
		}else{
			Notification.error({message: 'Please enter validate information'});
		}
	};


});
