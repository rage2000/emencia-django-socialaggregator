import os
from setuptools import setup


setup(name='emencia-django-socialaggregator',
      version=__import__('socialaggregator').__version__,
      description='Django app for aggregate some feeds from social networks.',
      long_description="%s\n%s" % (open('README.rst').read(),
                       open(os.path.join('docs', 'HISTORY.txt')).read()),
      keywords='django, emencia, social networks, aggregation',
      classifiers=[
          'Framework :: Django',
          'Programming Language :: Python',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Development Status :: 2 - Pre-Alpha',
          'Topic :: Software Development :: Libraries :: Python Modules'],
      author=__import__('socialaggregator').__author__,
      author_email=__import__('socialaggregator').__email__,
      url=__import__('socialaggregator').__url__,
      license=__import__('socialaggregator').__license__,
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'django-taggit',
                        'twitter',
                        'python-instagram',
                        'facebook-sdk',
                        'feedparser',
                        'google-api-python-client',
                        'django'])
