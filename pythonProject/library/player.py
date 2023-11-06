from library.user import User


class Player(User):
    development_points:int
    name:str

    def __init__(self,name:str, developmentPoints:int):
        super().__init__(0,name)
        self.development_points = developmentPoints


