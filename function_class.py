class Function:
    def __init__(self,dimensions: int):
        self.dimensions = dimensions
        
    @property
    def dimensions(self):
        return self._dimensions
    
    @dimensions.setter
    def dimensions(self,dimensions: int):
        self._dimensions = dimensions
        
    
             