import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lmfit-varpro",
    version="0.0.1",
    description='A variable projection implementation for Python/lmfit.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/glotaran/lmfit-varpro',
    download_url = 'https://github.com/glotaran/lmfit-varpro/archive/0.0.1.tar.gz',
    keywords = ['alpha'],
    author='Joris Snellenburg, '
           'Joern Weissenborn',
    author_email="""j.snellenburg@gmail.com,
                    joern.weissenborn@gmail.com""",
    license='GPLv3',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
	],
    install_requires=[
        'numpy',
        'lmfit',
    ],
    test_suite='tests',
    tests_require=['pytest'],
)
