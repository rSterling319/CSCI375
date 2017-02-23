#pragma once

#include "Owned.h"
#include "Instrument.h"
#include "Type.h"

namespace instruments {
    class Piano : public Instrument {
        private: Type::classification _instType;
        public: Type::classification getType() const;
        public: void setType(const Type::classification &value);

        public: Piano(owns::Own &own);

        public: virtual ~Piano();
    };
}