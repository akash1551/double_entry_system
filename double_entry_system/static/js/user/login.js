new Vue ({
	el: '#login',

	data: {
		userName: '',
		password: ''
	},

	methods: {
		login: function(e){
			e.preventDefault();
			console.log(this.userName);
			console.log(this.password);

			this.$http.post('/user_login/', {username: this.userName, password: this.password}).then(function (response) {
				console.log(response);
			}, function (response) {
				console.log(response);
			});

		}
	}
});
