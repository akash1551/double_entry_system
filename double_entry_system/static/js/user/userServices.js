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
		return $http.get('/logout/').then(function(result){
			return result.data;
		});
	};

	var addNewYearRequest = function(year){
		return $http.post('/add_acc_validity_date/', {start_year: year}).then(function(result){
			return result.data;
		});
	};

	// index end

	// myAccMaster

	var getYearListRequest = function(){
		return $http.get('/list_of_accounting_years/').then(function(result){
			return result.data;
		});
	};

	var addNewGroupRequest = function(groupName){
		return $http.post('/add_group/', {group_name : groupName}).then(function(result){
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

	var getUserInfoToEditRequest = function(id){
		return $http.post('/get_account_details/', {account_id: id}).then(function(result){
			return result.data;
		});
	};

	var saveEditDetailsRequest = function(userInfo, accountid){
		return $http.post('/save_edit_account/', {accountInfo: userInfo, account_id: accountid}).then(function(result){
			return result.data;
		});
	};

	// newUserAccount end

	// account

	var getTransactionRecordRequest = function(id, date){
		return $http.post('/show_transactions_of_single_account/', {account_id: id, start_date: date}).then(function(result){
			return result.data;
		});
	};

	// account end

	// activities

	var getAllTransactionRecordsRequest = function(){
		return $http.get('/show_all_transactions/').then(function(result){
			return result.data;
		});
	};

	// activities end



	return {
		getAccountListRequest : getAccountListRequest,
		getTransactionModeListRequest : getTransactionModeListRequest,
		saveTransactionEntryRequest : saveTransactionEntryRequest,
		logoutRequest : logoutRequest,
		getYearListRequest : getYearListRequest,
		createNewUserRequest : createNewUserRequest,
		getGroupListRequest : getGroupListRequest,
		getAccountTypeListRequest : getAccountTypeListRequest,
		addNewGroupRequest : addNewGroupRequest,
		getUserInfoToEditRequest : getUserInfoToEditRequest,
		saveEditDetailsRequest : saveEditDetailsRequest,
		addNewYearRequest : addNewYearRequest,
		getTransactionRecordRequest : getTransactionRecordRequest,
		getAllTransactionRecordsRequest : getAllTransactionRecordsRequest
	};

});
