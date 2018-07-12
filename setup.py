from setuptools import setup

setup(
    name="lmfit-varpro",
    version="0.1.0",
    description='A variable projection implementation for Python/lmfit.',
    url='https://github.com/glotaran/lmfit-varpro',
    author='Joris Snellenburg, '
           'Joern Weissenborn',
    author_email="""j.snellenburg@vu.nl,
                    joern.weissenborn@gmail.com""",
    license='GPLv3',
    packages=['lmfit_varpro'],
    install_requires=[
        'numpy',
        'lmfit',
    ],
    test_suite='tests',
    tests_require=['pytest'],
)
