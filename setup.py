from setuptools import setup, find_packages


# NOTE: EnthoughtBase should *never* depend on another ETS project!  We need
# to fix the below ASAP!

# Function to convert simple ETS project names and versions to a requirements
# spec that works for both development builds and stable builds.  Allows
# a caller to specify a max version, which is intended to work along with
# Enthought's standard versioning scheme -- see the following write up:
#    https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers
def etsdep(p, min, max=None, literal=False):
    require = '%s >=%s.dev' % (p, min)
    if max is not None:
        if literal is False:
            require = '%s, <%s.a' % (require, max)
        else:
            require = '%s, <%s' % (require, max)
    return require


# Declare our ETS project dependencies.
ENVISAGECORE = etsdep('EnvisageCore', '3.0.0b1')  # -- all from logger.(plugin|agent|widget)
ENVISAGEPLUGINS = etsdep('EnvisagePlugins', '3.0.0b1')  # -- all from logger.plugin
TRAITS = etsdep('Traits', '3.0.0b1')
TRAITSBACKENDWX = etsdep('TraitsBackendWX', '3.0.0b1')  # -- only from e.util.traits.editor.parameter_choice_editor.py
TRAITSGUI = etsdep('TraitsGUI', '3.0.0b1')  # -- from logger.(agent|plugin|widget)
TRAITS_UI = etsdep('Traits[ui]', '3.0.0b1')

# The following "soft dependencies" are wrapped in try..except blocks
#APPTOOLS -- util/wx/drag_and_drop
#SCIMATH -- util/wx/spreadsheet/unit_renderer.py

setup(
    author = 'Enthought, Inc',
    author_email = 'info@enthought.com',
    dependency_links = [
        'http://code.enthought.com/enstaller/eggs/source',
        ],
    description = 'EnthoughtBase is the root project of all other ETS projects',
    extras_require = {
        'agent': [
            ENVISAGECORE,
            TRAITS,
            TRAITSGUI,
            ],
        'distribution': [
            TRAITS_UI,
            ],
        'envisage': [
            ENVISAGECORE,
            ENVISAGEPLUGINS,
            TRAITSGUI,
            TRAITS_UI,
            ],
        'traits': [
            TRAITS,
            TRAITSBACKENDWX,
            ],
        'ui': [    # -- this includes util.ui.* and util.wx.* (see extras.map)
            TRAITSGUI,
            TRAITS_UI,
            ],

        # All non-ets dependencies should be in this extra to ensure users can
        # decide whether to require them or not.
        'nonets': [
            ],
        },
    license = 'BSD',
    include_package_data = True,
    install_requires = [
        ],
    name = 'EnthoughtBase',
    namespace_packages = [
        "enthought",
        ],
    packages = find_packages(),
    tests_require = [
        'nose >= 0.9',
        ],
    test_suite = 'test_all',
    url = 'http://code.enthought.com/ets',
    version = '3.0.0b1',
    zip_safe = False,
    )

