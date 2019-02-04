Script that converts Dashlane JSON exported data to CSV data that's compatible with 1Password's import function.

*Currently it's Python 2.7, but it shouldn't be hard to make it 3+ friendly.*

## Instructions
- In Dashlane, go to `File > Export > Unsecured archive (readable) in JSON format`
- Enter your master password if you need to
- Find the exported JSON file, and run the following:

```
python dashlane-to-1password.py DashlaneExport.json
```

A file `output.csv` will be created in the current directory, use that in the 1Password import function.

**I'd recommend deleting all of the files once you're done and clearing any backups/recyle bins.**