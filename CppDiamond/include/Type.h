#pragma once

#include <iostream>
#include <string>

namespace instruments {
	
	class Type {
		public: enum classification {Woodwind=1, Brass=2, Percussion=3, String=4};
		public: classification instType;
		
		public: Type(classification _instType);
	
		public: virtual void print(std::ostream &out) const;
		
		public: virtual ~Type();
	};
	
	std::ostream& operator<<(std::ostream &out, const Type &inst);	
}