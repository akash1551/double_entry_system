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
})

.controller('dashboardController', function($scope){
	console.log('dashboardController is loaded');
});
