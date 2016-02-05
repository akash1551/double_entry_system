angular.module('userApp.controllers')
.controller('accountingAppController', function($scope){
	console.log('accountingAppController is loaded');

	$scope.date = null;
	$scope.accountList = [];
	$scope.tranList = [];
	$scope.tranType = 'C';
	$scope.inputTabs = false;
	$scope.credit = null;
	$scope.debit = null;


	$scope.tranTypeFilter = function(val){
		if(val == 'c' || val == 'C'){
			$scope.inputTabs = false;
			return 'C';
		}else if(val == 'd' || val == 'D'){
			$scope.inputTabs = true;
			return 'D';
		}else{
			//
		}
	};

	$scope.addEntry = function(){
		if($scope.tranType == 'C' && $scope.credit != null){
			$scope.tranList.push({is_debit: $scope.tranType, amount: $scope.credit});
			$scope.credit = null;
		}else if($scope.tranType == 'D' && $scope.debit != null){
			$scope.tranList.push({is_debit: $scope.tranType, amount: $scope.debit});
			$scope.debit = null;
		}
		console.log($scope.tranList);
	};

	$scope.removeEntry = function(index){
		$scope.tranList.splice(index, 1);
	};
});
