angular.module('userApp.controllers')
.controller('newUserAccountController', function($scope, $timeout, networkService, Notification, $stateParams){
	console.log('newUserAccountController is loaded');

	console.log($stateParams);

	$scope.startDate = null;
	$scope.endDate = null;

	$scope.userInfo = {
		account_name : '',
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
		accounttype : '',
		start_date : '',
		end_date : '',
		duration : 1
	};

	$scope.accountTypeList = [];
	$scope.accountGroupList = [];

	$scope.init = function(){
		if($stateParams.id != ''){
			getUserInfoToEdit();
		}else{
			getGroupList();
			getAccountTypeList();
		}
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
		$scope.userInfo.start_date = new Date($scope.startDate).getTime();
		$scope.userInfo.end_date = new Date($scope.endDate).getTime();
		var dataPromis = networkService.createNewUserRequest($scope.userInfo);
		dataPromis.then(function(result){
			console.log(result);
		});
	};

	var getUserInfoToEdit = function(){
		var dataPromis = networkService.getUserInfoToEditRequest();
		dataPromis.then(function(result){
			console.log(result);
		});
	};
});
