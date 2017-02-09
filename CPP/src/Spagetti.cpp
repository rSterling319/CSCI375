#include "Spagetti.h"

namespace pastas {
	Spagetti::Spagetti(const string &addOn)
	
		: _addOn(addon), _cheese("parmesean")
	{
		
	}
	
	std::string Spagetti::getAddOn const {
		return _addOn;
	}
	
	void Spagetti::setAddOn(const std::string &value) {
		if(_addOn != value){
			_addOn = value;
			updateDish();
		}
	}
	
	void Spagetti::updateDish() {
		_dish = "Spagetti with ".append(_addOn);
	}
	
	std::string Spagetti::getDish() const {
		return _dish;
	}
}