#pragma once

#include <memory>
#include <vector>

#include "Owned.h"

namespace owns {
    class Own {
        private: std::vector < OwnedPtr > owned;
        public: ~Own();
        friend Owned;
    };
}