class A:

    def test(self):
        print("test with no argument")

    def test(self,a):
        print("test with 1 argument")

    def test(self,a,b):
        print("test with 2 argument")

a1=A()
a1.test()
a1.test(10)
a1.test(10,20)
