from points import P
log_level=1

def log(*arg):
	if log_level > 0 :
		for s in arg :
			print s,", ",
		print 


class MillDraw:
	def __init__(id=None):
		pass
	def draw_start(self,x,y):
		self.items = []
		# item g x y z i j k
		self.items.append((0, x, y, 0, None, None, None))		
		self.p = P(x,y)

	def line_to(self,x,y):
		self.items.append((1, x, y, 0, None, None, None))		
		print "Line to (%s, %s)"%(x,y)
	
	def arc_to(self,x,y,i,j):
		print "Arc to (%s, %s)-(%s, %s)"%(x,y,i,j)

	def draw(self):
		self.line = 0
		pass
	
	def get_line(self) :
		if self.line >= len(self.items) :
			return (-1,0,0,0,0,0,0)
		else :
			self.line += 1
			return self.items[self.line-1]

