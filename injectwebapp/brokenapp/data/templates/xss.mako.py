# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1409082405.888042
_enable_loop = True
_template_filename = '/home/user/p/brokenapp/brokenapp/templates/xss.mako'
_template_uri = '/xss.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<h1>XSS</h1>\n<p>Do evil things</p>\n<form name="test" method="post" action="/xss/inject">\nPayload: <input type="text" name="data" />\n<input type="submit" name="submit" value="Submit" />\n</form>\nClick <a href="/xss/inject?data=<script>alert(document.cookie)</script>">here</a> for more evil!\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


