from setuptools import setup, find_packages

setup(
    name='imageprocessing',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'scikit-image',
    ],
    author='Dakota',
    author_email='schang2@olin.edu',
    description='A simple Laplacian-over-Gaussian image processing package for edge detection.',
    keywords='Laplacian-over-Gaussian image processing edge detection',
    url='https://github.com/dcoder0111/QEA2_LaplacianOverGaussianOperator',
)