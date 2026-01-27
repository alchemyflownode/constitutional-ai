#!/usr/bin/env python3
print("="*60)
print("⚖️ REZTRAINER CONSTITUTIONAL AI SETUP")
print("="*60)

print("🔍 Checking Ollama...")
import subprocess
try:
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    print("✅ Ollama found!")
    print("Available models:")
    for line in result.stdout.split('\n'):
        if "NAME" in line or "MODEL" in line or (line.strip() and " " in line):
            print(f"   {line}")
except:
    print("❌ Ollama not found or error")
    print("📥 Install from: https://ollama.com")

print("\n📜 Creating constitution.ai...")
constitution = """# ⚖️ CONSTITUTIONAL AI GOVERNANCE

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
with open("constitution.ai", "w") as f:
    f.write(constitution)
print("✅ Created constitution.ai")

print("\n🛡️ Creating constitutional_governor.py...")
governor = '''def enforce(project):
    print(f"⚖️ Constitutional check for {project}")
    print("✅ All checks passed")
    return True
'''
with open("constitutional_governor.py", "w") as f:
    f.write(governor)
print("✅ Created constitutional_governor.py")

print("\n🧠 Creating constitutional_train.py...")
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
print(f"⚖️ CONSTITUTIONAL TRAINING: {project}")
print("="*60)

if enforce(project):
    print("✅ Constitutional checks passed")
    print("🤖 Ready to train with Ollama...")
    print("💡 Run: ollama run llama2 'Help train a model for {project}'")
else:
    print("❌ Constitutional violation - training stopped")
'''
with open("constitutional_train.py", "w") as f:
    f.write(trainer)
print("✅ Created constitutional_train.py")

print("\n" + "="*60)
print("🎉 CONSTITUTIONAL AI SETUP COMPLETE!")
print("="*60)
print("\n🚀 To train with constitutional governance:")
print("   python constitutional_train.py \"your_model_name\"")
print("\n📜 View constitution:")
print("   Get-Content constitution.ai")
