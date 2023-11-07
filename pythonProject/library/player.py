from library.user import User


class Player(User):
    development_points:int
    name:str

    def __init__(self,id:int,name:str, developmentPoints:int):
        super().__init__(id,name)
        self.development_points = developmentPoints


