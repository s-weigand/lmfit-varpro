import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()



setuptools.setup(
    name="lmfit-varpro",
    version="version='0.0.2'",
    description='A variable projection implementation for Python/lmfit.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/glotaran/lmfit-varpro',
    download_url = 'https://github.com/glotaran/lmfit-varpro/tarball/master',
    keywords = ['alpha'],
    author='Joris Snellenburg, '
           'Joern Weissenborn',
    author_email="""j.snellenburg@gmail.com,
                    joern.weissenborn@gmail.com""",
    license='GPLv3',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Chemistry',
	],
    install_requires=[
        'numpy',
        'lmfit'
    ],
    test_suite='tests',
    tests_require=['pytest'],
)
