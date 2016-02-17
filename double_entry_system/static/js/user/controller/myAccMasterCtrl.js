angular.module('userApp.controllers')
.controller('myAccMasterController', function($scope, $timeout, networkService, Notification){
	console.log('myAccMasterController is loaded');

	$scope.yearList = [];

	$scope.totalItems = 64;
	$scope.currentPage = 1;
	$scope.maxSize = 5;
	$scope.bigTotalItems = 175;
	$scope.bigCurrentPage = 1;

	$scope.pageChanged = function() {
		// $log.log('Page changed to: ' + $scope.currentPage);
		console.log('pagination');
	};

	$scope.init = function(){
		getYearList();
	};
	$timeout($scope.init);

	var getYearList = function(){
		var dataPromis = networkService.getYearListRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.yearList = result.AccYearsList;
			}
		});
	};




});
