# musabeytekin.github.io

Personal site of Musa Beytekin, served by GitHub Pages at https://musabeytekin.github.io
(English at `/`, Turkish at `/tr/`).

The two pages are generated from one template:

```bash
python3 build.py
```

- `build.py`: the text of both languages (`PAGES`) and the page template. Standard library only.
- `assets/site.css`, `assets/site.js`: styles, and the script that plays the run line once.
- `cv/`: the CV files the pages link to.
- `index.html`, `tr/index.html`: generated; edit `build.py` instead and commit the result.
