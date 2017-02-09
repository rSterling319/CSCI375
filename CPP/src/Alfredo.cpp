#include "Alfredo.h"

namespace pastas {
	Alfredo::Alfredo(const std::string &addOn)
		:_addOn(addOn),_dish("Alfredo"), _cheese("Asiago")
	{
	}
	
	std::string Alfredo::getAddOn() const {
		return _addOn;
	}
	
	void Alfredo::setAddOn(const std::string &value) {
		if(_addOn != value) {
			_addOn = value;
			updateDish();
		}
	}
	
	void Alfredo::updateDish(){
		_dish = _addOn.append(" Alfredo");
	}
	
	std::string Alfredo::getDish() const {
		return _dish;
	}
}