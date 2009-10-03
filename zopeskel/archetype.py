import os
import copy

from zopeskel.plone import Plone
from zopeskel.base import get_var
from zopeskel.base import var, EASY, EXPERT
from zopeskel.vars import StringVar

class Archetype(Plone):
    _template_dir = 'templates/archetype'
    summary = 'A Plone project that uses Archetypes content types'
    help = """
This creates a Plone project that uses Archetypes content types.
It has local commands that will allow you to add content types
and to add fields to your new content types.

This template expects a name in the form 'Products.MyProduct'
or 'mycompany.myproduct' (a 'basic namespace'); you cannot have
a flat package name ('myproduct') or a nested namespace
('collective.company.product').
"""

    required_templates = ['plone']
    use_cheetah = True
    use_local_commands = True

    vars = copy.deepcopy(Plone.vars)
    vars.insert(0, StringVar(
        'title',
        title='Project Title',
        description='Title of the project',
        modes=(EASY, EXPERT),
        default='Example Name',
        help="""
This becomes the title of the project. It is used in the 
GenericSetup registration for the project and, as such, appears
in Plone's Add/Remove products form.
"""
       )
       )

    #zope2product should always defaults to True
    get_var(vars, 'zope2product').default = True

    def post(self, command, output_dir, vars):
        # Remove tests.py -- we already have a tests/ package
        path = os.path.join(output_dir,
                            vars['namespace_package'],
                            vars['package'])
        os.remove(os.path.join(path, 'tests.py'))

        super(Archetype, self).post(command, output_dir, vars)
