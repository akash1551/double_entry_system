new Vue ({
	el: '#newUserAccount',

	data: {
		newUser: {
			userName: '',
			alias: '',
			firstName: '',
			lastName: '',
			addressLine1: '',
			addressLine2: '',
			city: '',
			state: '',
			country: '',
			pincode: '',
			email: '',
			mobileNo0: '',
			mobileNo1: '',
			openingBalance: '',
			groupName: ''
		}
	},

	methods: {
		createNewUser: function(){
			console.log(this.newUser);
		}
	}
});


