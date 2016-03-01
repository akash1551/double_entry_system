angular.module('userApp.controllers')
.controller('activitiesController', function($scope, $timeout, networkService, Notification){
	console.log('activitiesController is loaded');

	$scope.maxSize = 5;
	$scope.bigTotalItems = 175;
	$scope.bigCurrentPage = 1;
	$scope.entriesPerPage = 5;

	$scope.init = function(){
		getAllTransactionRecords();
	};
	$timeout($scope.init);

	var getAllTransactionRecords = function(){
		var dataPromis = networkService.getAllTransactionRecordsRequest($scope.bigCurrentPage, $scope.entriesPerPage);
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.allRecords = result.transactionList;
			}
		});
	};

	$scope.pageChanged = function() {
		console.log('pagination');
		getAllTransactionRecords();
	};

});
