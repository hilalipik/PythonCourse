class SuperList(list):
    def __len__(self):
        return 10

sup = SuperList()

print(len(sup))
sup.append(5)
print(sup[0])