import sys
from pathlib import Path

# Let tests import the modules in the project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
