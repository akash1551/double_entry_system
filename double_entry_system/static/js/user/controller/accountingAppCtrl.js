angular.module('userApp.controllers')
.controller('accountingAppController', function($scope){
	console.log('accountingAppController is loaded');

	$scope.tranList = [];

	$scope.tranTypeFilter = function(val){
		if(val == 'c' || val == 'C'){
			return 'C';
		}else if(val == 'd' || val == 'D'){
			return 'D';
		}else{
			//
		}
	};
});
