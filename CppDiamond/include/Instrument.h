#pragma once

#include "Owned.h"
#include "Type.h"

namespace instruments {
    struct Instrument : public virtual owns::Owned {
        Instrument(owns::Own &owned);
        //virtual Type::classification getType() const = 0;
        //virtual void setType(const Type &value) = 0;
        virtual ~Instrument();
    };
}