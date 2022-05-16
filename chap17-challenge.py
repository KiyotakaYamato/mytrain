# chapter 17

import re
senten = "The goast that says boo haunts the loo, luoo"
ma = re.findall(".oo", senten, re.IGNORECASE)
print(ma)
