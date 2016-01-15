angular.module('mudraApp.controllers',[])
.controller('mudraAppCtrl', function($scope, $timeout, $http, $window, Notification, networkCall){
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

// ++++++++++++++++++++++++++++++++++++++++++++++++++++
// +++++++++++   datepicker  ++++++++++++++++++++++++++
// ++++++++++++++++++++++++++++++++++++++++++++++++++++
	$scope.today = function() {
    $scope.dt = new Date();
  };
  $scope.today();

  $scope.clear = function() {
    $scope.dt = null;
  };

  // Disable weekend selection
  $scope.disabled = function(date, mode) {
    return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
  };

  $scope.toggleMin = function() {
    $scope.minDate = $scope.minDate ? null : new Date();
  };

  $scope.toggleMin();
  $scope.maxDate = new Date(2020, 5, 22);

  $scope.open1 = function() {
    $scope.popup1.opened = true;
  };

  $scope.open2 = function() {
    $scope.popup2.opened = true;
  };

  $scope.setDate = function(year, month, day) {
    $scope.dt = new Date(year, month, day);
  };

  $scope.dateOptions = {
    formatYear: 'yy',
    startingDay: 1
  };

  $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
  $scope.format = $scope.formats[0];
  $scope.altInputFormats = ['M!/d!/yyyy'];

  $scope.popup1 = {
    opened: false
  };

  $scope.popup2 = {
    opened: false
  };

  var tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  var afterTomorrow = new Date();
  afterTomorrow.setDate(tomorrow.getDate() + 1);
  $scope.events =
    [
      {
        date: tomorrow,
        status: 'full'
      },
      {
        date: afterTomorrow,
        status: 'partially'
      }
    ];

  $scope.getDayClass = function(date, mode) {
    if (mode === 'day') {
      var dayToCheck = new Date(date).setHours(0,0,0,0);

      for (var i = 0; i < $scope.events.length; i++) {
        var currentDay = new Date($scope.events[i].date).setHours(0,0,0,0);

        if (dayToCheck === currentDay) {
          return $scope.events[i].status;
        }
      }
    }

    return '';
  };

  $scope.addAccYear = function(){
  	var dataPromiss = networkCall.saveNewAccYearRequest($scope.dt.getTime());
  	dataPromiss.then(function(result){
  		console.log("result");
  	});
  };

  //newUserAccount
  $scope.newUserAccount = {};

 $scope.submitUserNewAccForm = function(){
 	$scope.userNewAccForm="";
    // check to make sure the form is completely valid
    if ($scope.userNewAccForm.$valid) {
       console.log("form validated");
    }
       console.log("validated" + $scope.newUserAccount );
};

});