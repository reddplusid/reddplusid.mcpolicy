from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='reddplusid.mcpolicy',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Inigo Consulting',
      author_email='team@inigo-tech.com',
      url='http://github.com/inigoconsulting/',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['reddplusid'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'plone.app.dexterity',
        'plone.namedfile [blobs]',
        'collective.grok',
        'reddplusid.mission',
        'reddplusid.missionreport',
        'reddplusid.mctheme',
        'reddplusid.attachments',
          # -*- Extra requirements: -*-
        'eea.facetednavigation',
        'Solgema.fullcalendar',
        'Products.ContentWellPortlets',
        'Products.feedfeeder',
	'Products.PloneKeywordManager',
        'collective.contentleadimage',
        'collective.documentviewer',
        'collective.carousel',
        'collective.plonetruegallery',
        'collective.flowplayer',
        'collective.quickupload',
        'collective.portlet.usertrack',
        'collective.externaleditor',
    	'plone.app.changeownership',
        'reddplusid.registration',
        'reddplusid.locales',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins=["templer.localcommands"],
)
