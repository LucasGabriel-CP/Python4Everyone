import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **Dic) -> None:
        self.contents = list()
        for i, j in Dic.items():
            for k in range(j):
                self.contents.append(i)
    
    def draw(self, N) -> list():
        if N >= len(self.contents) - 1:
            return self.contents
        ans = list()
        for i in range(N):
            Index = random.randrange(len(self.contents))
            ans.append(self.contents.pop(Index))
        return ans

def Valid(A, B: list()):
    for i in A:
        if len(B) == 0:
            return True
        Ok = False
        for j in B:
            if i == j:
                Ok = True
                B.remove(j)
                break
        if not Ok:
            return False
        Ok = False
    return True

def experiment(hat: Hat(), expected_balls, num_balls_drawn, num_experiments):
    Count = 0
    for i in range(num_experiments):
        Temp = copy.deepcopy(hat)
        Result = Temp.draw(num_balls_drawn)
        EB = list()
        for i, j in expected_balls.items():
            for k in range(j):
                EB.append(i)
        if Valid(EB, Result):
            Count += 1
    return Count * 1.0 / num_experiments