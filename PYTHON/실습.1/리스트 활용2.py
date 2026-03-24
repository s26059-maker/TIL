inventory = [5, 0, 12, 1, 0, 7]
for i in inventory:
    if i == 0:
        print("품절:재주문 필요")
    elif i < 3:
        print("재고 부족:확인 요망")
    else:
        print("정상")
