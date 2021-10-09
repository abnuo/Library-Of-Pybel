from flask import *"
from library_of_babel import *
import html
import os

app = Flask(__name__)
heroku = True
porty = int(os.environ.get('PORT', 5000))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/book/<name>')
def book(name):
    try:
      title = getTitle(name)
      page = getPage(name)
      firstpage = "/book/" + name[0:name.rfind(":")] + ":0"
      lastpage = "/book/" + poop[0:poop.rfind(":")] + ":410"
      prevpage = "/book/" + name[0:name.rfind(":")] + ":" + str(int(name[name.rfind(":") + 1:len(name)])-1)
      nextpage = "/book/" + name[0:name.rfind(":")] + ":" + str(int(name[name.rfind(":") + 1:len(name)])+1)
      randpage = "/book/" + name[0:name.rfind(":")] + ":" + str(random.randint(0, 410))
    except Exception as e:
      return html.escape(str(e))
    #title = "title"
    #page = "page"
    return render_template('page.html', name=html.escape(name), title=title, page=html.escape(page), firstpage=firstpage, prevpage=prevpage, nextpage=nextpage, lastpage=lastpage, randpage=randpage)

@app.route("/search/<q>")
def searchy(q):
    query = text_prep(q)
    containing = search(text_prep(query))
    only = search(query.ljust(length_of_page))
    stitle = searchTitle(query)
    return f"<a href=\"/book/{containing}\">Page which includes this text</a><br><a href=\"/book/{only}\">Page which includes only this text</a><br><a href=\"/book/{stitle}:0\">Title which contains this text</a>"
if heroku == True:
  app.run(host='0.0.0.0', port=porty)
else:
  app.run(host='0.0.0.0', port=8080)
