from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='multi_file_converter',
  version='1.0.9',
  author='dake_duck',
  author_email='arsengabdulin228@gmail.com',
  description='Simple way to convert files to another formats',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/DAKExDUCK/FileConverter',
  packages=find_packages(),
  install_requires=['Pillow>=10.0.0'],
  classifiers=[
    'Programming Language :: Python :: 3.10',
    'Operating System :: POSIX :: Linux'
  ],
  keywords='',
  project_urls={
    'GitHub': 'https://github.com/DAKExDUCK/FileConverter'
  },
  python_requires='>=3.10'
)
