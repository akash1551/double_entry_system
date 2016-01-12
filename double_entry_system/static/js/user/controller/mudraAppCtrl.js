angular.module('mudraApp.controllers',[])
.controller('mudraAppCtrl', function($scope){
	console.log("mudraAppCtrl loaded");

 $scope.toggleSidebar = function(){
 	console.log("inside");
		$('.ui.labeled.icon.sidebar')
			.sidebar('toggle');
	};
	$('.ui.dropdown').dropdown();

});