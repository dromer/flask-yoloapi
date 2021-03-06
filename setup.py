import os
from setuptools import setup, find_packages


version = '0.0.9'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read()
setup(
    name='Flask-YoloAPI',
    version=version,
    description='Simply the best Flask API library',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2'
    ],
    keywords='flask api flapi yoloapi',
    author='Sander Ferdinand',
    author_email='sa.ferdinand@gmail.com',
    url='https://github.com/skftn/flask-yoloapi',
    install_requires=[
        'flask',
        'python-dateutil'
    ],
    extra_requires=[
        'pytest'
    ],
    download_url=
        'https://github.com/skftn/flask-yoloapi/archive/master.zip',
    packages=find_packages(),
    include_package_data=True,
)
