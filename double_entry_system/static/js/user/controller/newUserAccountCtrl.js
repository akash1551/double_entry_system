angular.module('userApp.controllers')
.controller('newUserAccountController', function($scope, $timeout, networkService, Notification, $stateParams){
	console.log('newUserAccountController is loaded');

	console.log($stateParams);
	$scope.editMode = null;
	if($stateParams.id == ''){
		$scope.editMode = false;
	}else{
		$scope.editMode = true;
	}


	var clearData = function(){
		$scope.startDate = null;
		$scope.endDate = null;

		$scope.userInfo = {
			account_name : '',
			alias : '',
			group : {},
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
	};

	$scope.init = function(){
		clearData();
		getGroupList();
		getAccountTypeList();
		if($stateParams.id != ''){
			getUserInfoToEdit();
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
		if(!$scope.editMode){
			var dataPromis = networkService.createNewUserRequest($scope.userInfo);
			dataPromis.then(function(result){
				console.log(result);
				if(!result.status){
					Notification.error({message: result.validation});
				}else{
					Notification.success(result.validation);
				}
			});
		}else{
			var dataPromis = networkService.saveEditDetailsRequest($scope.userInfo, $stateParams.id);
			dataPromis.then(function(result){
				console.log(result);
				if(!result.status){
					Notification.error({message: result.validation});
				}else{
					Notification.success(result.validation);
				}
			});
		}
	};

	var getUserInfoToEdit = function(){
		var dataPromis = networkService.getUserInfoToEditRequest($stateParams.id);
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.userInfo.account_name = result.accountInfo.account_name;
				$scope.userInfo.firstName = result.accountInfo.firstName;
				$scope.userInfo.lastName = result.accountInfo.lastName;
				$scope.userInfo.accounttype = result.accountInfo.accounttype;
				$scope.userInfo.addressLine1 = result.accountInfo.addressLine1;
				$scope.userInfo.addressLine2 = result.accountInfo.addressLine2;
				$scope.userInfo.alias = result.accountInfo.alias;
				$scope.userInfo.mobileNo0 = result.accountInfo.mobileNo0;
				$scope.userInfo.mobileNo1 = result.accountInfo.mobileNo1;
				$scope.userInfo.city = result.accountInfo.city;
				$scope.userInfo.country = result.accountInfo.country;
				$scope.userInfo.state = result.accountInfo.state;
				$scope.userInfo.pincode = result.accountInfo.pincode;
				$scope.userInfo.email = result.accountInfo.email;
				$scope.userInfo.group = result.accountInfo.group;
				$scope.userInfo.openingBalance = result.accountInfo.openingBalance;
				$scope.userInfo.start_date = result.accountInfo.start_date;
				$scope.startDate = new Date(parseInt($scope.userInfo.start_date));
				$scope.userInfo.end_date = result.accountInfo.end_date;
				$scope.endDate = new Date(parseInt($scope.userInfo.end_date));
				$scope.userInfo.duration = result.accountInfo.duration;
			}
		});
	};
});
