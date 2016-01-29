new Vue ({
	el: '#registration',

	data: {
		userInfo: {
			userName: '',
			password: '',
			confirmPassword: '',
			firstName: '',
			lastName: '',
			addressLine1: '',
			addressLine2: '',
			city: '',
			state: '',
			pincode: '',
			country: '',
			mobileNo0: '',
			mobileNo1: '',
			email: ''
		}
	},

	methods: {
		submitRegistration: function(){
			console.log(this.userInfo);
			// this.$http.post('/register_new_user/', {this.userInfo}).then(function(response){
			// 	console.log(response);
			// }, function(response){
			// 	console.log(response);
			// });
			this.$http.post('/register_new_user/', {userInfo: this.userInfo}).then(function (response) {
				console.log(response);
			}, function (response) {
				console.log(response);
			});
		}
	}
});
