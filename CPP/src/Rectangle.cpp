#include "Rectangle.h"

namespace shapes {
	public: Rectangle(const double &width, const double &height)
		: _width(width), _height(height), _area(width*height)//constructor notation, constructed in order they are above -- can be a problem
	{
	}
	
	double Rectangle::getWidth() const{
		return _width;
	}
	void Rectangle::setWidth(const double &value){
		if (_width != value){
			_width = value;
			updateArea();
		}
	}
	
	double Rectangle::getHeight() const{
		return _height;
	}
	void Rectangle::setHeight(const double &value){
		if (_height != value){
			_height = value;
			updateArea();
		}
	}
	
	
	double Rectangle::getArea() const{
		return _area;
	}
	
	void Rectangle::updateArea(){
		_area = _width * _height;
	}
}