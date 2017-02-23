#include <iostream>
#include "Type.h"

namespace instruments {
	
	Type::Type(classification _instType)
	:instType (_instType)
	{
		std::cout<<"Type()@"<<(void*) this << std::endl;
	}
	
	Type::~Type()
	{
		std::cout << "~Type()@"<< (void*) this << std::endl;
	}

	void Type::print(std::ostream &out) const {
		out<< "("<<instType<<")"<<std::endl;
	}

	std :: ostream& operator << (std::ostream &out, const Type &instType){
		instType.print(out);
		return out;
	}
}