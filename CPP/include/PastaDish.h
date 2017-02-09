#pragma once

namespace pastas
{
	class PastaDish{
	public: PastaDish();
	public: virtual std::string getDish() const;
	public: virtual ~PastaDish();
	};
}