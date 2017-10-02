
class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor is Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print self.last_name + " " + self.eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, no_of_toys):
        print "Child Constructor here"
        Parent.__init__(self, last_name, eye_color)
        self.no_of_toys = no_of_toys

    def show_info(self):
        print self.last_name +" "+ self.eye_color+" " + self.no_of_toys


#billy_cyrus = Parent("cyrus", "Blue")
#print billy_cyrus.last_name

miley_cyrus = Child("cyrus","green","100")
#print miley_cyrus.no_of_toys
#print miley_cyrus.eye_color

#billy_cyrus.show_info()
miley_cyrus.show_info()
