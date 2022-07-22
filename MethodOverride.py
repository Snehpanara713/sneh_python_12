class A:

    def show(self):
        super().show()
        print("Show From A")

class B:

    def show(self):
        print("Show From B")

class C(A,B):

    def show(self):
        super().show()
        print("Show From C")

b1=C()
b1.show()
