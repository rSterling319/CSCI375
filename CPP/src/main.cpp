#include <iostream>

#include "Shape.h"
#include "Rectangle.h"


int main(int argc, char *argv[]){
	shapes::Shape *shape = new shapes::Shape();
	shapes::Rectangle *rectangle = new shapes::Rectangle(3,5);
	
	std::cout<< "shape area = "<<shape->getArea() <<std::endl;
	std::cout<< "rectangle area= "<< rectangle->getArea() <<std::endl;
	
	delete shape;
	delete rectangle;
	
	return 0;
	
}