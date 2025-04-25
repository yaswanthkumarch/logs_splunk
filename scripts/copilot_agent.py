import os
import sys

def validate_inputs_conf(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return False

    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        valid = True
        in_section = False

        for i, line in enumerate(lines):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith('[') and line.endswith(']'):
                in_section = True
                continue
            elif '=' in line and in_section:
                continue
            else:
                print(f"[Line {i+1}] Invalid syntax: {line}")
                valid = False

        if valid:
            print("Copilot Agent: inputs.conf syntax is valid.")
        return valid

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "splunk-apps/my_app/default/inputs.conf"
    result = validate_inputs_conf(path)
    sys.exit(0 if result else 1)
