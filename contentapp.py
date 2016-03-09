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
               '/cris': 'http://gsyc.es'
               } # Son variables de clase

    def parse(self, request): # Tiene que saber que tipo de metodo y recurso se utiliza
                              # y el cuerpo (PUT-Creo el cuerpo/GET-no importa el cuerpo)
        """Return the resource name (including /)"""
        # Ejemplo : GET | /pepe | HTTP1.1
        metodo = request.split(' ',1)[0] # partes una vez y te quedas con el primero (GET)

        recurso = request.split(' ', 2)[1] # partimos dos veces por cada espacio y te quedas
                                           # con el segundo (el del medio :PEPE)

        cuerpo = request.split('\r\n\r\n',1)[1]

        return metodo , recurso , cuerpo # Lo dividimos por espacios y nos quedamos con el recurso
                                        # Con la barra incluida (/urltochaca.com )
    def process(self, peticion):
        """Process the relevant elements of the request.
        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """
        metodo , recurso , cuerpo = peticion
        if metodo == "GET":
            if resourceName "/pepe": # self.content es un diccionario (clave/valor)
                httpCode = "302 Found\r\nLocation: " + self.content['/cris'] + '\r\n' # Con esto hemos realizado el redireccionamiento
                htmlBody = "<html><body>" + self.content[resourceName] \
                    + "</body></html>"

            if resourceName in self.content: # self.content es un diccionario (clave/valor)
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[resourceName] \
                    + "</body></html>" # resourceName nos devuelve el valor ; '\' nos indica que la linea sigue
                # ¡¡ AQUI VAN LAS FOTOS !!

            if recurso in self.content: # self.content es un diccionario (clave/valor)
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[resourceName] \
                    + "</body></html>" # resourceName nos devuelve el valor ; '\' nos indica que la linea sigue

            else:
                httpCode = "404 Not Found"
                htmlBody = "Not Found"
        elif metodo == "PUT" or metodo == "POST": # aqui nos leeria el post -- POSTER (app)
            self.content[recurso]  = cuerpo.split('=')[1] # si no existe el cuerpo lo meto y si existe lo actualiza
            httpCode = "200 OK"
            htmlBody = "Todo Bien"

        else:
            httpCode = "405 Method Not Allowed"
            htmlBody = "Go away!"  # Este seria el cuerpo ; NOTA: El Head no mira los cuerpos
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
# Formulario :  <form method= "POST" action=""#mandame a la propia pagina en la que esto>
#                   <input type = "submit" value "Enviar">
#                   <input type = "text" name = "firstname">
#               </form>
# Lo copiamos y lo guardamos en oto fichero
