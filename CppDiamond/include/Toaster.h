#pragma once

#include "Owned.h"
#include "Powered.h"


namespace power {
    class Toaster : public Powered {
        private: int _current;
        private: int _resistance;
        private: int _volts;

        public: Toaster(owns::Own &own, const int &current, const int &resistance);
        public: virtual ~Toaster();

        public: int getResistance() const;
        public: void setResistance(const int &value);
        
        public: int getCurrent() const;
        public: void setCurrent(const int &value);

        public: int getVolts() const;
        private: void updateVolts();
    };
}