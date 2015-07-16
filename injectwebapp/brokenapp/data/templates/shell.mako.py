# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1409152340.401266
_enable_loop = True
_template_filename = '/home/user/p/brokenapp/brokenapp/templates/shell.mako'
_template_uri = '/shell.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<h1>Shell Injection</h1>\n<p>Give the file you wish to cat</p>\n<p>List of files:</p>\n<p>')
        # SOURCE LINE 4
        __M_writer(escape(c.out))
        __M_writer(u'</p>\n<form name="test" method="post" action="/shellinjection/inject">\nFilename: <input type="text" name="filename" />\n<input type="submit" name="submit" value="Submit" />\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


