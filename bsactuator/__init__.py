import sys
if sys.version_info[0] == 2:
	from bsactuator import *
else:
	from bsactuator.bsactuator import *