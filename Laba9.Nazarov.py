import random

def get_random_sequence(n):
    numbers = list(range(1, n+1))
    random.shuffle(numbers)
    return numbers

def main():
    while True:
        try:
            n = int(input("Введите натуральное число N: "))
            if n <= 0:
                print("Число должно быть больше 0!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите корректное натуральное число.")

    sequence = get_random_sequence(n)

    print("Последовательность чисел от 1 до N в случайном порядке:")
    print(sequence)

if __name__ == "__main__":
    main()