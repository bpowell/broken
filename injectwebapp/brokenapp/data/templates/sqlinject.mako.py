# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1409071410.318576
_enable_loop = True
_template_filename = '/home/user/p/brokenapp/brokenapp/templates/sqlinject.mako'
_template_uri = '/sqlinject.mako'
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
        __M_writer(u'<h1>We Injected data!</h1>\n<p>your email address is ')
        # SOURCE LINE 2
        __M_writer(escape(c.email))
        __M_writer(u'</p>\n')
        # SOURCE LINE 3
        __M_writer(escape(c.r))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


