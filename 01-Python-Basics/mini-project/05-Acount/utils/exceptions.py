# 사용자 정의 예외 클래스
class InsufficientFundsError(Exception):
    def __init__(self, balance: int) -> None:
        super().__init__(f"잔액이 부족합니다. 현재 잔액: {balance}원")

class NegativeAmountError(Exception):
    def __init__(self) -> None:
        super().__init__("거래 금액은 0보다 커야 합니다!")

class UserNotFoundError(Exception):
    def __init__(self, username: str) -> None:
        super().__init__(f"사용자 '{username}'을(를) 찾을 수 없습니다!")