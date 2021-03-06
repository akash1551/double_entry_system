angular.module('userApp.controllers')
.controller('accountController', function($scope, $timeout, $stateParams, networkService, Notification, $state){
	console.log('accountController is loaded');
	console.log($stateParams);

	$scope.accountList = [];
	$scope.year = null;

	$scope.maxSize = 5;
	$scope.bigTotalItems = 175;
	$scope.bigCurrentPage = 1;
	$scope.entriesPerPage = 5;

	$scope.pageChanged = function() {
		console.log('pagination');
		getAccountList();
	};


	$scope.init = function(){
		getAccountList();
		if($stateParams.date != ''){
			$scope.year = new Date(parseInt($stateParams.date)).getFullYear();
		}
	};
	$timeout($scope.init);

	var getAccountList = function(){
		var dataPromis = networkService.getAccountListRequest($scope.bigCurrentPage, $scope.entriesPerPage);
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.accountList = result.accountList;
			}
		});
	};

	$scope.redirectTo = function(info){
		if($stateParams.edit == 'true'){
			$state.go('newUserAccount', {'id': info.id});
		}else{
			// if($stateParams.date != ''){
				$state.go('transactionDetails', {'id': info.id, 'date': $stateParams.date});
			// }else{
			// 	$state.go('transactionDetails', {'id': info.id, 'date': $stateParams.date});
			// }
		}
	};
});
