angular.module('userApp.services', [])
.factory('networkService', function($http){

	var getAccountListRequest = function(){
		return $http.get('/show_account_names/').then(function(result){
			return result.data;
		});
	};


	return {
		getAccountListRequest : getAccountListRequest
	};

});
