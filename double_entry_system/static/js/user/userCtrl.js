angular.module('userApp.controllers', [])
.controller('userCtrl', function($scope, $timeout, networkService, Notification){
	console.log('userCtrl is loaded');

	$scope.$on('$stateChangeSuccess', function(e, toState, toParams, fromState, fromParams) {
		setTimeout(function(){ getBodyHeight(); }, 1000);
	});

	var getBodyHeight = function(){
		var height = $('#page-content-wrapper').height();
		console.log(height);
		$('#sidebar-wrapper').height(height+60);
	};

	$scope.init = function(){
	};
	$timeout($scope.init);

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

	$scope.addNewYear = function(key){

	};

})

.controller('dashboardController', function($scope){
	console.log('dashboardController is loaded');
});
