
this addon will list the related files with current file.


you could config the command with hotkeys like :


    {
        "keys": ["ctrl+i"],
        "command": "related_file_list",
        "args":
        {
            "suggests": ["Store", "Controller", "Test", ".react"]
        }
    }


words in the suggests list will be ignored