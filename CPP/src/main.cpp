#include <iostream>
#include <vector>

#include "Cheese.h"
#include "Spagetti.h"
#include "Alfredo.h"
#include "PastaDish.h"

using namespace cheeses;
using namespace pastas;

int main(int argc, char *argv[])
{
	
	pastas::PastaDish *pasta = new pastas::PastaDish();
	pastas::Spagetti *spagetti = new pastas::Spagetti("Meatballs");
	
	cheeses::Cheese *parm = new cheeses::Cheese("Parmesean");
	
	std::cout<<"Parmesean = " <<*parm <<std::endl;
	
	std::vector <pastas::PastaDish*> pastaVec;
	pastaVec.push_back(new pastas::Spagetti("Marinara"));
	pastaVec.push_back(new pastas::Alfredo("Shrimp"));
	pastaVec.push_back(new pastas::PastaDish());
	
	for (auto dish : pastaVec) {
		std::cout<<"Item: " <<dish->getDish() <<std::endl;
	}
	
	for (auto dish : pastaVec)
	{
		delete dish;
	}
	
	std::cout<<"Pasta dish: "<< pasta->getDish()<<std::endl;
	
	std::cout<<"Spagetti: "<<spagetti->getDish()<<spagetti->getCheese()<<std::endl;
	
	delete pasta;
	delete spagetti;
	
	return 0;
}