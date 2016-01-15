angular.module('FrontPageApp.services',[])
.factory('networkCall', function($log,$http) {

	var saveNewAccYear = function(date){
		return $http.post("/add_acc_validity_date/",{start_date:date}).then(function(result){
			return result.data;
		});
	};



	return{
		getNotificationCountRequest : getNotificationCountRequest
	}
});

