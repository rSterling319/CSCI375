#pragma once

#include "Cheese.h"

namespace cheeses {
	struct Cheesable {
		virtual Cheese getCheese() const = 0;
		virtual void setCheese(const Cheese &value) = 0;
		virtual ~Cheesable();
	};
}