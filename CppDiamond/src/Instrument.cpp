#include <iostream>
#include "Instrument.h"

namespace instruments {
    Instrument::Instrument(owns::Own &owned) : owns::Owned(owned) {
        std::cout<<"Instrument()@"<< (void*) this <<std::endl;
    }
    Instrument::~Instrument() {
        std::cout<<"~Instrument()@"<<(void*) this <<std::endl;
    }

}