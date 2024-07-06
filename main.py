import os
from Elements.page import Page
from Elements.button import Button
from Elements.anchor import anchor
from c import *

class PyWeb:
    def __init__(self, path):
        self.path : str = path
        self.pages : list = []
        self.currentPage : Page = None
        if os.path.isdir(f"{path}") == False:
            os.mkdir(f'{path}')
    def open(self):
        os.system(f'cmd /k "start {self.path}/{self.currentPage.name()}"')
    def CreatePage(self, name, title):
        self.pages.append(Page(file_name = name , code = "" , title=title))
        return Page(file_name = name , code = "" , title=title)
    def SelectPage(self, name):
        for page in self.pages:
            if page.name() == name:
                self.currentPage = page
    def execute(self):
        for page in self.pages:
            f = open(f'{self.path}/{page.name()}' , "w")
            f.write(HTML + page.code() + END)
            f.close()

    def Button(self, args : dict = {
        "width" : float,
        "height" : float,
        "text" : str
    }):
        self.currentPage.code_ += f'<button style = "width : {args["width"]}px; height : {args["height"]}px">{args["text"]}</button>'
        return Button(float(args["width"]) , float(args["height"]), args["text"])
    def Anchor(self, args : dict = {
        "href" : Page,
        "text" : str
    }):
        self.currentPage.code_ += f'<a href = {args["href"].name()}>{args["text"]}</a>'
        return anchor(args["href"].name() , args["text"])
    