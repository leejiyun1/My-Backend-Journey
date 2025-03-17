from typing import Callable

def validate_transaction(func: Callable) -> Callable:
    def wrapper(self, amount: int) -> None:
        if amount <= 0:
            print("거래 금액은 0보다 커야 합니다!")
            return
        return func(self, amount)   
    
    return wrapper