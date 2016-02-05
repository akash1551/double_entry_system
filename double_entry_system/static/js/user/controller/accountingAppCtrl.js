angular.module('userApp.controllers')
.controller('accountingAppController', function($scope, $timeout, networkService){
	console.log('accountingAppController is loaded');

	$scope.date = null;

	$scope.accountList = [];
	$scope.account = {};

	$scope.transactionModeList = [];
	$scope.transactionMode = {};

	$scope.tranList = [];
	$scope.tranType = 'C';
	$scope.inputTabs = false;
	$scope.credit = null;
	$scope.debit = null;

	$scope.init = function(){
		getAccountList();
		getTransactionModeList();
	};
	$timeout($scope.init);

	var getAccountList = function(){
		var dataPromis = networkService.getAccountListRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.accountList = result.account_obj_list;
			}
		});
	};

	var getTransactionModeList = function(){
		var dataPromis = networkService.getTransactionModeListRequest();
		dataPromis.then(function(result){
			console.log(result);
			if(!result.status){
				Notification.error({message: result.validation});
			}else{
				$scope.transactionModeList = result.TransactionTypeList;
			}
		});
	};

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
			$scope.tranList.push({is_debit: $scope.tranType, amount: $scope.credit, account: $scope.account});
			$scope.credit = null;
		}else if($scope.tranType == 'D' && $scope.debit != null){
			$scope.tranList.push({is_debit: $scope.tranType, amount: $scope.debit, account: $scope.account});
			$scope.debit = null;
		}
		console.log($scope.tranList);
	};

	$scope.removeEntry = function(index){
		$scope.tranList.splice(index, 1);
	};
});
