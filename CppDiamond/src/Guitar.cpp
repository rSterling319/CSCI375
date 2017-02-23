#include "Guitar.h"

namespace power {
    Guitar::Guitar(owns::Own &own, const int &current, const int &resistance)
    :
    owns::Owned(own),
    instruments::Instrument(own),
    power::Powered(own),
    _current(current),
    _resistance(resistance),
    _volts(current*resistance),
    _instType(static_cast<instruments::Type::classification>(4))
    {
    }
/*
    instruments::Type::classification Guitar::getType() const {
        return _type;
    }

    void Guitar::setType(const instruments::Type::classification &value) {
        if (_type != value) {
            _type = value;
        }
    }
    */
    int Guitar::getResistance() const {
        return _resistance;
    }

    void Guitar::setResistance(const int &value){
        if(_resistance != value) {
            _resistance = value;
            updateVolts();
        }
    }

    int Guitar::getCurrent() const {
        return _current;
    }
    void Guitar::setCurrent(const int &value){
        if(_current != value){
            _current = value;
            updateVolts();
        }
    }

    int Guitar::getVolts() const {
        return _volts;
    }

    void Guitar::updateVolts(){
        _volts = _current * _resistance;
    }

}