# CLIENT API

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='whoz_api',
      version='0.1',
      description='Query gene annotations',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='gene annotate annotation ensembl',
      url='https://github.com/churchill-lab/whoz_api',
      author='Matt Vincent',
      author_email='matt.vincent@jax.org',
      license='MIT',
      #packages=['whoz'],
      packages=find_packages(),
      install_requires=[
          'markdown',
      ],
      #test_suite='nose.collector',
      #tests_require=['nose', 'nose-cover3'],
      #entry_points={
      #    'console_scripts': ['funniest-joke=funniest.command_line:main'],
      #},
      entry_points={
          'console_scripts': ['whoz-server=whoz_api.command_line:main'],
      },

      include_package_data=True,
      zip_safe=False)
