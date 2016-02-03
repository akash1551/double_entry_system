new Vue ({

	el: '#myAccMaster',

	data: {
		message: 'hellllo world'
	},

	ready: function() {
		this.$http.get('/list_of_accounting_years/').then(function (response){
			console.log(response.data);

		}, function (response){
			console.log(response.data);
		});
	},

});
