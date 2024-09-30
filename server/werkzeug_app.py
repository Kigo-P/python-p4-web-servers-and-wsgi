#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

# @ Request.application method- run any code inside the function in the browser at the place we specify with the development server
@Request.application
def application(request):
    print(f"This web server is running at {request.remote_addr}")
    return Response("A WSGI generated this response!")

# import run_simple from werkzeug.serving- it runs a server for a one page application
#run_simple takes 3 arguments: hostname which is the localhost, port and applicatio which is our function application
if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        hostname = "localhost",
        port = 5555,
        application = application
    )
