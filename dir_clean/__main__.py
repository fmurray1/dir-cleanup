import click
from pathlib import Path


@click.Argument("dir", help="The directory to clean", type=click.Path(file_okay=False, exists=True))
@click.option("--upper_first", "-u", help="Set the first letter of each directory to an uppercase letter", is_flag=True, default=False)
def main(dir: click.Path, upper_first: bool):
    """This is a windows utility to combine folder structures into like names 
        Currently if the sub_path is a directory and there exists a directory that has the first 
        lowercase or uppercase letter (user defined default lower) and there is another matching name that differs 
        it will combine the two directories into the user specified format.

        To-Do: Find mispelled directories (maybe prompt the user if confidence is below ?90%?)
    """
    print(f"Test: {dir}")
    
    
    
    with Path(dir.name) as parent_path:
        for sub_path in parent_path.iterdir():
            if not sub_path.is_dir():
                continue
    
            


