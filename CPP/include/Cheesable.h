#pragma once

#include "Cheese.h"

namespace cheeses {
	struct Cheesable {
		virtual Cheese getCheese() const = "none";
		virtual void setCheese(const Cheese &value) ="none";
		virtual ~Cheesable();
	};
}