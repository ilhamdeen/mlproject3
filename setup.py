from setuptools import find_packages,setup
from typing import List

HYPEN_E_DON='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DON in requirements: 
            requirements.remove(HYPEN_E_DON)

    return requirements

setup(
name = "mlproject3",
version="0.0.1",
author= "krish",
author_email="deenilham@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)