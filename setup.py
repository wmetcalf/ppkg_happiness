from setuptools import setup, find_packages

setup(
    name="ppkg_happiness",
    version="0.1.0",
    description="PPKG Analyzer",
    author="Node5",
    packages=find_packages(),
    install_requires=[
        "python-magic",
        "beautifulsoup4",
        "xmltodict",
    ],
    entry_points={
        "console_scripts": [
            "ppkg-happiness=ppkg_happiness.__main__:main",
        ]    
    },
    python_requires=">=3.8",
)
