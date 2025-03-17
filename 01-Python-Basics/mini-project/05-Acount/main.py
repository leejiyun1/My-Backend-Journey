from model.bank_service import BankingService

def main() -> None:
    """은행 시스템 메인 함수"""

    service = BankingService()  # BankingService 인스턴스 생성

    while True:
        print("\n=== 은행 시스템 ===")
        print("1. 사용자 추가")
        print("2. 사용자 찾기 및 메뉴 실행")
        print("3. 종료")

        choice = input("원하는 작업을 선택하세요: ").strip()

        if choice == "1":
            username = input("추가할 사용자 이름을 입력하세요: ").strip()
            service.add_user(username)

        elif choice == "2":
            username = input("찾을 사용자 이름을 입력하세요: ").strip()
            service.user_menu(username)  #  사용자 찾고 메뉴 실행

        elif choice == "3":
            print("프로그램을 종료합니다.")
            break

        else:
            print("올바른 번호를 입력하세요.")

if __name__ == "__main__":
    main()  # main 함수 실행
