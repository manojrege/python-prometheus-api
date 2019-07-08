from distutils.core import setup

setup(
    name='python-prometheus-api',
    version='0.1',
    author='Manoj R. Rege',
    author_email='rege.manoj@gmail.com',
    url='https://github.com/manojrege/python-prometheus-api',
    description='A Python wrapper for Prometheus HTTP API',
    long_description=open('README.md').read(),
    license=open('LICENSE').read(),
    packages=[
        'promapi'
    ],
)
