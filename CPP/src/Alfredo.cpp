#include "Alfredo.h"

namespace pastas {
	Alfredo::Alfredo(const string &addOn)
	{
		:_addOn(addOn), _cheese("Asiago")
	}
	
	string Alfredo::getAddOn const {
		return _addOn;
	}
	
	void Alfredo::setAddOn(const string &value) {
		if(_addOn != value) {
			_addOn = value;
			updateDish();
		}
	}
	
	void Alfredo::updateDish(){
		_dish = _addOn.append(" Alfredo");
	}
	
	string Spagetti::getDish() const {
		return _dish;
	}
}