# Importing necessary functions from setuptools package
# setuptools is the standard tool for packaging Python projects
from setuptools import find_packages, setup

# Constant for editable install flag ('-e .') that appears in requirements.txt
# This flag indicates the package should be installed in "editable" or "development" mode
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''
    This function reads a requirements file and returns a list of requirements
    
    Parameters:
        file_path (str): Path to the requirements file (typically 'requirements.txt')
    
    Returns:
        list: Cleaned list of package requirements without newlines or editable install flag
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines from requirements file
        requirements = file_obj.readlines()
        # Remove newline characters from each requirement
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove the editable install flag (-e .) if present
        # This is needed because '-e .' is not an actual package dependency
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

# The setup() function is the core of the file - it defines your package
setup(
    # Basic package metadata
    name='ML Project',          # Name of your package
    version='0.0.1',            # Current version (using semantic versioning)
    author='pranav',            # Author name
    
    # Automatically find all Python packages in your project
    # A package is any directory with __init__.py file
    packages=find_packages(),
    
    # List of package dependencies that pip will install automatically
    # Uses our get_requirements() function to read from requirements.txt
    install_requires=get_requirements('requirements.txt')
)