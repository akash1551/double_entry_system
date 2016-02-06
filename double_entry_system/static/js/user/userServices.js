angular.module('userApp.services', [])
.factory('networkService', function($http){

	// accountingApp
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
	// accountingApp end

	// index

	var logoutRequest = function(data){
		return $http.post('/logout/', {data: data}).then(function(result){
			return result.data;
		});
	};

	// index end

	// myAccMaster

	var getYearListRequest = function(data){
		return $http.get('/list_of_accounting_years/').then(function(result){
			return result.data;
		});
	};

	// myAccMaster end

	// newUserAccount

	var createNewUserRequest = function(userInfo){
		return $http.post('/create_new_user_account/', {accountInfo : userInfo}).then(function(result){
			return result.data;
		});
	};

	var getGroupListRequest = function(){
		return $http.get('/get_groups_from_db/').then(function(result){
			return result.data;
		});
	};

	var getAccountTypeListRequest = function(){
		return $http.get('/get_accounttype_from_db/').then(function(result){
			return result.data;
		});
	};

	// newUserAccount end



	return {
		getAccountListRequest : getAccountListRequest,
		getTransactionModeListRequest : getTransactionModeListRequest,
		saveTransactionEntryRequest : saveTransactionEntryRequest,
		logoutRequest : logoutRequest,
		getYearListRequest : getYearListRequest,
		createNewUserRequest : createNewUserRequest,
		getGroupListRequest : getGroupListRequest,
		getAccountTypeListRequest : getAccountTypeListRequest
	};

});
