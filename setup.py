from setuptools import setup

setup(
    name='imagemagickCommandBuilder',
    version='0.0.1a0',
    packages=['ImagemagickDriver'],
    scripts=['scripts/dummy.py'],
    test_suite="tests",
    tests_require=['pytest'],
    data_files=[
        ('settings', ['settings/settings.ini']),
                ],
    zip_safe=False,
    url='',
    license='',
    author='Henry Borchers',
    author_email='hborcher@illinois.edu',
    description='Command builder for Imagemagick 6'
)
