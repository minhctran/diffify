#!/usr/bin/env python3
from diffify import diffify


# Make a diff file
diffify(
        main_path='example/main.tex',                           # Path to the main file
        old_ver='4a9379f25c69ce2a0879f76198f3d78239e3fd30',     # old commit to be compared,
        new_ver='master',                                       # [Optional] new commit, default value is 'master'
        make_pdf=True,                                          # Make a pdf from the diff file.
                                                                # May throw an error if latexpdf is not properly setup
        clean_up=False)                                          # Clean the temp LaTeX files. Keep only the diff PDF










