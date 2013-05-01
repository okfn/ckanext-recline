from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-recline',
    version=version,
    description="A CKAN preview extension to preview tabular data using recline",
    long_description="""\
    """,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='ckan, recline, preview',
    author='Dominik Moritz',
    author_email='',
    url='',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.recline'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points=\
    """
    [ckan.plugins]
    recline_preview=ckanext.recline.plugin:ReclinePreview
    """,
)
