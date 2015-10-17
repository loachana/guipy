

class Students(object):
    def __init__(self, val):
        self.val = val

    def show(self):
        print self.val

    def det(self):
        if self.val <= 5:
            print "you are short"
        else:
            print "you are tall"


'''

we give a name for sudent class as a instance of object

and then call method in it

'''

kamal = Students(4)

kamal.show()
kamal.det()
