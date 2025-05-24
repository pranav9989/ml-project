from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''
    This function will return the list of requirements
    '''
    reuirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='pranav',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)