from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='userpass',
    version='0.1',
    description='Generate a username (access_key) and password (secret_key).',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Passwords ',
    ],
    keywords='userpass generate username password secret_key',
    url='http://github.com/Rylaney/userpass',
    author='Ryan Laney',
    author_email='ryanlaney [at] teus [dot] media',
    license='Apache 2.0',
    packages=['userpass'],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
    entry_points={
        'console_scripts': ['userpass=userpass.command_line:main'],
    },
    include_package_data=True,
    zip_safe=False)
