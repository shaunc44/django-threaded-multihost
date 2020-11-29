import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

# version = __import__('threaded_multihost_3').__version__

setup(
    name = 'django-threaded-multihost-3',
    version = '3.0',
    description = "Django Threaded Multihost 3",
    long_description = """django-threaded multihost provides support utilities to
    enable easy multi-site awareness in Django apps.""",
    author = 'Shaun Cox',
    author_email = 'shauncox44@gmail.com',
    url = 'https://github.com/shaunc44/django-threaded-multihost-3',
    license = 'MIT License',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'Framework :: Django :: 1.11'],
    packages = ['threaded_multihost_3'],
    include_package_data = False,
    zip_safe=False,
)
