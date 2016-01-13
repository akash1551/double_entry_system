angular.module('mudraApp.controllers',['ui-notification'])
.controller('mudraAppCtrl', function($scope, $timeout, $http, $window, Notification){
	console.log("mudraAppCtrl loaded");

 	// register user

 		$scope.newUser = {
		firstName : null,
		lastName : null,
		userName : null,
		password : null,
		confirmPassword : null,
		addressLine1 : null,
		addressLine2 : null,
		city : null,
		state : null,
		pincode : null,
		country : null,
		mobileNo0 : null,
		mobileNo1 : null,
		email : null
	};


	function validateNumber(no){
		var regex = /^(\+91[\-\s]?)?[0]?[1789]\d{9}$/;
		return regex.test(no);
	}

	function validatePin(pin){
		var checkPinCode = /(^\d{6}$)/;
		return checkPinCode.test(pin);
	}

	function validateEmail(email) {
		var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
		return re.test(email);
	}


	$scope.signUp = function(){
		console.log($scope.newUser);
		if($scope.newUser.firstName != null &&
			$scope.newUser.lastName != null &&
			$scope.newUser.userName != null &&
			$scope.newUser.password != null &&
			$scope.newUser.confirmPassword != null &&
			$scope.newUser.addressLine1 != null &&
			$scope.newUser.city != null &&
			$scope.newUser.state != null &&
			$scope.newUser.pincode != null &&
			$scope.newUser.country != null &&
			$scope.newUser.mobileNo0 != null &&
			$scope.newUser.email != null &&
			validateNumber($scope.newUser.mobileNo0) &&
			validatePin($scope.newUser.pincode) &&
			validateEmail($scope.newUser.email)){

			$http.post('/register_new_user/', {newUser: $scope.newUser}).
			success(function(data, status, headers, config) {
				console.log(data);
				if(data.status){
					Notification.success({message: data.validation});
				}else{
					Notification.error({message: data.validation});
				}
				// if(!data.status){
				// 	console.log('error');
				// }else{
				// 	$window.localStorage.setItem('token', data.token);
				// 	$window.location.href = data.redirect_url;
				// }
			}).error(function(data, status, headers, config) {
				console.error(data);
			});
		}else{
			console.log('please fill all details');
		}

	};

	// function to submit the form after all validation has occurred            
        $scope.submitForm = function() {
        	$scope.userForm="";
            // check to make sure the form is completely valid
            if ($scope.userForm.$valid) {
               console.log("form validated");
            }

        };
	 
	$scope.userName = null;
	$scope.password = null;

	$scope.login = function(userName, password){
		$http.post('/user_login/', {username: userName, password: password}).
		success(function(data, status, headers, config) {
			console.log(data);
			if(!data.status){
				console.log('error');
			}else{
				$window.localStorage.setItem('token', data.token);
				if(data.redirect_url != undefined){
					$window.location.href = data.redirect_url;
				}else{
					console.log('You does not have ui register device');
				}
			}
		}).error(function(data, status, headers, config) {
			console.error(data);
		});
	};


});