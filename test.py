from main import *

website = PyWeb("website")
website.CreatePage("a.html", "a")
website.CreatePage("h.html" , "h")
website.SelectPage('a.html')
website.Button({
    "width" : 100,
    "height" : 100,
    "text" : "Click Me",
})
website.execute()
website.open()