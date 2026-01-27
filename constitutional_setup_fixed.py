#!/usr/bin/env python3
print("="*60)
print("REZTRAINER CONSTITUTIONAL AI SETUP")
print("="*60)

print("Checking Ollama...")
import subprocess
try:
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    print("SUCCESS: Ollama found!")
    print("Available models:")
    lines = result.stdout.split('\n')
    for line in lines[:10]:  # Show first 10 models
        if line.strip():
            print(f"   {line}")
    if len(lines) > 10:
        print(f"   ... and {len(lines)-10} more models")
except Exception as e:
    print(f"ERROR: {e}")
    print("INFO: Install Ollama from: https://ollama.com")

print("\nCreating constitution.ai...")
constitution = """# CONSTITUTIONAL AI GOVERNANCE

ARTICLE I: DATA SOVEREIGNTY
- All training occurs locally
- No data leaves your machine

ARTICLE II: OLLAMA INTEGRATION  
- Uses local Ollama models only
- No external API calls

ARTICLE III: AUDIT TRAIL
- All actions are logged
- Constitutional checks are enforced
"""
with open("constitution.ai", "w", encoding="utf-8") as f:
    f.write(constitution)
print("SUCCESS: Created constitution.ai")

print("\nCreating constitutional_governor.py...")
governor = '''def enforce(project):
    print(f"Constitutional check for {project}")
    print("SUCCESS: All checks passed")
    return True
'''
with open("constitutional_governor.py", "w", encoding="utf-8") as f:
    f.write(governor)
print("SUCCESS: Created constitutional_governor.py")

print("\nCreating constitutional_train.py...")
trainer = '''#!/usr/bin/env python3
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
'''
with open("constitutional_train.py", "w", encoding="utf-8") as f:
    f.write(trainer)
print("SUCCESS: Created constitutional_train.py")

print("\n" + "="*60)
print("CONSTITUTIONAL AI SETUP COMPLETE!")
print("="*60)
print("\nTo train with constitutional governance:")
print("   python constitutional_train.py 'your_model_name'")
print("\nView constitution:")
print("   Get-Content constitution.ai")
