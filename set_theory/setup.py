from setuptools import setup, find_packages
setup(
    name = 'set_theory',
    version = '0.0.1',
    description = 'Basic set theory operations',
    author = 'David Ochoa',
    author_email = 'device.mxl@gmail.com',
    license = 'CC BY-NC-SA 4.0'
    url = 'https://github.com/devicemxl/Maths-Bytes/set_theory/',
    download_url = 'https://github.com/devicemxl/Maths-Bytes/set_theory/SetTheory/archive/0.0.1.tar.gz',
    keywords = ['set theory', 'set'],
    classifiers = [ # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    platforms=['Platform Independent'],
    packages=find_packages(),
    #install_requires=['numpy', 'matplotlib', 'matplotlib-venn', 'wordcloud'],
)
