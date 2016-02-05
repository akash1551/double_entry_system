angular.module('userApp.services', [])
.factory('networkService', function($http){

	var getAccountListRequest = function(){
		return $http.get('/show_account_names/').then(function(result){
			return result.data;
		});
	};

	var getTransactionModeListRequest = function(){
		return $http.get('/get_transactiontype_from_db/').then(function(result){
			return result.data;
		});
	};

	var saveTransactionEntryRequest = function(data){
		return $http.post('/transaction_for_account/', {data: data}).then(function(result){
			return result.data;
		});
	};


	return {
		getAccountListRequest : getAccountListRequest,
		getTransactionModeListRequest : getTransactionModeListRequest,
		saveTransactionEntryRequest : saveTransactionEntryRequest
	};

});
