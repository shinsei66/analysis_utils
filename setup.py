from setuptools import setup, find_packages


install_requires = [
    'pandas'
]



console_scripts = [
    
]


setup(
    name='analysis_utils',
    description='Python Data Analysis Utilities',
    author='shinsei66',
    # author_email='XXS@XXXX.net',
    url='https://github.com/shinsei66',
    version='0.0.0',
    packages=find_packages,
    install_requires=install_requires,
    license='MIT',
    entry_points={'console_scripts': console_scripts},
)