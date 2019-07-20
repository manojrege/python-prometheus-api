import  setuptools

setuptools.setup(
    name='python-prometheus-api',
    version='0.1.3',
    author='Manoj R. Rege',
    author_email='rege.manoj@gmail.com',
    url='https://github.com/manojrege/python-prometheus-api',
    description='A Python wrapper for Prometheus HTTP API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license=open('LICENSE').read(),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: BSD LICENSE",
    ],
    package_data = {'promapi': ['data/config.yml']},
    include_package_data = True,
)
