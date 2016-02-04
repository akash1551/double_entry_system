new Vue ({
	el: '#accounting',

	data: {
		date: '',
		tranType: 'C',
		credit: '',
		debit: '',
		tranList: [],
		inputTabs: false
	},

	filters: {
		tranTypeFilter: function(val){
			if(val == 'c' || val == 'C'){
				this.inputTabs = false;
				this.tranType = 'C';
				return 'C';
			}else if(val =='d' || val =='D'){
				this.inputTabs = true;
				this.tranType = 'D';
				return 'D';
			}else{
				this.inputTabs = false;
				this.tranType = 'C';
				return 'C';
			}
		}
	},

	methods: {
		addEntry: function(){
			if(this.credit != '' || this.debit != ''){
				this.tranList.push({tranType: this.tranType, credit: this.credit, debit: this.debit});
				this.tranType = '';
				this.credit = '';
				this.debit = '';
			}
		},

		removeEntry: function(entry){
			this.tranList.$remove(entry);
		}
	}
});
