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

	filters: {
		dateFilter: function(val) {
			var date = new Date(val);
			console.log(date);
			return date;
			// return isNaN(number) ? 0 : parseFloat(number.toFixed(2));
		}
	}

});
