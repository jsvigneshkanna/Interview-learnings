class Player:
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def get_name(self):
        return self.name

    def __str__(self) -> str:
        return f"player {self.name} is with symbol: {self.symbol}"