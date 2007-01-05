import cherrypy,os
current_dir = os.path.dirname(os.path.abspath(__file__))
settings = {
            '/img':{'tools.staticdir.on':True,
                          'tools.staticdir.dir':r'img'}
       
            }


class header_begin:
    def __init__(self):
        self.header = "<body>"
    def printh(self):
        return  self.header
    
class header_end:
    def __init__(self):
        self.header = "</body>"
    def printh(self):
        return  self.header

class write_page:
    def __init__(self):
        self.page = """
        <table width=100% height=100%>
        <tr width=100% height=100%>
        <td width=100% height=100%>
        Bussiere<br>
        Python Programmer for hire2<br>
        web site : <a href="http://www.bussieresama.net">http://www.bussieresama.net</a><br>
        <img src="img/bussiere.jpg">
        </td>
        </tr>
        </table>
        """
class root:
    def __init__(self):
        pass
    nom = ""
    passwd = ""
    def doLogin(self, username=None, password=None): 
        self.nom = username
        self.passwd = password
        return self.page()
    def index(self,username=None,password=None):
        return self.page()
    
    
    index.exposed = True
    doLogin.exposed = True 
 
    
        
    def page(self):
        h1 = header_begin()
        h2 = header_end()
        pagewrite = write_page()
        page = pagewrite.page
        page = "%s %s %s %s %s" %(h1.printh(),page,self.nom,self.passwd,h2.printh())
        return page

cherrypy.config.update({'tools.staticdir.root':r'%s'%current_dir})   
cherrypy.config.update({'environment': 'production','log.screen': True})
cherrypy.config.update({'server.socket_port' : 664})
cherrypy.quickstart(root(),config=settings)
