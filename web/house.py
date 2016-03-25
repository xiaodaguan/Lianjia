import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json

from tornado.options import define, options
from json2html import *

define("port", default=8876, help="run on the given port.", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello!")


class NowaMagicHandler(tornado.web.RequestHandler):
    def get(self):
        content = u'Welcome!'
        content += u"<div><a href='www.baidu.com'>baidu</a></div>"
        # self.write(content)
        title = u'test'
        self.render("../templates/index.html", title=title, content=content)


class HouseHandler(tornado.web.RequestHandler):
    def get(self):
        t = 'house info'

        page = self.get_argument('page', 1)
        start = 10 * (page - 1)
        end = 10 * page
        cont = ""
        with open('../items.jl', 'r') as f:
            i = 1

            line = f.readline()
            while (line):
                # todo
                if i <= start: continue

                if i <= end:
                    data = json.loads(line)
                    cont += json2html.convert(json=data)

                    line = f.readline()
                    i += 1
                else:
                    break
        self.render('../templates/house.html', title=t, content=cont)


def main():
    tornado.options.parse_command_line()

    application = tornado.web.Application([
        (r"/hello", MainHandler),
        (r"/nowamagic", NowaMagicHandler),
        (r"/house", HouseHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
