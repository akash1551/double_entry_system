angular.module('loginApp.service', [])
.factory('networkCall', function($http){


	var loginRequest = function(){
		return $http.post('', {}).then(function(result){
			return result.data;
		});
	};

	var signUpRequest = function(){
		return $http.post('', {}).then(function(result){
			return result.data;
		});
	};

	return {
		loginRequest : loginRequest,
		signUpRequest : signUpRequest
	};
});
