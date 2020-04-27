import falcon

class HelloWorldResource:

    def on_get(self, request, response):
        response.media = ('Hello world from App API!')


app = falcon.API()
app.add_route('/', HelloWorldResource()) 
