from typing import List

def get_requirements(file_path:str):
    """
    Returns a list of requirements from a file path.
    """
    requirements = []
    with open (file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [rq.replace("\n","") for rq in requirements]

        requirements.remove("-e .")

        return requirements