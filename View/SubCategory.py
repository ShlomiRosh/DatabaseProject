from View.Category import Category, OUTSIDE


class SubCategory(Category):
    def __init__(self, controller, frame, name):
        Category.__init__(self, controller, frame, name)

    def on_click(self, controller):
        if self.check_var.get():
            print(self.name[1] + " is checked")
        else:
            print(self.name[1] + " not checked")
