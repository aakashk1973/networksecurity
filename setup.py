from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    """
    requirement_list:List[str] = []
    try:
        with open('req.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. No requirements will be installed.")

    return requirement_list 

setup(
    name='Network Security',
    version='0.1.0',
    author='Aakash',
    packages=find_packages(),
    install_requires=get_requirements('req.txt')
)
