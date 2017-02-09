#pragma once

#include <string>

namespace pastas
{
	class PastaDish{
	public: PastaDish();
	public: virtual std::string getDish() const;
	public: virtual ~PastaDish();
	};
}