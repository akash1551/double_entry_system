angular.module('userApp.controllers')
.controller('transactionDetailsController', function($scope, $timeout, $stateParams, networkService, Notification){
	console.log('transactionDetailsController is loaded');


	$scope.init = function(){
		getTransactionRecord();
	};
	$timeout($scope.init);

	var getTransactionRecord = function(){
		var dataPromis = networkService.getTransactionRecordRequest($stateParams.id, parseInt($stateParams.date));
		dataPromis.then(function(result){
			console.log(result);
		});
	};

});
