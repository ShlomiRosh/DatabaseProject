from View.Category import Category, OUTSIDE


class SubCategory(Category):
    def __init__(self, controller, frame, name):
        Category.__init__(self, controller, frame, name)
