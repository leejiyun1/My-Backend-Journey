from .transaction import Transaction
from utils.exceptions import InsufficientFundsError, NegativeAmountError
from utils.decorators import validate_transaction

class Account():

    # 초기화 함수
    def __init__(self) -> None:
        self.__balance: int = 0
        self.transactions: list = []

    # 입금
    @validate_transaction
    def deposit(self, amount:int) -> None:
        self.__balance += amount
        transaction = Transaction("입금", amount, self.__balance)
        self.transactions.append(transaction)   
        
    # 출금
    @validate_transaction
    def withdraw(self, amount:int) -> None:
        # 잔고확인
        if amount > self.__balance:
            raise InsufficientFundsError(self.__balance)
        # 메소드 함수
        self.__balance -= amount
        transaction = Transaction("출금", amount, self.__balance)
        self.transactions.append(transaction)

    
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