# 클래스의 선언
class Calculator:
    # 클래스의 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


# 클래스의 상속
class CalculatorExp(Calculator):

    def pow(self):
        return self.first ** self.second

    def square(self):
        return self.first ** 2

    def cube(self):
        return self.first ** 3


# 매소드의 오버라이딩
class SafeCalculatorExp(CalculatorExp):
    def div(self):
        if self.second == 0:
            return "div by 0"
        else:
            return self.first / self.second


#이 파일이 이 파일이름으로 실행되었을 때만
if __name__ == "__main__":
    c = Calculator(0, 0)
    c.setdata(10, 20)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())

    c2 = Calculator(100, 2020)
    print(c2.add())
    print(c2.sub())
    print(c2.mul())
    print(c2.div())

    c3 = CalculatorExp(10, 40)
    print(c3.add())
    print(c3.sub())
    print(c3.mul())
    print(c3.div())
    print(c3.pow())
    print(c3.square())
    print(c3.cube())

    c4 = SafeCalculatorExp(10, 0)
    print(c4.add())
    print(c4.sub())
    print(c4.mul())
    print(c4.div())
    print(c4.pow())
    print(c4.square())
    print(c4.cube())
