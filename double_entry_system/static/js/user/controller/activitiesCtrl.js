angular.module('userApp.controllers')
.controller('activitiesController', function($scope, $timeout, networkService, Notification){
	console.log('activitiesController is loaded');

	$scope.init = function(){
		getAllTransactionRecords();
	};
	$timeout($scope.init);

	var getAllTransactionRecords = function(){
		var dataPromis = networkService.getAllTransactionRecordsRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.allRecords = result.transactionList;
			}
		});
	};
});
