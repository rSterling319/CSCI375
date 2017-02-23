#pragma once

#include <memory>

namespace owns {
    class Own;
    class Owned;
    typedef Owned * OwnedPtr;

    class Owned {
        private: Own &own;
        public: Owned(Own &_own);
        public: virtual ~Owned();
    };
}