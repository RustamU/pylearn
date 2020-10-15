import string
class A:

    def __init__(self):
        self.shift_dict = {}



    def build_shift_dict(self, shift):

        self.shift = shift
        for a in string.ascii_lowercase:
            self.shift_dict.update({a:string.ascii_lowercase[(string.ascii_lowercase.index(a)+self.shift)%26]})
        for a in string.ascii_uppercase:
            self.shift_dict.update({a:string.ascii_uppercase[(string.ascii_uppercase.index(a)+self.shift)%26]})
        return self.shift_dict

a = A()
print (a.build_shift_dict(3))
