angular.module('userApp.controllers')
.controller('myAccMasterController', function($scope, $timeout, networkService, Notification){
	console.log('myAccMasterController is loaded');

	$scope.yearList = [];

	$scope.newGroup = '';

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
