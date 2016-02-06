angular.module('userApp.controllers')
.controller('newUserAccountController', function($scope, $timeout, networkService, Notification){
	console.log('newUserAccountController is loaded');

	$scope.userInfo = {
		accountName : '',
		alias : '',
		group : '',
		firstName : '',
		lastName : '',
		addressLine1 : '',
		addressLine2 : '',
		city : '',
		state : '',
		country : '',
		pincode : '',
		email : '',
		mobileNo0 : '',
		mobileNo1 : '',
		openingBalance : '',
		accountType : '',
		startDate : '',
		endDate : '',
		duration : ''
	};

	$scope.accountTypeList = [];
	$scope.accountGroupList = [];

	$scope.init = function(){
		getGroupList();
		getAccountTypeList();
	};
	$timeout($scope.init);

	var getGroupList = function(){
		var dataPromis = networkService.getGroupListRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.accountGroupList = result.accGroupList;
			}
		});
	};

	var getAccountTypeList = function(){
		var dataPromis = networkService.getAccountTypeListRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.accountTypeList = result.accTypeList;
			}
		});
	};

	$scope.createNewUser = function(){
		var dataPromis = networkService.createNewUserRequest();
		dataPromis.then(function(result){
			console.log(result);
		});
	};
});
