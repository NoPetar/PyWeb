from main import *

website = PyWeb("website")
a = website.CreatePage("a.html", "a")
h = website.CreatePage("h.html" , "h")
website.SelectPage('a.html')
website.Button({
    "width" : 100,
    "height" : 100,
    "text" : "Click Me",
})
website.Anchor({
    "href" : h,
    "text" : "Click Me"
})

website.execute()
website.open()