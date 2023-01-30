# Python Teaching 2023

The repository consist of two main folders: 

- notebooks: This is where exercise notebooks are stored. 
- utils_package: This is where the utility python package 'emo_utils' is stored. 

I think the simplest way is to git clone (with SSH) the repository to a local (but synced) Google Drives folder. 

Then a notebook can be shared as a file from that drive, like with this link: 

1. [Notebook Test](https://drive.google.com/file/d/1-VWiSR_FJ-cxP_rIImIG-3qMblO1k4D1/view?usp=sharing)

Theres two scenarios when clicking this link: 

1. As the owner of the file.
2. As anyone else.

*In scenario 1*: I can edit the file and the changes are automatically synced to my Google Drive including to my local Google Drive installation. So that means git will see those changes and they can be pushed to this repo. 

*In scenario 2*: Others don't have write permission so they need to make a copy in their own Google Drive (File -> Save a copy in Drive). 

To make developing the exercise notebooks easier I have added a script 'clean_notebooks.py' does the following: 

1. Find all notebooks that have '_working' in their name. 
2. Saves a copy with output cells removed with '_working' removed from the name (test_notebook_working.ipynb --> test_notebook.ipynb)

