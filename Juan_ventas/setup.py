from setuptools import setup


setup(
    name='jv',
    version='0.1',
    py_modules=['jv'],
    install_requires=['Click',],
    entry_points='''
        [console_scripts]
        jv=jv:cli
        ''',
)
