#!/usr/bin/env python3
from diffify import diffify
import os
# For the purpose of this example, we need the path to where the script is running
script_path = os.path.dirname(os.path.abspath(__file__))
# Make a diff file
diffify(
        # Full path to the main file
        main_path= script_path + '/example/main.tex',
        # old commit to be compared,
        old_ver='4a9379f25c69ce2a0879f76198f3d78239e3fd30',
        # [Optional] new commit, default value is 'master'
        new_ver='master',
        # [Optional] Make a pdf from the diff file. May throw an error if latexpdf is not properly setup
        # make_pdf=True,
        # [Optional] Clean all temp files. Keep only the diff PDF
        clean_up=False,
        # [Optional] markup style for ADD changes, default = '{\\protect\\color{blue} #1}'
        # style_add='{\\protect\\color{blue} #1}',
        # [Optional] markup style for DEL changes, default = '{\\protect\\color{red} \\sout{#1}}'
        # style_del='{}'
        )










