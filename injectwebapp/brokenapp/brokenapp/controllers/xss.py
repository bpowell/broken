import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from brokenapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class XssController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/xss.mako')
        # or, return a string
        response.set_cookie("SESSIONID", "ABCDEF123456789")
        return render('/xss.mako')

    def inject(self):
        response.headerlist.append( ("X-XSS-Protection", 0) )
        c.data = request.params['data']
        return render('/xssinject.mako')
