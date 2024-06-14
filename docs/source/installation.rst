Installation
============

In this tutorial we cover how to setup an Python environment that allows you quickly get started to run simulations of MARVEL spectra.

.. important::

   We recommend to follow the installation instructions below while using `Poetry <https://python-poetry.org/>`_ to install MARVELsim. With Poetry you will get a direct freeze of the software which successfully will build across any platform, which particularly becomes handy on computing clusters. Note that **Python version 3.8 - 3.10** have been well tested with Poetry.

   
1. Downlod from source
----------------------

The first step depends on whether you want to simply use the code or to be a developer.

*For users*
...........

For usage only simply git clone the repository. Move to a desired directory for which you want to download the software on your system and simply: 

.. code-block:: shell

   git clone https://github.com/IvS-KULeuven/MARVELsim.git

*For developers*
................
   
If you want to be a developer you need to adhere to our branching strategy being:

.. warning::

   All development is done on the ``develop`` branch. The ``master`` branch should alsways be a stable and well-tested branch merged from the ``develop`` branch, which is tracked with a `Release tag <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>`_.

- First go to the `upstream GitHub MARVELsim repository page <https://github.com/IvS-KULeuven/MARVELsim/tree/develop>`_. Check that your are indeed on the develop branch page and make a fork of the develop branch (click on the ``Fork`` bottom located in the top right cornor).
- Upon a fork creation you are now within your own GitHub repository (named ``<username>/MARVELsim``). Now copy the HTTPS link from the green ``Code`` bottom.
- Move to a desired directory for which you want to download the software on your system and simply: ``git clone <copied-link-to-fork>``.
- To be able to pull the latest version of the upstream software into your local copy, you need to add the upstream to your list of remote repositories by executing the command ``git remote add upstream https://github.com/IvS-KULeuven/MARVELsim.git``. To check your list of remote repositories, execute the following command in the the installation folder: ``git remote -v``.
- A general workflow as a developer looks like:
  
  * Make a change to some file(s)
  * Add the change to git: ``git add <file>``
  * Commit the change: ``git commit -m "<Write useful message>``
  * Fetch any changes that may be from collaborators: ``git fetch upstream``
  * If any changes, merge these into the local repo: ``git merge upstream/develop``
  * If conflict, resolve them by opening each conflicted file and edit (again commit changes)
  * Push commit(s) to your fork: ``git push origin develop``
  * Open a pull request on the IvS upstream develop branch (compare forks) and merge.
  * That's it! Now your collaborators can use your changes!

2. Local installation
---------------------
   
We strongly recommend to install Poetry through a `Conda <https://docs.conda.io/en/latest/>`_ environment. This is especially handy when installing on a computing cluster since these typically only have limited versions of Python installed by default. While using Conda all Python versions can be installed and thus an exact freeze of the poetry installation can be made. Thus first install Conda (using `Anaconda <https://www.anaconda.com/>`_  or `Miniconda <https://docs.conda.io/projects/miniconda/en/latest/>`_) and the create a new environment called ``marvelsim`` (here we use Python 3.9): 

.. code-block:: shell
		
   conda create -n marvelsim python=3.9

Activate your new conda environment:

.. code-block:: shell

   conda activate marvelsim

Since the most commen use case for MARVELsim is to run with High Performace Computing (HPC), it is recommended to use `Poetry <https://python-poetry.org/>`_ as your Python package manager. First `check how to install Poetry <https://python-poetry.org/docs/>`_.

.. code-block:: shell

   curl -sSL https://install.python-poetry.org | python -

Verify that poetry was installed successfully by typing ``poetry --version``. With your ``marvelsim`` Conda environment activated, and being located in the ``MARVELsim`` folder, install all packages with:

.. code-block:: shell

   poetry install

If you are a developer and want to update the MARVELsim documentation page, simply add the argument ``--with docs`` to the above poetry install call.

.. warning::

   Some users may find that Poetry stalls during the installation procedure. If that happens it is typically caused by a bad *keyring* setting in Poetry. Simple run the following command and retry the installation:

   .. code-block:: shell
		   
      export PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring




2. Cluster installation
-----------------------

Here we show how to install Poetry on the `Vlaams Supercomputer Centrum (VSC) <https://docs.vscentrum.be/index.html>`_, however, the general workflow can most likely be followed for installing MARVELsim on any cluster.

* Your first steps are to create a VSC account and install Miniconda as per the documentation. On a computing cluster you typically want to avoid installing software directly to your ``$VSC_HOME`` directory since this location typically offers a limited amount of storage memory. Thus, install Miniconda and Poetry (next bullet point) into your ``$VSC_DATA`` directory. Install Poetry pointing to ``$VSC_DATA`` directory:

  .. code-block:: shell

     curl -sSL https://install.python-poetry.org | POETRY_HOME=$VSC_DATA/poetry python -
   
  Verify that poetry was installed successfully by typing ``poetry --version`` and verify that installation location with ``which poetry``.
  
* Create a Conda environment, activate it, and install the Python packages with Poetry:

  .. code-block:: shell
		
     conda create -n marvelsim python=3.9
     conda activate marvelsim
     poetry install

* Lastly we need to create VSC module environment with modules needed to launch a simulation on the GPU nodes. Since the VSC Tier-2 have two main clusters called Genius and wICE. In the following we create a module environment on Genius (``cluster/genius/batch``):
  
  .. code-block:: shell
		
     module load intel/2021a
     module load CUDA/11.4.1
     
  Save the modules into a module environment:
  
  .. code-block:: shell
		
     module save marvelsim_genius

  Before submitting any MARVELsim job, simply load your module environment with:

  .. code-block:: shell
		
     module restore marvelsim_genius

  Check out how to generate a job script for CPU/CUDA usage in the section of :doc:`Performance <performance>`.




  
.. raw:: html

   <hr>



	 
Extra tools
-----------

Before starting investigating your output fits files we recomment to install `dfits <https://www.eso.org/sci/software/eclipse/eug/eug/node8.html>`_ which is an nice tool to inspect fits headers (e.g. ``dfits <filename>.fits``). On Linux install this packge with:

.. code-block:: shell

   sudo apt-get install qfits-tools

In addition, the astronomy software `ds9 <https://sites.google.com/cfa.harvard.edu/saoimageds9>`_ is an indispensable tool to quickly view your fits images (e.g. ``ds9 <filename>.fits``). Install this software with:

.. code-block:: shell

   sudo apt install saods9
