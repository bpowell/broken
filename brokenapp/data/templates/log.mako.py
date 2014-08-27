# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1409072978.280526
_enable_loop = True
_template_filename = '/home/user/p/brokenapp/brokenapp/templates/log.mako'
_template_uri = '/log.mako'
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
        __M_writer(u'<h1>Logging too much!</h1>\n<p>Size of log file: ')
        # SOURCE LINE 2
        __M_writer(escape(c.size))
        __M_writer(u' bytes</p>\n<p>Size of disk is: 10000000 bytes</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


