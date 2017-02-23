#include "Own.h"

namespace owns {
    Own::~Own() {
        for (auto item : owned) {
            delete item;
        }
    }
}