import logging

from subprocess import call
import os
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from brokenapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ShellinjectionController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/shellinjection.mako')
        # or, return a string
        (child_stdin, child_stdout) = os.popen2("ls tmp", 'r', 10000)
        c.out = child_stdout.readlines()
        return render('/shell.mako')

    def inject(self):
        c.name = request.params['filename']
        (child_stdin, child_stdout) = os.popen2("cat ./tmp/" + c.name, 'r', 10000)
        return child_stdout
