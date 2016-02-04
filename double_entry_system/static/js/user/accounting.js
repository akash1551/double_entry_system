new Vue ({
	el: '#accounting',

	data: {
		date: '',
		tranType: 'C',
		credit: null,
		debit: null,
		tranList: [],
		inputTabs: false
	},

	init: function() {
		$( "#tranType" ).focus();
	},

	filters: {
		tranTypeFilter: function(val){
			if(val == 'c' || val == 'C'){
				this.inputTabs = false;
				this.tranType = 'C';
				return this.tranType;
			}else if(val =='d' || val =='D'){
				this.inputTabs = true;
				this.tranType = 'D';
				return this.tranType;
			}else{
				this.inputTabs = false;
				this.tranType = 'C';
				return this.tranType;
			}
		}
	},

	methods: {
		addEntry: function(){
			if(this.tranType == 'C' && this.credit != null){
				this.tranList.push({is_debit: this.tranType, amount: this.credit});
			}else if(this.tranType == 'D' && this.debit != null){
				this.tranList.push({is_debit: this.tranType, amount: this.debit});
			}
			this.credit = null;
			this.debit = null;
			$( "#credit" ).val('');
			$( "#debit" ).val('');
			$( "#tranType" ).focus();
		},

		removeEntry: function(entry){
			this.tranList.$remove(entry);
		}
	}
});
