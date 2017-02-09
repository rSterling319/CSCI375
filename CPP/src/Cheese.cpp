#include "Cheese.h"

namespace cheeses {
	Cheese::Cheese(std::string _cheeseType)
	:cheese(_cheeseType)
	{
	}
	
	void Color::print(std::ostream &out) const {
		out<< "(" << cheese<<")";
	}
	
	std::ostream& operator<< (std::ostream &out, const Cheese &color) {
		cheese.print(out)
		return out;
	}
}