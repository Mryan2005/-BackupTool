import subprocess
sh = r'.\push.sh'
def main():
    child = subprocess.Popen(sh,shell=True)
    child.wait()

if __name__ == "__main__":
    main()