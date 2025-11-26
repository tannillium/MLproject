from setuptools import find_packages,setup
from typing import List

MINUS_E_DOT = '-e.'
def get_requirements(file_path:str)->list[str]:

    # gives the list of requirements(libraries)
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        # removing that -e. from our list of requirements
        if MINUS_E_DOT in requirements:
            requirements.remove(MINUS_E_DOT)
    return requirements

setup(
    name='MLproject',
    version='0.0.1',
    author='Tannillium',
    author_email='jaintanishq0709@gmail.com',
    packages=find_packages(),
    # install_requirements=['pandas','numpy','seaborn'] 
    install_requires=get_requirements('requirements.txt')
)