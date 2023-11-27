
import os
import subprocess

def create_project_structure():
    # Define project root directory
    project_root = "D:\Projects\DLproject1"
    
    # Step 1: Create main project directory
    os.makedirs(project_root, exist_ok=True)
    
    # Step 2: Create data directory and its files
    data_dir = os.path.join(project_root, "data")
    os.makedirs(data_dir, exist_ok=True)
    subprocess.run(["touch", os.path.join(data_dir, "example_data.txt")])

    # Step 3: Create model directory and its files
    model_dir = os.path.join(project_root, "model")
    os.makedirs(model_dir, exist_ok=True)
    subprocess.run(["touch", os.path.join(model_dir, "your_trained_model.h5")])

    # Step 4: Create src directory and its files
    src_dir = os.path.join(project_root, "src")
    os.makedirs(src_dir, exist_ok=True)

    # List of files to create in src directory
    src_files = ["__init__.py", "data_preprocessing.py", "train_model.py", "inference.py"]

    # Create files in src directory
    subprocess.run([f"touch {os.path.join(src_dir, file)}" for file in src_files])

    # Step 5: Create app directory and its files
    app_dir = os.path.join(project_root, "app")
    os.makedirs(app_dir, exist_ok=True)

    # List of files to create in app directory
    app_files = ["__init__.py", "routes.py"]

    # Create files in app directory
    subprocess.run([f"touch {os.path.join(app_dir, file)}" for file in app_files])

    # Step 6: Create templates and static directories within app
    os.makedirs(os.path.join(app_dir, "templates"), exist_ok=True)
    os.makedirs(os.path.join(app_dir, "static"), exist_ok=True)

    # Step 7: Create train_in_colab.ipynb file
    subprocess.run(["touch", os.path.join(project_root, "train_in_colab.ipynb")])

    # Step 8: Create requirements.txt file
    subprocess.run(["touch", os.path.join(project_root, "requirements.txt")])

    # Step 9: Create main.py file
    subprocess.run(["touch", os.path.join(project_root, "main.py")])

    print("Project structure created successfully.")

if __name__ == "__main__":
    create_project_structure()
