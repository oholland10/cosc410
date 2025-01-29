# Instructions for setting up your environment 

These instructions are heavily adapted from the `install.md` file written by [Forrest Davis](https://forrestdavis.github.io/) in the [NLPScholar](https://github.com/forrestdavis/NLPScholar/tree/main) repository. 


## Ways of running code

Here are two ways you can write and run code in this class. 

1. Use your local computer
2. Use Jupyter lab on the Colgate Supercomputer [Turing](https://turing.colgate.edu/)

To use Turing, you need to either be connected to eduroam on the Colgate campus or connect to the [VPN](https://www.colgate.edu/about/campus-services-and-resources/vpn-connections-campus-network). 

It might be worth it to setup the `cosc410` environment both locally ad on Turing. 


## (Local Computer) Install Anaconda

Note this only applies if you are installing things on your device. If you are on Turing, for example, you can skip to the next section. 

You will need Python 3 and some libraries. First, [download and install
Anaconda](https://www.anaconda.com/download) to manage the packages. You
should install the latest version of Anaconda (or Miniconda) available.

During the installation on MacOSX and Linux, you will be asked whether to
initialize Anaconda by running `conda init`: you should accept, as it will update your shell script to ensure that `conda` is available whenever you open a terminal.  

During the installation on Windows, you will be asked whether you
want the installer to update the `PATH` environment variable. This is not
recommended as it may interfere with other software. Instead, after the
installation you should open the Start Menu and launch an Anaconda Shell
whenever you want to use Anaconda.

After the installation, you must close your terminal and open a new
one for the changes to take effect.

    conda update -n base -c defaults conda
    conda update conda 
    pip install --upgrade pip

## Create the `cosc410` Environment

Navigate to the directory which has the [environment.yml](environment.yml) file, and run the following command. 

It will create a new `conda` environment containing the libraries you need to run the toolkit.  

    conda env create -f environment.yml

Next, activate the new environment:

    conda activate cosc410

## Add `cosc410` as a kernel 

Sometimes you want to use the `cosc410` environment in a jupyter notebook environment. To do this, you need to add it as a kernel. You can do so with: 
 

    python -m ipykernel install --user --name=cosc410 

Then, when you open a notebook, select `cosc410` as your kernel.

## Troubleshooting


### Errors installing torch 

If you run into errors while installing torch with the nlp environment,
**change** `torch==2.4.0` **to** `torch==2.2.0`  **in** `environment.yml` 

### Can't activate nlp environment on Turing but you installed it

Run: 

    source ~/.bashrc

If you see `(base)` to the left of your username on the terminal, then you are
all set to activate `nlp`. 


### Conda activate doesn't work

You will see a longer message about setting up conda for your shell. Run 

    conda init --all


### You want to try re-creating the environment (prefix already found)

Sometimes the environment is created, but something has gone wrong. That is when
you run: 

    conda env list 

You see `cosc410` but you want to reinstall it. To do this, delete the environment: 

    conda deactivate cosc410
    conda remove -n cosc410 --all 


