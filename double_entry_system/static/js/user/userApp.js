var mudraApp = angular.module('mudraApp', ['mudraApp.controllers','ui.router']);

mudraApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to /state1
  // $urlRouterProvider.otherwise('/');
  //
  // Now set up the states
  $stateProvider

    .state('accList', {
      url: '/accList',
      templateUrl: '/accList'
      // controller: 'mudraAppCtrl'

      // url: '/party/:partyID/:partyLocation',
      //   controller: function($scope, $stateParams) {
      //       // get the id
      //       $scope.id = $stateParams.partyID;

      //       // get the location
      //       $scope.location = $stateParams.partyLocation;   
      //   }
    })
    .state('accDetail', {
      url: '/accDetail',
      templateUrl: '/accDetail'
    })
    .state('registration', {
      url: '/registration',
      templateUrl: '/registration'
    })
    .state('userLogin', {
      url: '/userLogin',
      templateUrl: '/userLogin'
    });

 });