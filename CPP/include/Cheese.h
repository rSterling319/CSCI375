#pragma once

#include <stdint.h>
#include <iostream>
#include <string>

namespace cheeses {

	class Cheese {
	public: std::string asiago;
	public: std::string parmesean;
	public: std::string mozzerela;
	public: Cheese(std::string _cheeseType = "none");

	public: virtual void print(std::ostream &out) const;
	};

	std::ostream& operator<< (std::ostream &out, const Cheese &cheese);
}