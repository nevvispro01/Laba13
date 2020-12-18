import random

if __name__ == '__main__':
    exit = False
    while exit == False:
        print("Введите цифру нужного действия")
        print("1) Запустить жеребьевку")
        print("2) Выход")
        action = int(input())
        print()
        if action == 1:
            N = 0
            L = []
            while N < 1:
                N = int(input("Введите количество бочонков: "))
                print()
            for i in range(N):
                test = False
                check = input("Введите любой символ для жеребьевки: ")
                print()
                while test == False:
                    barrel = random.randint(1, N)
                    test = True
                    for j in range(len(L)):
                        if L[j] == barrel:
                            test = False
                L.append(barrel)
                print(i+1, "номер жеребьевки равен: ", barrel)
                print()
        elif action == 2:
            exit = True
            print("Выход...")
        else:
            print("Введено неверное число, попробуйте еще раз!")