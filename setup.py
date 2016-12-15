from setuptools import setup

setup(
    name='imagemagickDriver',
    version='0.0.1a0',
    packages=['ImagemagickDriver'],
    scripts=['scripts/dummy.py'],
    test_suite="tests",
    tests_require=['pytest'],
    data_files=[
        ('settings', ['settings/imdsettings.ini']),
                ],
    zip_safe=False,
    url='',
    license='',
    author='Henry Borchers',
    author_email='hborcher@illinois.edu',
    description='wrapper around Imagemagick 6'
)
