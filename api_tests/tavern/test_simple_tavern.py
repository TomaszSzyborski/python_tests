from tavern.core import run

success = run("test_simple.tavern.yaml", {})

if not success:
    print("Error running tests")