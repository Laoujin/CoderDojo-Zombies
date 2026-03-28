# Voor Coaches

## Installatie Stappen

- Python
   - Installatie: `winget install -e --id Python.Python.3.12`
      - Versie: `python --version`
   - Python staat niet in je PATH
      - Typisch: `C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\`
- VS Code
   - `winget install -e --id Microsoft.VisualStudioCode`
   - `Ctrl+Shift+P` → "Python: Select Interpreter" → Kies Python 3.12
   - Extensions, zie `.vscode/extensions.json`
- Python packages: `python -m pip install -r requirements.txt`
