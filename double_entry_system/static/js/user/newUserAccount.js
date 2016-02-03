new Vue ({
	el: '#newUserAccount',

	data: {
			accountName: '',
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
			group: '',
			accountType: '',
			duration: 1,
			startDate: '',
			endDate: '',

			groupList: [],
			accountTypeList: []
	},

	ready: function(){
		this.$http.get('/get_groups_from_db/').then(function (response){
			console.log(response.data);
			if(!response.data.status){
				console.log('error');
			}else{
				this.groupList = response.data.accGroupList;
			}
		}, function (response){
			console.log(response.data);
		});


		this.$http.get('/get_accounttype_from_db/').then(function (response){
			console.log(response.data);
			if(!response.data.status){
				console.log('Error');
			}else{
				this.accountTypeList = response.data.accTypeList;
			}
		}, function (response){
			console.log(response.data);
		});
	},

	methods: {
		createNewUser: function(){
			if(this.startDate != '' && this.endDate != ''){
				var tempStartDate = new Date(this.startDate).getTime();
				var tempEndDate = new Date(this.startDate).getTime();
				this.$http.post('/create_new_user_account/', {
					account_name: this.accountName, alias : this.alias,
					firstName: this.firstName, lastName: this.lastName,
					addressLine1: this.addressLine1, addressLine2: this.addressLine2,
					city: this.city, state: this.state, country: this.country, pincode: this.pincode,
					email: this.email, mobileNo0: this.mobileNo0, mobileNo1: this.mobileNo1,
					group: this.group, openingBalance: this.openingBalance, accounttype: this.accountType,
					duration: this.duration, start_date: this.tempStartDate, end_date: this.tempEndDate

				}).then(function (response){
					console.log(response.data);
				}, function (response){
					console.log(response.data);
				});
			}
		}
	}
});


