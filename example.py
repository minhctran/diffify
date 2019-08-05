#!/usr/bin/env python3
from diffify import diffify


# Make a diff file
diffify(
        # Path to the main file
        main_path='/Users/congminhc1/Research/papers/heating-power-law/main.tex',
        # old commit to be compared,
        old_ver='59367a7c0ba958944e53ee6a12750a5a59fc8e71',
        # [Optional] new commit, default value is 'master'
        new_ver='master'
        # [Optional] Make a pdf from the diff file. May throw an error if latexpdf is not properly setup
        # make_pdf=True,
        # [Optional] Clean all temp files. Keep only the diff PDF
        # clean_up=True,
        # [Optional] markup style for ADD changes, default = '{\\protect\\color{blue} #1}'
        # style_add='{\\protect\\color{blue} #1}',
        # [Optional] markup style for DEL changes, default = '{\\protect\\color{red} \\sout{#1}}'
        # style_del='{}'
        )










