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
    
    def user_menu(self, username:str) -> None:
        
        user = self.find_user(username)

        if not user:
            print("사용자 {username}을(를) 찾을 수 없습니다.")
            return
        
        while True:

            print("\n======사용자 메뉴======")
            print("1. 입금")
            print("2. 출금")
            print("3. 잔고 확인")
            print("4. 거래 내역")
            print("5. 종료")

            choice = input("원하는 작업을 선택해주세요.").strip()

            if choice == "1":
                amount = int(input("입금하실 금액을 입력해주세요."))
                user.account.deposit(amount)

            elif choice == "2":
                amount = int(input("출금하실 금액을 입력해주세요."))
                user.account.withdraw(amount)
            
            elif choice == "3":
                print(f"현재 잔고: {user.account.get_balance()}원")

            elif choice == "4":
                transactions = user.account.get_transactions()
                if transactions:
                    for i in transactions:
                        print(i)
                else:
                    print("거래 내역이 없습니다.")

            elif choice == "5":
                print("메뉴를 종료합니다.")
                break

            else:
                print("올바른 숫자를 입력해주세요.")