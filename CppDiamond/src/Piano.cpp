#include <iostream>
#include "Piano.h"

namespace instruments {
    Piano::Piano(owns::Own &own)
    :
    owns::Owned(own),
    instruments::Instrument(own),
    _instType(static_cast<instruments::Type::classification>(4))
    {
    }

    Type::classification Piano::getType() const {
        return _instType;
    }

    void Piano::setType(const Type::classification &value){
        if(_instType != value){
            _instType = value;
        }
    }

    Piano::~Piano(){}
}