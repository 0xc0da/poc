from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import urlparse
import sys

class RequestHandler(BaseHTTPRequestHandler):

    def generic_handling(self):
        with open(sys.argv[2],'a') as logfile:
            line = self.headers["user-agent"]# + "\n"
            logfile.write(line + '\n')
        self.send_response(200)
	for name,value in self.headers.items():
		print "%s -> %s" % (name,value)
        self.end_headers()
        return

    def do_HEAD(self):
        self.generic_handling()
        return

    def do_GET(self):
        self.generic_handling()
        return

    def do_POST(self):
        self.generic_handling()
        return

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Use: %s <Port> <Logfile>" % (sys.argv[0])
        sys.exit(1)

    port = int(sys.argv[1])

    server = HTTPServer(('localhost', port), RequestHandler)    
    print 'Server started, use <Ctrl-C> to stop'
    server.serve_forever()    
