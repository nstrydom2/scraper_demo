


class Algorithms:
    def __init__(self):
        pass

    def fizzbuzz(self, num):
        result = ''

        if num % 5 != 0 and num % 3 != 0:
            result += str(num)
        if num % 5 == 0:
            result += "fizz"
        if num % 3 == 0:
            result += "buzz"

        return result


if __name__ == '__main__':
    a = Algorithms()

    for num in range(1, 21):
        print(a.fizzbuzz(num))


