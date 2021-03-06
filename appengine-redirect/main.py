from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch, urlfetch_errors


ENDPOINT = "http://188.242.150.98:7777"


class AllHandler(webapp.RequestHandler):
    def proxy(self):
        path = self.request.path_qs
        headers = self.request.headers
        headers.pop("Host", None)

        try:
            response = urlfetch.fetch(
                ENDPOINT + path,
                self.request.body,
                self.request.method,
                self.request.headers,
                False, True, 5)

            self.response.headers = response.headers
            self.response.write(response.content)
        except urlfetch_errors.Error as e:
            self.response.write(e)

    def head(self):
        self.proxy()

    def get(self):
        self.proxy()

    def post(self):
        self.proxy()


application = webapp.WSGIApplication([('/.*', AllHandler)])


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
