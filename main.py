import os
from page import Page
from c import *

class PyWeb:
    def __init__(self, path):
        self.path : str = path
        self.pages : list = []
        self.currentPage : Page = None
    def open(self):
        os.system(f'cmd /k "start {self.path}/{self.currentPage.name()}"')
    def CreatePage(self, name, title):
        self.pages.append(Page(file_name = name , code = HTML1 + title + HTML2 + END , title=title))
    def SelectPage(self, name):
        for page in self.pages:
            if page.name() == name:
                self.currentPage = page
    def execute(self):
        for page in self.pages:
            f = open(f'{self.path}/{page.name()}' , "w")
            f.write(page.code())
            f.close()

    
    
web = PyWeb("website")
web.CreatePage("sigma.html" , "beta")
web.CreatePage("beta.html" , "Sigma")
web.SelectPage("sigma.html")
web.execute()
web.open()