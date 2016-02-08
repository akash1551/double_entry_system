angular.module('userApp.controllers')
.controller('accountMenuController', function($scope){
	console.log('accountMenuController is loaded');

})
.controller('accountController', function($scope, $timeout, $stateParams, networkService, Notification, $state){
	console.log('accountController is loaded');
	console.log($stateParams.edit);

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

	$scope.redirectTo = function(info){
		if($stateParams.edit){
			$state.go('newUserAccount', {'id': info.id});
		}
	};
});
