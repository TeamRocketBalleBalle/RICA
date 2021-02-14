import sys
import os
from pathlib import Path
current_path = Path(os.getcwd())
sys.path.append(str(current_path.parent))

try:
    from Back_End import create_app
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)
    print("Are you sure you are running this file from `RICA/Back_End` directory?")
    print("Try running `flask run` in Back_End.")
    quit()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
