var mudraApp = angular.module('mudraApp', ['mudraApp.controllers','ui.router']);

mudraApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to /state1
  // $urlRouterProvider.otherwise('/');
  //
  // Now set up the states
  $stateProvider

    .state('registration', {
      url: '/registration',
      templateUrl: '/registration'
    })
    .state('userLogin', {
      url: '/userLogin',
      templateUrl: '/userLogin'
    })
    .state('menu', {
      url: '/menu',
      templateUrl: '/menu'
    })
    .state('myAcc', {
      url: '/myAcc',
      templateUrl: '/myAcc'
    })
    .state('myAcc.credit', {
      url: '/credit',
      templateUrl: '/credit'
    })
    .state('myAcc.debit', {
      url: '/debit',
      templateUrl: '/debit'
    })
    .state('myAcc.summary', {
      url: '/summary',
      templateUrl: '/summary'
    })
    .state('accounting', {
      url: '/accounting',
      templateUrl: '/accounting'
    })
    .state('newUserAccount', {
      url: '/newUserAccount',
      templateUrl: '/newUserAccount'
    })
    .state('accounting.accountingCredit', {
      url: '/accountingCredit',
      templateUrl: '/accountingCredit'
    })
    .state('accounting.accountingDebit', {
      url: '/accountingDebit',
      templateUrl: '/accountingDebit'
    });

 });