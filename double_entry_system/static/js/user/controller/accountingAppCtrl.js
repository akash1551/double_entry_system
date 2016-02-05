angular.module('userApp.controllers')
.controller('accountingAppController', function($scope, $timeout, networkService, Notification){
	console.log('accountingAppController is loaded');

	$scope.date = null;
	var change = false;

	$scope.accountList = [];
	$scope.account = {};

	$scope.transactionModeList = [];
	$scope.transactionMode = {};

	$scope.tranList = [];
	$scope.tranType = 'C';
	$scope.inputTabs = false;
	$scope.credit = null;
	$scope.debit = null;
	$scope.description = '';

	$scope.init = function(){
		getAccountList();
		getTransactionModeList();
		$('#tranType').focus();
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
		// if(tranTypeValidation(val)){
			if(val == 'c' || val == 'C'){
				$scope.inputTabs = false;
				return 'C';
			}else if(val == 'd' || val == 'D'){
				$scope.inputTabs = true;
				return 'D';
			}else{
				//
			}
		// }else{
		// 	Notification.error({message: "Sorry you can't add random entries"});
		// }
	};

	var tranTypeValidation = function(val){
		// console.log('In tranTypeValidation func');
		if($scope.tranList.length == 0){
			console.log('In tranTypeValidation func first length 0');
			return true;
		}

		if(!change && $scope.tranList.length != 0){
			console.log($scope.tranList.length);
			if($scope.tranList[$scope.tranList.length-1].is_debit == val ){
			console.log('In tranTypeValidation func mid true');
				return true;
			}else{
				console.log('In tranTypeValidation func mid change true');
				change = true;
				return true;
			}
		}

		if(change && $scope.tranList[$scope.tranList.length-1].is_debit == val){
			return true;
			console.log('In tranTypeValidation func last true');
		}else{
			console.log('In tranTypeValidation func last false');
			return false;
		}

	};

	$scope.addEntry = function(){
		if(tranTypeValidation($scope.tranType)){
			if($scope.tranType == 'C' && $scope.credit != null){
				$scope.tranList.push({is_debit: $scope.tranType, amount: $scope.credit, account: $scope.account});
				$scope.credit = null;
			}else if($scope.tranType == 'D' && $scope.debit != null){
				$scope.tranList.push({is_debit: $scope.tranType, amount: $scope.debit, account: $scope.account});
				$scope.debit = null;
			}
			$('#tranType').focus();
			console.log($scope.tranList);
		}else{
			Notification.error({message: "Sorry you can't add random entries"});
		}
	};

	$scope.removeEntry = function(index){
		$scope.tranList.splice(index, 1);
	};

	$scope.saveTransactionEntry = function(){
		var obj = {
			Acc_list: $scope.tranList,
			transaction_date: $scope.date,
			description: $scope.description,
			transactiontype: $scope.transactionMode.id
		};
		var dataPromis = networkService.saveTransactionEntryRequest(obj);
		dataPromis.then(function(result){
			console.log(result);
		});
	};
});
