from setuptools import setup

setup(
    name="montecarlo",
    version='1.0.0',
    author="Tara Haas",
    packages=["montecarlo.py","montecarlo_demo.ipynb","montecarlo_tests.py"],
    url="https://github.com/taramh/montecarlo",
    license='LICENSE.txt',
    description="A Monte Carlo Simulator and test files.",
    long_description= open('README.md').read(),
    install_requires= ["random","pandas","unittest","pandas.testing","matplotlib.pyplot"]
)