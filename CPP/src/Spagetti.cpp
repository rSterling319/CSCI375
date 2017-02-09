#include "Spagetti.h"

namespace pastas {
	Spagetti::Spagetti(const std::string &addOn)
		: _addOn(addOn), _dish("Spagetti"), _cheese("parmesean")	
	{
	}
	
	std::string Spagetti::getAddOn() const {
		return _addOn;
	}
	
	void Spagetti::setAddOn(const std::string &value) {
		if(_addOn != value){
			_addOn = value;
			updateDish();
		}
	}
	
	void Spagetti::updateDish() {
		_dish = "Spagetti with " + _addOn;
	}
	
	std::string Spagetti::getDish() const {
		return _dish;
	}
}