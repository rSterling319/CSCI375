#pragma once

#include "PastaDish.h"
#include "Cheesable.h"

namespace pastas
{
	class Alfredo : public PastaDish, public cheeses::Cheesable {
	private string _addOn;

	private: cheeses::Cheese _cheese;
	public: cheeses::Cheese getCheese() const {return _cheese;}
	public: void setCheese(const cheeses::Cheese &value) {_cheese =value}

	public: Alfredo(const string &addOn);

	public: string getAddOn() const;
	public: void setAddOn(const sring &value);

	public: string getDish() const;

	private: void updateDish();

	};
}