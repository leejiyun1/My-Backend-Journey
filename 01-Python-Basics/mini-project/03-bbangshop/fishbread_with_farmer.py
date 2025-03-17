

def order_bread():
    print("")

def admin_mode():
    print("")


while True:
    mode = input("원하는 모드를 선택하세요. (주문, 관리자, 종료) : ")
    
    if mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
    elif mode == "종료":
        print("시스템을 종료합니다.")
        break
