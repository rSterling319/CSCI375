#include "Cheese.h"

namespace cheeses {
	Cheese::Cheese(std::string _cheeseType)
		: cheese(_cheeseType)
	{
	}
	
	void Cheese::print(std::ostream &out) const {
		out<< "(" << cheese<<")";
	}
	
	std::ostream& operator<< (std::ostream &out, const Cheese &cheese) {
		cheese.print(out);
		return out;
	}
}