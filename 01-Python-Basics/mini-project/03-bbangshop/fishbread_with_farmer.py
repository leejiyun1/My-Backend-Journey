stock ={
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}   

sales ={
    "팥붕어빵" : 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택해주세요. (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '뒤로가기'입력 : ")
        if bread_type == "뒤로가기":
            break
        # 메뉴 주문
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력해주세요."))
            if stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f"{bread_type}을(를) {bread_count}개 판매했습니다.")
            else:
                print(f"재고가 부족합니다. \n현재 재고: {stock[bread_type]}")
        else:
            print("팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 하나를 골라주세요.")


def admin_mode():
    print("")

# 메인 기능 선택
while True:
    mode = input("원하는 모드를 선택하세요. (주문, 관리자, 종료) : ")
    
    if mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
    elif mode == "종료":
        print("시스템을 종료합니다.")
        break
