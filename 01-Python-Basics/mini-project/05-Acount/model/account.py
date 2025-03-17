from .transaction import Transaction

class Account():

    # 초기화 함수
    def __init__(self) -> None:
        self.__balance: int = 0
        self.transactions: list = []

    # 입금
    def deposit(self, amount:int) -> None:

        # 양수 확인
        if amount > 0:
            self.__balance += amount
            transaction = Transaction("입금", amount, self.__balance)
            self.transactions.append(transaction)
        else:
            print("0보다 큰 금액을 입력해주세요.")
        
    # 출금
    def withdraw(self, amount:int) -> None:

        # 잔액과 양수 확인
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            transaction = Transaction("출금", amount, self.__balance)
            self.transactions.append(transaction)
        else:
            print("0보다 크거나 잔고보다 작은 금액을 입력해주세요.")

    # 잔고 반환 메서드
    def get_balance(self) -> int:
        return self.__balance

    # 거래 내력 반환 메서드
    def get_transactions(self) -> list:
        return self.transactions

    # 클래스 변수 및 메서드
    bank_name = ""

    def get_bank_name(cls) -> str:
        return cls.bank_name

    def set_bank_name(cls, name: str) -> None:
        cls.bank_name = name    