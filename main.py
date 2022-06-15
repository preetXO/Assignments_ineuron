import logging
logging.basicConfig(level=logging.DEBUG, filename='main.log', format='%(asctime)s - %(levelname)s - %(message)s')

def replace_string(file_path: str, old_string: str, new_string: str) -> None:
    """
    Replace a string in a file.
    param file_path: Path to file
    param old_string: String to replace
    param new_string: New string
    """
    logging.info(f'Replacing {old_string} with {new_string} in {file_path}')
    with open(file_path, 'r') as f:
        logging.info(f'Reading {file_path}')
        s = f.read()
        s = s.replace(old_string, new_string)
        with open(file_path, 'w') as f:
            logging.info('Writing to {file_path}')
            f.write(s)


if __name__ == "__main__":
    '''replace a string placement in example.txt to screening'''
    logging.info('calling replace_string')
    replace_string('example.txt', 'placement', 'screening') # replace placement to screening
    print('Done!')


