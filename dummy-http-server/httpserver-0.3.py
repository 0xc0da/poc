#!-*- coding: utf8 -*-
#
# PoC - Dummy HTTP Server
# Armazena o valor do campo User-Agent de qualquer request, e
# retorna 200 OK.
#
# Uso: python http-server-0.3.py <IP> <Port> <Logfile>
# Ex.: python http-server-0.3.py 127.0.0.1 8080 ua.txt
#
# Versao: 0.3 - 15/Set/2013
#
# Daniel Marques - daniel /arroba\ codalabs /ponto\ net
# http://codalabs.net
#
# Changelog
# v0.3~> Versão inicial.


from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
import urlparse
import sys

class RequestHandler(BaseHTTPRequestHandler):

    def generic_handling(self):
        with open(sys.argv[3],'a') as logfile:
            line = self.headers["user-agent"]
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
        print "Use: %s <IP> <Port> <Logfile>" % (sys.argv[0])
        sys.exit(1)

    host = sys.arv[1]
    port = int(sys.argv[2])

    server = HTTPServer((host, port), RequestHandler)    
    print 'Server started, use <Ctrl-C> to stop'
    server.serve_forever()    
