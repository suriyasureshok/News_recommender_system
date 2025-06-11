from setuptools import setup, find_packages
from src.utils import get_requirements

setup(
    name='News_Recommender_System',
    version='1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Suriya',
    author_email='suriyasureshkumarkannian@gmail.com'
)