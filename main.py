import sys
import platform
import docker

def check_environment():
    print (f"Python version: {sys.version}")
    print (f"OS {platform.system()} {platform.release()}")

    try:
        client = docker.from_env()
        client.ping()
        print ("Docker daemon is running")
    except Exception as e:
        print (f"Docker error: {e}")

if __name__ == "__main__":
    check_environment()
    