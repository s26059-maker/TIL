R = int(7)
guess = 0

while guess != R:
    guess = int(input("숫자를 입력하세요: "))
    if guess != R:
        print("다시 입력하세요.")
    if guess == R:
        break

print  ("정답입니다!")