#!/usr/bin/python

"""
 contentApp class
 Simple web application for managing content
 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp # Se ejecuta el otro programa (webapp) menos lo que ponga en el "__main__"
              # Solo nos interesa la clase

class contentApp (webapp.webApp):
    """Simple web application for managing content.
    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': 'Root page',
               '/page': 'A page'
               } # Son variables de clase

    def parse(self, request): # Tiene que saber que tipo de metodo y recurso se utiliza
                              # y el cuerpo (PUT-Creo el cuerpo/GET-no importa el cuerpo)
        """Return the resource name (including /)"""
        # Ejemplo : GET | /pepe | HTTP1.1
        try:
            metodo = request.split(' ',1)[0] # partes una vez y te quedas con el primero (GET)
            recurso = request.split(' ', 2)[1] # partimos dos veces por cada espacio y te quedas
                                               # con el segundo (el del medio :PEPE)
            if metodo == 'POST':
                cuerpo = request.split('\r\n\r\n')[1]
            else:
                cuerpo = ''
        except IndexError:
            return None
        return (metodo , recurso , cuerpo) # Lo dividimos por espacios y nos quedamos con el recurso
                                        # Con la barra incluida (/urltochaca.com )

    def process(self, resourceName):

        metodo, recurso, cuerpo = resourceName

        #si el recuerso esta en content:
        if metodo == 'GET':
            if recurso in self.content:
                httpCode = '200 OK'
                htmlBody += '<html><body>' + self.content[recurso]
                htmlBody +='<form method="POST" action="">'
                htmlBody += 'New URL: <input type="text" name="new_URL"><br>'
                htmlBody += '<input type="submit" value="Send">'
                htmlBody += '</form>'
                htmlBody += '</body></html>'
            else:
        #si no encuentro not found
                httpCode = '404 Not Found'
                htmlBody = 'Not Found'
        elif metodo == 'PUT'or metodo == 'POST':
            self.content[recurso]=cuerpo
            httpCode = '200 OK'
            htmlBody = 'Todo ha ido bien'
        else:
            httpCode = '405 Method Not'
            htmlBody = 'Go Away!'
        return (httpCode, htmlBody)


if __name__ == "__main__":
    try:
        testWebApp = contentApp("localhost", 2312)
    except KeyboardInterrupt:
        print "Servidor cerrado"
