## About PCV
PCV is a pure Python library for computer vision based on the book "Programming Computer Vision with Python" by Jan Erik Solem.
The original repository was forked by Abada Samuel for compatibility with Python 3.

More details on the book (and a pdf version of the latest draft) can be found at [programmingcomputervision.com](http://programmingcomputervision.com/).

### Dependencies
You need to have Python 3+ and as a minimum:
For Python2.6+ check the original repository: (https://github.com/jesolem/PCV)
* [NumPy](http://numpy.scipy.org/)
* [Matplotlib](http://matplotlib.sourceforge.net/)

Some parts use:

* [SciPy](http://scipy.org/)

Many sections show applications that require smaller specialized Python modules. See the book or the individual examples for full list of these dependencies.

### Structure

*pcv/*  the code.

*pcv_book/*  contains a clean folder with the code exactly as used in the book at time of publication.

*examples/*  contains sample code. Some examples use data available at [programmingcomputervision.com](http://programmingcomputervision.com/).

### Installation

For windows:
    Open a terminal in the PCV directory and run
    python setup.py install

For linux:
    Open a terminal in the PCV directory and run with sudo:
    python setup.py install

Now you should be able to do

	import PCV
	
in your Python session or script. Try one of the sample code examples to check that the installation works.

### License

All code in this project is provided as open source under the BSD license (2-clause "Simplified BSD License"). See LICENSE.txt. 


---
-Abada Samuel