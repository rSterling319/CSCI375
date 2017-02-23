#include <iostream>
#include "Powered.h"

namespace power {

    Powered::Powered(owns::Own &own) : owns::Owned(own) {
        std::cout<< "Powered@"<<(void*) this <<std::endl;
    }

    int Powered::getVoltage() const {
        return 0;
    } 

    Powered::~Powered() {
        std::cout<<"~Powered()@"<<(void*) this <<std::endl;
    }
}