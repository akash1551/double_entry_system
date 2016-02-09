angular.module('userApp.controllers', [])
.controller('userCtrl', function($scope, networkService, Notification){
	console.log('userCtrl is loaded');

	$scope.logout = function(){
		var dataPromis = networkService.logoutRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				window.location.href = result.redirecturl;
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
})

.controller('dashboardController', function($scope){
	console.log('dashboardController is loaded');
});
