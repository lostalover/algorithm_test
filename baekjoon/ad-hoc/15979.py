from math import gcd


class BaekJoon15979():
    def __init__(self) -> None:
        pass

    def solution(self, M: int, N: int) -> None:
        if M == 0 and N == 0:
            print('0')
            return
        if gcd(M, N) != 1:
            print('2')
            return
        else:
            print('1')


if __name__ == "__main__":
    bj15979 = BaekJoon15979()
    temp = input()
    temp = temp.split(' ')
    M = int(temp[0])
    N = int(temp[1])
    bj15979.solution(M, N)
