from abc import abstractclassmethod


class ABC:  # stands for AbstractClass
    def method_1(self):
        raise NotImplementedError  # this defines a must-be-implemented method

    def method_2(self):  # same here, a must-be-implemented method
        raise NotImplementedError


class Test(ABC):
    def method_1(self):  # here we redefine a must-be-implemented method and implement it
        print("Method 1")

