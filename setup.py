from setuptools import setup

setup(
    name="Lab2_module",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A single-file installable Python script",
    long_description_content_type="text/markdown",
    py_modules=["Lab2   "],  
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn"
    ],
    python_requires=">=3.8",
)
