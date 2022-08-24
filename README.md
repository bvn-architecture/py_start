# `py_start` for a successful start to the day 🌤

Starts a new project in a directory, with a _venv_, a _.gitignore_, and installs some packages to get started.

The idea of this is that it gets projects off the ground in a consistent and useful way, with all the things you'll need to succeed. 

## How to use

Clone this repo into the same folder that you want the new repo to be in. It'll make a repo _next_ to this one.

```
parent
  ║
  ╠═ py_start ⟸ This repo
  ║
  ╚═ new_repo ⟸ your new repo. You can call it whatever you like
```

Then run the start.py file. This is how I run it on my computer:

```
C:\Users\bd\repos\py_start>python start.py
```

And then it'll ask you a bunch of questions about what you want to do.

## What does it do?

It'll:

1. Make a folder for your project
1. Download a `.gitignore` with everything you need for a good python project
1. Sets up a virtual environment using `venv`
1. Make a `requirements.in` file, which then compiles to a `requirements.txt`
1. Gives you all the instructions on what to do next

Give it a go!

## Some pointers 

For using your new venv:
1. It's a virtual environment, so you can run specific versions of libraries in isolation of other libraries you may have
1. This is an ideal workaround for if you're having difficulties with your virtual machine environment where you are unable to use pip when Using Path Variable(s)
1. A few ways you can activate a venv: `venv\Scripts\Activate.ps1`, or, `Ctrl+Shift+P` Selecting `Python Select Interpreter` then opening a new terminal.
1. If using VS code, you can quickly check that the venv is active by the green text with the active venv name in the terminal. 
1. Check that it's not defaulting to another venv by accident if you have multiple venv
1. Make sure you install the library you need into the venv, else it won't work!

## Contributing

This project is super young, so there's nothing formal to do. Just hack away and submit a PR, or open an issue and I'll see what I can do.
