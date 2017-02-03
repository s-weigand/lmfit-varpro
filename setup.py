from setuptools import setup

setup(
    name="lmfit-varpro",
    version="0.1.0",
    description='A variable projection implementation for Python/lmfit.',
    url='http://github.com/ThingiverseIO/pythingiverseio',
    author='Joris Snellenburg, Stefan Schuetz, Joern Weissenborn',
    author_email="""j.snellenburg@vu.nl,
                    YamiNoKeshin@gmail.com,
                    joern.weissenborn@gmail.com""",
    license='GPLv3',
    packages=['lmfit_varpro'],
    install_requires=[
        'numpy',
        'lmfit',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
