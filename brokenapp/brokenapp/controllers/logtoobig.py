import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from brokenapp.lib.base import BaseController, render
import os

log = logging.getLogger(__name__)

class LogtoobigController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/logtoobig.mako')
        # or, return a string
        for i in range(1,100):
            log.info("log")
        c.size = os.path.getsize('access.log')
        log.info(c.size)
        return render('/log.mako')
