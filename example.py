#!/usr/bin/env python3
from diffify import diffify


# Make a diff file
diffify(
        # Path to the main file
        main_path='example/main.tex',
        # old commit to be compared,
        old_ver='4a9379f25c69ce2a0879f76198f3d78239e3fd30',
        # [Optional] new commit, default value is 'master'
        new_ver='master',
        # [Optional] Make a pdf from the diff file. May throw an error if latexpdf is not properly setup
        make_pdf=True,
        # [Optional] Clean all temp files. Keep only the diff PDF
        clean_up=True,
        # [Optional] markup style for ADD changes
        style_add='{\\protect\\color{blue} #1}',
        # [Optional] markup style for DEL changes
        style_del='{\\protect\\color{red} \\sout{#1}}')










