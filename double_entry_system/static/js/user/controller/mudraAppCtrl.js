angular.module('mudraApp.controllers',[])
.controller('mudraAppCtrl', function($scope, $timeout, $http, $window){
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
		console.log($scope.ownerInfo);
		if($scope.ownerInfo.firstName != null &&
			$scope.ownerInfo.lastName != null &&
			$scope.ownerInfo.userName != null &&
			$scope.ownerInfo.password != null &&
			$scope.ownerInfo.confirmPassword != null &&
			$scope.ownerInfo.addressLine1 != null &&
			$scope.ownerInfo.city != null &&
			$scope.ownerInfo.state != null &&
			$scope.ownerInfo.pincode != null &&
			$scope.ownerInfo.country != null &&
			$scope.ownerInfo.mobileNo0 != null &&
			$scope.ownerInfo.email != null &&
			validateNumber($scope.ownerInfo.mobileNo0) &&
			validatePin($scope.ownerInfo.pincode) &&
			validateEmail($scope.ownerInfo.email)){

			$http.post('/register_new_user/', {ownerInfo: $scope.ownerInfo}).
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

            // check to make sure the form is completely valid
            if ($scope.userForm.$valid) {

               console.log("form validated");
            }

        };

});