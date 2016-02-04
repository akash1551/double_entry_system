angular.module('loginApp.service', [])
.factory('networkCall', function($http){


	var loginRequest = function(name, password){
		return $http.post('/user_login/', {username: name, password: password}).then(function(result){
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
