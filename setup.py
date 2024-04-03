from setuptools import find_packages, setup

setup(
    name="mcqsgenrator",
    version="0.0.1",
    author="Bilal Ahmad Khan",
    author_email="",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages(),
)
