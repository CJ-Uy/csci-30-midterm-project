class bst_node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

class bst:
    def __init__(self, root):
        self.root = bst_node(root)
    
    def search(self, x):
        if x.key == self.key:
            return self
        elif x.key > self.key:
            if self.right is None:
                return None
            return self.search(self.right, x)
        elif x.key < self.key:
            if self.left is None:
                return None
            return self.search(self.left, x)
        
    def insert(self, x):
        if x == self.key:
            return False
        else:
            if x > self.key:
                if self.right is None:
                    self.right = x
                else:
                    self.insert(self.right, x)
            elif x< self.key:
                if self.left is None:
                    self.left = x
                else:
                    self.insert(self.left, x)
                    
            return True
        
    def delete(self, x):
        found = self.search(x) 
        if found is not None and found.right is not None:
			
            return True
        return False
     
