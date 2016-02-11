angular.module('userApp.controllers')
.controller('accountController', function($scope, $timeout, $stateParams, networkService, Notification, $state){
	console.log('accountController is loaded');
	console.log($stateParams);

	$scope.accountList = [];

	$scope.init = function(){
		getAccountList();
	};
	$timeout($scope.init);

	var getAccountList = function(){
		var dataPromis = networkService.getAccountListRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.accountList = result.account_obj_list;
			}
		});
	};

	var getTransactionRecord = function(info){
		var dataPromis = networkService.getTransactionRecordRequest(info.id, parseInt($stateParams.date));
		dataPromis.then(function(result){
			console.log(result);
		});
	};

	$scope.redirectTo = function(info){
		if($stateParams.edit == 'true'){
			$state.go('newUserAccount', {'id': info.id});
		}else{
			getTransactionRecord(info);
		}
	};
});
