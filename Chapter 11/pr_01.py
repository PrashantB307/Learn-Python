



class C1dvec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j" 


class C2dvec(C1dvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"  


v1 = C1dvec(3, 4)
v2 = C2dvec(5, 7, 9)

print(v1)     # ====> 3i + 4j
print(v2)     # ====> 5i + 7j + 9k
