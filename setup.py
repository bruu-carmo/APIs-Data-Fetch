from setuptools import setup, find_packages

setup(
    name="python-automation-framework",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
    ],
    author="Bruna Carmo",
    description="Framework de automação para coleta e análise de dados via APIs.",
    license="MIT",
)
