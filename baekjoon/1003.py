class BaekJoon1003():
    fibo = [0, 1, 1]

    def __init__(self) -> None:
        for i in range(3, 41):
            self.fibo.append(self.fibo[i-1] + self.fibo[i-2])

    def solution(self, value_N: int):
        if value_N == 0:
            print('1 0')
            return
        elif value_N == 1:
            print('0 1')
            return
        print(f'{self.fibo[value_N-1]} {self.fibo[value_N]}')
        return


if __name__ == "__main__":
    bj1003 = BaekJoon1003()
    test_case_T = int(input())
    for i in range(0, test_case_T):
        value_N = int(input())
        bj1003.solution(value_N)
