from setuptools import setup, find_packages

setup(
    name='CCRE_Card_Unique_ID_Exporter',
    version='0.0.3',
    packages=find_packages(),
    author='taxi-tabby',
    author_email='rkdmf0000@gmail.com',
    description='A simple Card Unique ID Exporter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/taxi-tabby/CCRE_Card_Unique_ID_Exporter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pyscard', 
    ],
    extras_require={
        'dev': ['check-manifest'],
    },
    license='MIT',  
)
