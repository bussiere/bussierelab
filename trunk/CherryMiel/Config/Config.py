import cherrypy

class Config():
    def getConfig(self):
        settings = {
            'global':{
                      'server.socket_port' : 80
                      }
            }
        return settings
