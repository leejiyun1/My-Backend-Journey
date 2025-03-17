from .user import User
from utils.exceptions import UserNotFoundError, InvalidInputError
from typing import Union

class BankingService():
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, username: str) -> None:
        if username in self.users:
            print(f"사용자 '{username}'은(는) 이미 존재합니다.")
            return
        
        new_user = User(username)
        self.users[username] = new_user
        print(f"사용자 '{username}'이(가) 추가되었습니다.")

    def find_user(self, username: str) -> Union[User, None]:
        """사용자를 찾고 없으면 예외 발생"""
        user = self.users.get(username, None)
        if user is None:
            raise UserNotFoundError(username)  # 예외 발생
        return user
    
    def user_menu(self, username: str) -> None:
        """사용자 메뉴 실행"""
        try:
            user = self.find_user(username)  # 사용자가 없으면 예외 발생
        except UserNotFoundError as e:
            print(f"{e}")
            return
        
        while True:
            print(f"\n=== {username}님의 계좌 메뉴 ===")
            print("1. 입금")
            print("2. 출금")
            print("3. 잔고 확인")
            print("4. 거래 내역")
            print("5. 이전 메뉴로 돌아가기")

            choice = input("원하는 작업을 선택하세요: ").strip()

            try:
                if choice == "1":
                    amount = self.get_valid_amount("💰 입금할 금액을 입력하세요: ")
                    user.account.deposit(amount)

                elif choice == "2":
                    amount = self.get_valid_amount("🏦 출금할 금액을 입력하세요: ")
                    user.account.withdraw(amount)

                elif choice == "3":
                    print(f"💳 현재 잔고: {user.account.get_balance()}원")

                elif choice == "4":
                    transactions = user.account.get_transactions()
                    if transactions:
                        print("\n📜 거래 내역:")
                        for transaction in transactions:
                            print(f" - {transaction}")
                    else:
                        print("📭 거래 내역이 없습니다.")

                elif choice == "5":
                    print("🔙 이전 메뉴로 돌아갑니다.")
                    break

                else:
                    print("⚠ 올바른 숫자를 입력해주세요.")

            except InvalidInputError as e:
                print(f"{e}")
            except Exception as e:
                print(f"알 수 없는 오류 발생: {e}")

    def get_valid_amount(self, prompt: str) -> int:
        """입금/출금 시 올바른 숫자를 입력받는 함수 (예외 처리 포함)"""
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                raise InvalidInputError()
