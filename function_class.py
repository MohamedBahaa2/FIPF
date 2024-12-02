class Function:
    def __init__(self,degree):
        self.degree = degree
        
    @property
    def degree(self):
        return self._degree
    
    @degree.setter
    def degree(self,degree):
        self._degree = degree
        
    
            