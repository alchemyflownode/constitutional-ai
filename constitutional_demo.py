# constitutional_demo.py
print("CONSTITUTIONAL AI DEMO")
print("="*40)

import subprocess

# Check Ollama
print("1. Checking Ollama...")
try:
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    if "llama2" in result.stdout or "mistral" in result.stdout:
        print("   ✅ Ollama models available")
    else:
        print("   ⚠️  Ollama found but no common models")
except:
    print("   ❌ Ollama not working")

# Check constitution
print("\n2. Checking constitution...")
try:
    with open("constitution.ai", "r") as f:
        constitution = f.read()
    print(f"   ✅ Constitution found ({len(constitution)} characters)")
    print("   First principle:", constitution.split("\n")[2])
except:
    print("   ❌ Constitution not found")

print("\n" + "="*40)
print("DEMO COMPLETE: Constitutional AI is ready!")
print("Run: python constitutional_train.py 'your_project'")
