import logging
import sqlite3

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import jsonify

from brokenapp.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SqlinjectionController(BaseController):

    def index(self):
        conn = sqlite3.connect('broken.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists email (address text)''')
        conn.commit()
        return render('/sql.mako')

    def inject(self):
        c.email = request.params['email']
        conn = sqlite3.connect('broken.db')
        x = conn.cursor()
        c.r = x.executescript(''' insert into email (address) VALUES( "''' + c.email + '''")''').fetchall()
        conn.commit()
        return render('/sqlinject.mako')

    @jsonify
    def display(self):
        conn = sqlite3.connect('broken.db')
        c = conn.cursor()
        d = {}
        i = 0
        for row in c.execute('SELECT * FROM email'):
            d[str(i)] = row
            i = i +1

        return d

