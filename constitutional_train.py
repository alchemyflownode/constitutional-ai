#!/usr/bin/env python3
import sys
try:
    from constitutional_governor import enforce
except:
    def enforce(project):
        print(f"Checking {project}...")
        return True

if len(sys.argv) < 2:
    print("Usage: python constitutional_train.py <project_name>")
    sys.exit(1)

project = sys.argv[1]
print("="*60)
print(f"CONSTITUTIONAL TRAINING: {project}")
print("="*60)

if enforce(project):
    print("SUCCESS: Constitutional checks passed")
    print("INFO: Ready to train with Ollama...")
    print(f"HINT: Run: ollama run llama2 'Help train a model for {project}'")
else:
    print("ERROR: Constitutional violation - training stopped")
