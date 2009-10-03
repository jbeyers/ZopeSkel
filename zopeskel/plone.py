import copy

from zopeskel.basic_zope import BasicZope
from zopeskel.base import get_var
from zopeskel.base import var

class Plone(BasicZope):
    _template_dir = 'templates/plone'
    summary = "A project for Plone products"
    help = """
This creates a Plone project (to create a Plone *site*, you probably
want to use the one of the templates for a buildout).

This template expects a name in the form 'Products.MyProduct' or 
'mycompany.myproject' (1 dot, a 'basic namespace'). To create a Plone
project with a name like 'plone.app.myproject' (2 dots, a 'nested
namespace'), use the 'plone_app' template. You cannot have a flat package 
name (no dots, 'myproduct').
"""
    required_templates = ['basic_namespace']
    use_local_commands = True
    use_cheetah = True
    vars = copy.deepcopy(BasicZope.vars)
    get_var(vars, 'namespace_package').default = 'plone'
    get_var(vars, 'package').default = 'example'
    get_var(vars, 'author').default = ''
    get_var(vars, 'author_email').default = ''
    get_var(vars, 'url').default = 'http://svn.plone.org/svn/plone/plone.example'


