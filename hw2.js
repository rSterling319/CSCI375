//Used .html from class example
class PastaDish {
	
	get dish() {
		return 0;
	}
}

class Spagetti extends PastaDish {
	constructor(addOn = "Plain") {
		super()
		this._addOn = addOn
		this._dish = null
	}
	_updateDish(){
		this._dish = "Spagetti with " + this._addOn;
	}
	
	get addOn() {return this._addOn; }
	set addOn(value){
		if (value != this._addOn){
			this._addOn = value;
			this._dish = null;
		}
	}
	
	
	get dish() {
		if (this._addOn !== "Plain") {
			return "Spagetti with " + this._addOn;
		}
		else{
			return "Spagetti with red sauce"
		}
	}
}

class Alfredo extends PastaDish {
	constructor(addOn="Plain") {
		super();
		this._addOn = addOn;
		this._dish = null;
	}
	_updateDish(){
		this._dish = this._addOn +" Alfredo";
	}
	
	get addOn() {return this._addOn; }
	set addOn(value){
		if(value != this._addOn){
			this._addOn = value;
			this._dish =null;
		}
	}
	
	get dish() {
		if(this._addOn !== "Plain"){
			return this._addOn + " Alfredo";
		}
		else{
			return "Classic Alfredo"
		}
	}
}


class Console {
	constructor(id) {
		this.element = document.getElementById(id);
	}
	log(message) {
		let p = document.createElement("p");
		p.innerText = message;
		this.element.appendChild(p);
	}
}

let dinner = new PastaDish();
let console = new Console("console");
console.log("Hello! Tonights menu items are:");
let spag = new Spagetti("Shrimp");
console.log("Spagetti with shrimp added on: " + spag.dish);
spag.addOn = "Chicken";
console.log("Spagettin with shrimp deleted, chicken added: " +spag.dish);
let food = new Array(
  new Alfredo("Chicken"), 
  new Spagetti("Meatballs"),
  new Spagetti("Parmesean"),
  new Alfredo(),
  new Spagetti());
  
food.forEach(function (item) { console.log(item.dish); });
