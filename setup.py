from setuptools import find_packages, setup
from typing import List

def requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements,
    ignoring the '-e .' line which is only for pip.
    '''
    HYPHEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='ml-project',
    version='0.0.1',
    author='APOORV',
    author_email='apoorvbirthada@gmail.com',
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
)
