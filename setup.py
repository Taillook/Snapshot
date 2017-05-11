from setuptools import setup, find_packages

setup(
    name='snapshot',
    version='1.0.1',
    packages=find_packages(),
    install_requires=['cliff'],
    entry_points={
        'console_scripts':
            'snapshot = snapshot.main:main'
    },
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS Sierra',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6.0',
    ],
)
