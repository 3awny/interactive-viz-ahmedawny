import os
import subprocess
import sys
import venv

def create_virtual_environment(env_dir, python_executable):
    """Create a virtual environment using the specified Python executable."""
    if not os.path.exists(env_dir):
        print(f"Creating a virtual environment with {python_executable}...")
        subprocess.check_call([python_executable, '-m', 'venv', env_dir])
    else:
        print("Virtual environment already exists.")

def install_dependencies(env_dir):
    """Install dependencies from requirements.txt."""
    print("Installing dependencies from requirements.txt...")
    pip_executable = os.path.join(env_dir, 'bin' if os.name != 'nt' else 'Scripts', 'pip')
    subprocess.check_call([pip_executable, 'install', '-r', 'requirements.txt'])

def run_application(env_dir):
    """Run the application."""
    print("Running the application...")
    python_executable = os.path.join(env_dir, 'bin' if os.name != 'nt' else 'Scripts', 'python')
    subprocess.check_call([python_executable, 'app.py'])

def main():
    env_dir = os.path.join(os.getcwd(), 'venv')
    
    # Check for Python 3.10 or 3.11
    python_executable = None
    for version in ['3.10', '3.11']:
        try:
            subprocess.check_call([f'python{version}', '--version'])
            python_executable = f'python{version}'
            break
        except subprocess.CalledProcessError:
            continue

    if not python_executable:
        print("Error: This script requires Python 3.10 or 3.11.")
        sys.exit(1)

    create_virtual_environment(env_dir, python_executable)
    install_dependencies(env_dir)
    run_application(env_dir)
    print("Setup complete. The application is running at http://localhost:8080")

if __name__ == "__main__":
    main()
