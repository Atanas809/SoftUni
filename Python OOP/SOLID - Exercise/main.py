class W:
    def work(self):
        pass


class A(W):
    def work(self):
        return "working...."


class B(W):
    def work(self):
        return "working...."


work1 = A()
work2 = B()
work3 = W()

workers = [work3, work1, work2]

for worker in workers:
    if isinstance(worker, W):
        print("hoooya i gat it!")
    else:
        print("WTF is going on")