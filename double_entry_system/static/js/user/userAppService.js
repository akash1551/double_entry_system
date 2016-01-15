angular.module('mudraApp.services',[])
.factory('networkCall', function($log,$http) {

	var saveNewAccYearRequest = function(date){
		return $http.post("/add_acc_validity_date/",{start_date:date}).then(function(result){
			return result.data;
		});
	};



	return{
		saveNewAccYearRequest : saveNewAccYearRequest
	}
});

