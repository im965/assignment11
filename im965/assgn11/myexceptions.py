# This module defines the exceptions

class NotListError(Exception) :
        def __init__(self,msg="positions argument must be a list") :
            self.m=msg
        def __str__(self):
            return repr(self.m)


class NotNumError(Exception) :
        def __init__(self,msg="elements in positions(list) must be numeric"):
            self.m=msg
        def __str__(self):
	    return repr(self.m)

class NotIntError(Exception) :
        def __init__(self,msg="elements in positions(list) must be whole numbers"):
            self.m=msg
	def __str__(self):
	    return repr(self.m)

class InvalidPosError(Exception) :
        def __init__(self,msg="elements in positions(list) must be between 1 and 1000"):
            self.m=msg
	def __str__(self):
	    return repr(self.m)

class TrialNotNumError(Exception) :
        def __init__(self,msg="num_trials argument must be numeric"):
            self.m=msg
        def __str__(self):
            return repr(self.m)

class TrialNegError(Exception) :
	def __init__(self,msg="num_trials argument must be positive integer"):
	    self.m=msg
	def __str__(self):
	    return repr(self.m)

