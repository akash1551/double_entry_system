angular.module('loginApp.service', [])
.factory('networkCall', function($http){


	var loginRequest = function(name, password){
		return $http.post('/user_login/', {username: name, password: password}).then(function(result){
			return result.data;
		});
	};

	var signUpRequest = function(userInfo){
		return $http.post('/register_new_user/', {userInfo}).then(function(result){
			return result.data;
		});
	};

	return {
		loginRequest : loginRequest,
		signUpRequest : signUpRequest
	};
});
