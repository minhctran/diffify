# diffify
Flatten and make a LaTeX diff file between the most recent git commit, i.e. `master`, and an older commit.

## Installation
Simply download everything. For a quick start, check out `example.py`.

## Prerequisites 
We use `latexdiff` to generate the diff file. For instructions on how to install and use `latexdiff`, see [here](https://www.overleaf.com/learn/latex/Articles/Using_Latexdiff_For_Marking_Changes_To_Tex_Documents).

**Tip:** If you have trouble with installing or using `latexdiff`, the script also generates flattened versions of the TeX files. Set `clean_up = False` (See `example.py`) to keep these files, then use an online tool, such as [this one](https://3142.nl/latex-diff/), to generate the diff file. 

**Tip:** You will also need `pdflatex` and `bibtex` to compile the PDF of the diff file. You probably have them already. But if for some reason they are not working properly, simply set `clean_up = False` to keep the `.tex` file, then use a different method to generate the PDF.

## Usage

First, import `diffify()` from `diffify.py`:
```
from diffify import diffify
```
Set the path to the main `.tex` file and the old commit to be compared with `master`:
```
main_path = 'example/main.tex' # Path to the main file
old_ver = '4a9379f25c69ce2a0879f76198f3d78239e3fd30' # previous commit to be compared with master
```
Call `diffify()` to make the diff file: 
```
diffify(
        main_path,
        old_ver,
        new_ver = 'master'      # Can change 'master' to a different commit
        make_pdf = True,        # Make a pdf from the diff file. May throw an error if latexpdf is not properly setup
        clean_up = True)        # Clean the temp LaTeX files. Keep only the diff PDF
```
**Tip:** You can also use ``diffify`` to flatten the TeX files by simply setting `old_ver` to any commit, e.g. `master`, and `clean_up = False` to keep the flattened files.

## Recent changes: 

* Can customize the diff markup, e.g. color, strikeout, etc. See `example.py` for more details  
* Can change 'master' to a different commit.
* Add an option to remove comments from the flattened file. Should be used with care.
