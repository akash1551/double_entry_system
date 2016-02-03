new Vue ({

	el: '#myAccMaster',

	data: {
		accYearsList: []
	},

	ready: function() {
		this.$http.get('/list_of_accounting_years/').then(function (response){
			console.log(response.data);
			if(!response.data.status){
				console.log('Error');
			}else{
				this.accYearsList = response.data.AccYearsList;
			}
		}, function (response){
			console.log(response.data);
		});
	},

});
