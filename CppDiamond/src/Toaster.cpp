#include "Toaster.h"

namespace power {
    Toaster::Toaster(owns::Own &own, const int &current, const int &resistance)
    :
    owns::Owned(own),
    power::Powered(own),
    _current(current),
    _resistance(resistance),
    _volts(current*resistance)
    {
    }

    int Toaster::getResistance() const {
        return _resistance;
    }

    void Toaster::setResistance(const int &value){
        if(_resistance != value) {
            _resistance = value;
            updateVolts();
        }
    }

    int Toaster::getCurrent() const {
        return _current;
    }
    void Toaster::setCurrent(const int &value){
        if(_current != value){
            _current = value;
            updateVolts();
        }
    }

    int Toaster::getVolts() const {
        return _volts;
    }

    void Toaster::updateVolts(){
        _volts = _current * _resistance;
    }
}