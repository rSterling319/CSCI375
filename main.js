//Used .html from class example
class PastaDish {
	
	get dish() {
		return 0;
	}
}

class Spagetti extends PastaDish {
	constructor(addOn = "Plain") {
		super()
		this.addOn = addOn
	}
	
	get dish() {
		if (this.addOn !== "Plain") {
			return "Spagetti with " + this.addOn;
		}
		else{
			return "Spagetti with red sauce"
		}
	}
}

class Alfredo extends PastaDish {
	constructor(addOn="Plain") {
		super();
		this.addOn = addOn;
	}
	get dish() {
		if(this.addOn !== "Plain"){
			return this.addOn + " Alfredo";
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
let food = new Array(
  new Alfredo("Chicken"), 
  new Spagetti("Meatballs"),
  new Spagetti("Parmesean"),
  new Alfredo(),
  new Spagetti());
  
food.forEach(function (item) { console.log(item.dish); });
