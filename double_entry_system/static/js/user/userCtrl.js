angular.module('userApp.controllers', [])
.controller('userCtrl', function($scope, $timeout, networkService, Notification){
	console.log('userCtrl is loaded');

	$scope.$on('$stateChangeSuccess', function(e, toState, toParams, fromState, fromParams) {
		setTimeout(function(){ getBodyHeight(); }, 200);
	});

	var getBodyHeight = function(){
		var height = $('#page-content-wrapper').height();
		$('#sidebar-wrapper').height(height+60);
	};

	$scope.userDetails = '';
	$scope.years = [];
	$scope.selectedYear = null;
	$scope.nextYear = 'Select';
	$scope.newGroup = '';

	$scope.init = function(){
		getUserInfo();
	};
	$timeout($scope.init);

	var getUserInfo = function(){
		var dataPromis = networkService.getUserInfoRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.userDetails = result.User;
			}
		});
	};

	var createYearList = function(){
		var max = new Date().getFullYear(),
		min = max - 10;
		console.log(min);
		console.log(max);
		for(var i = min; i<=max; i++){
			$scope.years.push(i);
		}
		console.log($scope.years);
	};

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

	$scope.openYearModal = function(){
		createYearList();
		$('#addYearModal').modal('show');
	};

	$scope.addNewYear = function(key){
		if($scope.selectedYear != null && key){
			var dataPromis = networkService.addNewYearRequest($scope.selectedYear);
			dataPromis.then(function(result){
				console.log(result);
				if(!result.status){
					Notification.error({message: result.validation});
				}else{
					Notification.success(result.validation);
					window.location.href = result.redirecturl;
				}
			});
		}
		$scope.selectedYear = null;
		$scope.nextYear = 'Select';
		$('#addYearModal').modal('hide');
	};

})

.controller('dashboardController', function($scope){
	console.log('dashboardController is loaded');
});
