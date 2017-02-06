#pragma once

#include <stdint.h>
#include <iostream>
#include <string>

namespace cheeses {

	class Cheese {
	public: string asiago;
	public: string parmesean;
	public: string mozzerela;
	public: Cheese(string _cheeseType = "none");

	public: virtual void print(std::ostream &out) const;
	};

	std::ostream& operator<< (sted::ostream &out, const Cheese &cheese);
}