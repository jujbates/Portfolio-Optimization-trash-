from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Generate an optimized portfolio from the current S&P 500 companies. To optimize a portfolio we want to maximize returns while minimizing the risk with respect to the amount of money we allocate on each asset in our portfolio. We want to think about index, sector, industry, and industry anti-correlation and covariance. Our portfolio will be measured in respect to the efficient frontier.',
    author='Justin Bates',
    license='MIT',
)
