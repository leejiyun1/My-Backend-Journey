from .account import Account

class User():
    def __init__(self, username: str) -> None:
        
        self.username: str = username
        self.account: Account = Account()