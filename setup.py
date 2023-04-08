from setuptools import find_packages,setup
from typing import List


setup(
name='ProjectName',
version='0.0.1',
author='AuthorName',
author_email='AuthorEmail',
packages=find_packages(),
install_requires=['pandas', 'numpy', 'seaborn', 'matplotlib', 'scikit-learn', 'catboost', 'xgboost', 'dill', 'Flask']

)
