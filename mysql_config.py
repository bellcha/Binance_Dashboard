from configparser import ConfigParser

def read_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        items = parser.items(section)
        db = {item[0]:item[1] for item in items}
    
    else:
        raise Exception(f'{section} not found in {filename}')

    return db

if __name__ == '__main__':
    print(read_config())