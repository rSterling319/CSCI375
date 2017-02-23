#include <iostream>
#include <vector>

#include "Instrument.h"
#include "Guitar.h"
#include "Piano.h"
#include "Toaster.h"
#include "Type.h"
#include "Own.h"

int main(int argc, char *argv[]){
    owns::Own *own = new owns::Own();

    std::cout<<"New Instrument" <<std::endl;
    instruments::Instrument *inst = new instruments::Instrument(*own);

    std::cout<<"New Guitar"<<std::endl;
    power::Guitar *guitar = new power::Guitar(*own,60,2);

    std::cout<<"New Toaster"<<std::endl;
    power::Toaster *toaster = new power::Toaster(*own,110,2);

    std::cout<<"New Piano"<<std::endl;
    instruments::Piano *piano = new instruments::Piano(*own);

   instruments::Type *stringed = new instruments::Type(static_cast<instruments::Type::classification>(4));

    std::cout<<"Stringed = "<<*stringed<<std::endl;

    std::vector < power::Powered* > powered;
    powered.push_back(new power::Powered(*own)),
    powered.push_back(new power::Guitar(*own, 10, 12)),
    powered.push_back(new power::Toaster(*own, 40,3));

    for (auto item : powered) {
        std::cout<<"This items voltages is: "<<item->getVoltage()<<std::endl;
    }

    std::cout<<"guitar voltage = "<<guitar->getVoltage()<<std::endl;
    guitar->setType(static_cast<instruments::Type::classification>(4));
    std::cout<<"Guitar is a "<<guitar->getType()<<" instrument"<<std::endl;

    std::cout<<"Toaster voltage = "<<toaster->getVoltage()<<std::endl;

    std::cout<<"Piano is a "<<piano->getType()<<" instrument"<<std::endl;

    delete own;

    return 0;


}