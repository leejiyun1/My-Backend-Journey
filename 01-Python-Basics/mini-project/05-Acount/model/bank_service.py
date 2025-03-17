from .user import User

class BankingService():
    def __init__(self) -> None:
        self.user = []


    def add_user(self, username: str) -> None:
        
        new_user = User(username)
        self.user.append(new_user)
        print(f"사용자 {username}이(가) 추가되었습니다.")

    def find_user(self, username: str) -> User:

        for user in self.user:
            if user.username == username:
                return user
        return None
    
    def user_menu(self, username:str)