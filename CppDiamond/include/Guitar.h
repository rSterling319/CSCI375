#pragma once

#include "Owned.h"
#include "Powered.h"
#include "Instrument.h"
#include "Type.h"

namespace power {
    class Guitar : public instruments::Instrument, public Powered {
        private: int _current;
        private: int _resistance;
        private: int _volts;

        private: instruments::Type::classification _instType;
        public: instruments::Type::classification getType() const {return _instType; }
        public: void setType(const instruments::Type::classification &value) {_instType=value; }
        //Woodwind=1, Brass=2, Percussion=3, String=4
        public: Guitar(owns::Own &own, const int &resistence, const int &current);

        public: virtual ~Guitar();

        public: int getResistance() const;
        public: void setResistance(const int &value);

        public: int getCurrent() const;
        public: void setCurrent(const int &value);

        public: int getVolts() const;

        private: void updateVolts();

    };
}

