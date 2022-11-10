from distutils.core import setup

setup(
    name='google-sheets-reader',
    version='1.0',
    packages=['google_sheets_reader',
              'google_sheets_reader.src'],
    package_dir={'src': 'test'},
    url='https://github.com/JesseLeung97/steins-progress-logger',
    license='MIT',
    author='JesseLeung97',
    author_email='jesse@steins.co.jp',
    description='An automated progress logger for google sheets and slack.'
)