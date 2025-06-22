import time
def count_up_to(max_number):
    number = 0
    while number < max_number:
        # 숫자를 반환하고 함수 실행을 일시 중단한 뒤, 처리가 끝나면 실행을 재개하여 반환합니다.
        yield number  
        print("count_up_to에서 yield 이후:", number)
        number += 1

for num in count_up_to(5):
    print(num)  # 0, 1, 2, 3, 4 출력
    time.sleep(1)  # 1초 대기
    print("반복문에서 yield됨:", num)  # 반복문에서 yield됨: 0, 1, ...