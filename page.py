class Page:
    def __init__(self , file_name , code , title):
        self.title_ = title
        self.code_ = code
        self.file_name_ = file_name
    def title(self):
        return self.title_
    def code(self):
        return self.code_
    def name(self):
        return self.file_name_