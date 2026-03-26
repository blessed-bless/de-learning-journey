import sys
import platform
import subprocess
import shutil
from pathlib import Path

def check_python():
    # Check Python version
    version = sys.version_info
    print (f"python {version}")
    return version

def check_os():
    # Check operating system
    os_name = platform.system()
    os_release = platform.release()
    print (f"os {os_name} {os_release}")
    return f"{os_name} {os_release}"
def check_git():
    # Check if Git is installed
    git_path = shutil.which('git')
    if git_path:
        result = subprocess.run([git_path, '--version'], capture_output=True, text=True)
        print (f"Git: {result.stdout.strip()}")
        return True
    else:
        print("Git is not installed.")
        return False

def check_docker():
    # Check if Docker is installed
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
        print (f"Docker: {result.stdout.strip()}")
        return True
    except:
        print("Docker is not installed.")
        return False

def check_venv():
    # Check if virtualenv is installed
    venv_path = Path("./venv")
    if venv_path.exists():
        print (f"venv: {venv_path.resolve()}")
        return True
    else:
        print("venv is not found.")
        return False

def generate_report():
    # Generate a report of the environment
    print ("\n" + "=" * 50)
    print ("database engineer environment check")
    print ("=" * 50 + "\n")

    results = {
        "python": check_python(),
        "os": check_os(),
        "git": check_git(),
        "docker": check_docker(),
        "venv": check_venv()
    }

    print ("\n" + "=" * 50)
    success = all([
        results["git"],
        results["docker"],
        results["venv"]
    ])

    if success:
        print("All installations are successful. Your environment is ready for database engineering!")
    else:
        print("Some installations are missing. Please review the report above and install the necessary tools.")
        print("=" * 50 + "\n")

    return results

if __name__ == "__main__":
    generate_report()