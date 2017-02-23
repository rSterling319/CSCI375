#pragma once

#include "Owned.h"

namespace power {

    class Powered : public virtual owns::Owned {
        public: Powered(owns::Own &own);
        public: virtual int getVoltage() const;
        public: virtual ~Powered();
    };
}