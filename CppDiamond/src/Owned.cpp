#include <iostream>
#include "Owned.h"
#include "Own.h"

namespace owns {
    Owned::Owned(Own &_own) : own(_own) {
        std::cout<<"Owned()@"<<(void*) this <<std::endl;
        own.owned.push_back(OwnedPtr(this));
    }
    Owned::~Owned() {
        std::cout<<"~Owned()@"<<(void*) this <<std::endl;
    }
}