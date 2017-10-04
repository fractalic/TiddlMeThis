TiddlMeThis
====================

Scripts to download files and convert them into tiddler-importable objects
--------------------

# How do I use this?
1. Configure `file_props.json` to list the urls to the files you would like to
download, along with the tiddler properties you would like to generate for them.
1. Run pull_files.py in python3
    1. `python3 pull_files.py`
1. Import the files into your tiddlywiki. Copy the `importables` folder
to the directory of your tiddlywiki, then run
    1. `xargs tiddlywiki --load < importables/_importables`

