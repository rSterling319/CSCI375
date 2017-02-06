#pragma once

namespace pastas
{
	class PastaDish{
	public: PastaDish();
	public: virtual string getDish() const;
	public: virtual ~PastaDish();
	};
}