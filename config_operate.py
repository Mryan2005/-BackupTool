from configparser import ConfigParser

def main():
    # 初始化类
    cp = ConfigParser()
    cp.read("default.cfg")
    # main
    if a_float == 'null':
        git = input()
        config_raw.set('Section', 'git_poth', git)
        a_float = config_raw.getfloat('Section', 'git_poth')
    else:
        a_float = config_raw.getfloat('Section', 'git_poth')