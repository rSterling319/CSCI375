#pragma once

#include "PastaDish.h"
#include "Cheesable.h"

namespace pastas
{
	class Alfredo : public PastaDish, public cheeses::Cheesable {
	private: std::string _addOn;

	private: cheeses::Cheese _cheese;
	public: cheeses::Cheese getCheese() const {return _cheese;}
	public: void setCheese(const cheeses::Cheese &value) {_cheese =value;}

	public: Alfredo(const std::string &addOn);

	public: std::string getAddOn() const;
	public: void setAddOn(const std::string &value);

	public: std::string getDish() const;

	private: void updateDish();

	};
}