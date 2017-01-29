#pragma once

#include "Shape.h"

namespace shapes
{
	class Rectangle : public Shape //: is basically extends
	{
	private: double _width;
	private: double _height;
	private: double _area;
	
	// double width = 3;
	// double height = 5;
	// Rectangle *rect = new Rectangle(width,height) (how init in main)
	
	//passing with the const strickly for input--so just an adress gets passed down save steps
	public: Rectangle(const double &width, const double &height)
	
	{
	}
	
	public: double getWidth() const;
	public: void setWidth(const double &value);
	
	public: double getHeight() const;
	public: void setHeight(const double &value);
	
	public: double getArea() const;
	
	private: void updateArea();

	};


}