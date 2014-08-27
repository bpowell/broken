# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1409081585.826745
_enable_loop = True
_template_filename = '/home/user/p/brokenapp/brokenapp/templates/xssinject.mako'
_template_uri = '/xssinject.mako'
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
        __M_writer(u'<h1>What do we have here?</h1>\n<p>Someone forgot to sanitize their input!</p>\n<br /><hr />\n')
        # SOURCE LINE 4
        __M_writer(c.data )
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


