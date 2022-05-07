try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()


setup(
    name='geezswitch',
    version='1.0.0',
    description='Language Identification library.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Fitsum Gaim',
    author_email='fitsum@geezlab.com',
    url='https://github.com/fgaim/geezswitch',
    keywords='language identification',
    packages=['geezswitch', 'geezswitch.utils', 'geezswitch.tests'],
    include_package_data=True,
    install_requires=['six'],
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
