class Zabkonator {
	constructor() {
		this.path = "../api/";
		this.request = axios.create({
			baseURL: this.path
		});
	}

	getPromotions(secret, success, fail) {
		let params = {
			secret: secret
		};
		this.request.get("/", {params: params, crossdomain: true})
			.then(response => {
				success(response.data.promotions);
			})
			.catch(error => {
				fail()
			});
	}
}

let app = new Vue({
	el: "#zabka-app",
	data: {
		view: "login",
		secret: "",
		api: null,
		promotions: [],
		promo: {}
	},

	created: function() {
		this.api = new Zabkonator();		
	},

	methods: {
		getPromotions: function() {
			this.api.getPromotions(this.secret,
				promos => {
					this.setPromotions(promos);
					this.view = "promotions"; 
				},
				fail => {
					alert("Złe hasło!")
				});
		},
		setPromotions: function(promos) {
			let hour = ('0'+new Date().getHours()).substr(-2);

			this.promotions = {};
			for (let promo of promos) {
				let thumb = promo.thumbnail;
				let timeout = promo.timeout;
				if (timeout.substr(0, 2) < hour)
					continue; // old promotion
				
				if (!(thumb in this.promotions))
					this.promotions[thumb] = [];

				this.promotions[thumb].push(promo);
			}			
		},

		selectPromotion: function(promo) {
			this.promo = promo;
			this.view = 'promo';
		},

		showBarcode: function(user) {
			let id = "barcode"+user.barcode;
			let code = user.barcode;
			JsBarcode("#"+id, code, {width: 4});
			let svg = document.getElementById(id);
			svg.classList.toggle("visible");
		}
	}
});