# 0 Preliminary Requirements for BIST Python Bootcamp  
  
Welcome to the BIST Python Bootcamp! So, what do we hope to achieve? We aim to provide you with the extremely powerful tool of programming languages for data analysis without any previous experience requirements.  

Programming languages allow us to analyse much larger datasets with a broader toolkit in terms of numerical anaysis and data visualisation that what we obtain with spreadsheets like Microsoft Excel or Google Sheets. For those who are not familiar either with programming or python, even though it may be slower at the beginning, as we become more profficient in with it, it is much easier and faster to work with data this way. Hopefully, by the end of this bootcamp, you will have a firm grasp of programming in Python, with a clear idea of how ot use it for data analysis and visualisation. Going forward, you should have a strong grounding in programming and might wish to develop skills in data mining or computational modelling - useful skills for science and other careers. 

Beyond providing you with specific Python knowledge, we also aim to teach you good programming practices, like version control. This will include setting up a [GitHub](https://github.com/) account, as described in the last section. We will cover this throughout the course, though you are more than welcome to try it out before hand and download the course's contents before we start. 

Before the bootcamp, it will be very helpful if you could install Python 3 on your computer, as described in the section below, which should set you up nicely for the course and hopefully any data analysis you need to do during your Masters. We have some optional resources for those [coming to Python from either Matlab or R](http://mathesaurus.sourceforge.net/matlab-python-xref.pdf), or those who are [new to programming](https://www.codecademy.com/learn/python). For the ones already experienced in Python, you are more than welcome to join and learn some new tricks. Finally, all students are encouraged to work together and help each other!


## Installing Python3 on Your Computer  

You may already have Python3 installed on your computer (especially if you have a Mac or Linux distribution). However, we recommend installing [Anaconda Python 3.7](https://www.anaconda.com/distribution/), which nicely supports Windows, Mac and Linux machines and will include the right version of Python with all the scientific packages needed for this bootcamp. If you have problems with the installation and Google is no help, we will do our best to help you in the first session of the bootcamp. 

Now that you have Python installed on your computer, you may want to try it out. The easiest way is to open a terminal and type `python`. This will let you introduce python commands. You may try with

+ `2+2`
+ `print('Hello, world!')`
+ `import numpy`

If you got no errors, you are more than ready to start the bootcamp! If you got any error, fear not, we will cover it in the first session of the bootcamp. Now to exit the python mode, you can type `exit()` and hit enter. 

## Git

Git is a version control software that allows us to keep track of the history of our code, data, and documents. This becomes essential when working with a team on a common project, but it is also extremely helpful even when working alone. To download the course materials run `$ git clone https://github.com/BorjaRequena/BIST-master-python-bootcamp`. 

### Remote Repositories
Our local git repositories are connected to a remote repository, e.g. the one you cloned. Remote repositories are often hosted by providers like [GitHub](https://github.com) or [GitLab](https://gitlab.com), which provide a graphical interface and further functionality for collaboration, such as an issue tracker or a wiki. We can download updates using `$ git pull` and upload your changes using `$ git push`.

In addition, there is software like [GitKraken](https://www.gitkraken.com/) that provides us with a visual interface that allows us to manage our git repositories without the command line. This comes specially handy to deal with git conflicts. 

### Versioning
We can view our changes to tracked files using `$ git diff` and get an overview with `$ git status`. Then, we can stage changes using `$ git add file-name` or `$ git add -A` to stage them all.  We can create a checkpoint with the staged changes using `$ git commit -m "Commit message"`. This message should be short, in case we want to add more information, we can skip the `-m` and our default text editor will open. To move or delete tracked files we can use `$ git mv` and `$ git rm` respectively. We can see the history with `$ git log` and go back to any point using `$ git checkout #commit-hash`.

### Stash and Branch
In case we need to quickly interupt our current tasks to work on something else, we can save and remove your unstaged changes with `$ git stash` and restore them with `$ git stash apply`. To keep track of several versions of our software, e.g. a stable version and one (for each new feature) under development, we can use [branches](https://git-scm.com/docs/git-branch).

### Git with Jupyter Notebooks
Our course uses Jupyter Notebooks, one of the most extended platforms, provided they can store code, plots and markdowns. However, notebooks are notoriously difficult to compare and version given that they, under the hood, are json files that store loads of metadata, such as cell execution counts. The [nbdev](https://nbdev.fast.ai/) library helps us with this. Once we have python, we can install it from the terminal with `$ pip install nbdev`. Then, the steps are: 
- Go to the github repository that we just downloaded: ~/whatever/path/BIST-master-python-bootcamp 
- Run `$ nbdev_install_git_hooks` 

nbdev is a library designed to use Jupyter Notebooks as source code for our libraries. In case you want a deeper dive into nbdev, we recommend going through [its tutorial](https://nbdev.fast.ai/tutorial.html) or our [metatutorial](https://borjarequena.github.io/nbdev_metatuto/tutorial/) with extended explanations, screenshots and source code.
