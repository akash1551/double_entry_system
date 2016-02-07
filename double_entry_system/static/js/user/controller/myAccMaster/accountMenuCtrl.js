angular.module('userApp.controllers')
.controller('accountMenuController', function($scope){
	console.log('accountMenuController is loaded');

})
.controller('accountController', function($scope, $stateParams){
	console.log('accountController is loaded');
	console.log($stateParams);

});
