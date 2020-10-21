# Python code demonstrate the working of
list1=[1,2,3]
list2=[4,5,6]
CombLst=[[x,y] for x in list1 for y in list2]
print(CombLst)
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

# parent class
class Programming:
    # properties
    DataStructures = True
    Algorithms = True

    # function practice
    def practice(self):
        print("Practice makes a man perfect")

    # function consistency
    def consistency(self):
        print("Hard work along withjk consistency can defeat Talent")

    # child class


class Python(Programming):

    # function
    def consistency(self):
        print("Hard work along withddd consistency can defeat Talent.")


Py = Python()
Py.consistency()
Py.practice()
