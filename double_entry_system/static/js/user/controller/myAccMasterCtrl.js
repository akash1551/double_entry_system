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

	$scope.addNewGroup = function(key){
		console.log(key);
		if(!key){
			$scope.newGroup = '';
			$('#addGroupModal').modal('hide');
		}else{
			if($scope.newGroup != ''){
				var dataPromis = networkService.addNewGroupRequest($scope.newGroup);
				dataPromis.then(function(result){
					console.log(result);
					if(!result.status){
						Notification.error({message: result.validation});
					}else{
						Notification.success(result.validation);
						$scope.newGroup = '';
					}
				});
				$('#addGroupModal').modal('hide');
			}else{
				Notification.error({message: "Please Add Name"});
			}
		}
	};

});
