
![Amaranthus](./img/amaranthus1.svg)

## Amaranthus - A Cookiecutter template for Computational Scientific Research

_Finally, a folder structure and work flow that I'm proud to share!_


This template is my first true workflow for my computational neuroscientific projects.  However, it is broad enough to be applied to any computational discipline.
This is highly based on the great [Cookiecutter Data Science project template](http://drivendata.github.io/cookiecutter-data-science/)


Dedicated to [Amaranta Saball](https://open.spotify.com/track/0PqaN2yyQ1QdUR6UVHLna5?si=cf80748268e549c1).

### Requirements to use the Amaranthus template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```
or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### To start a new project, run:
------------

    cookiecutter  https://github.com/jpalma-espinosa/Amaranthus


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```

├── data
│   ├── params              <- Set of parameters to process the raw data
|   ├── processed           <- Put here the processeced data, ready to analyze and create plots
|   └── raw                 <- Raw unmutable data. 
├── LICENSE
├── Makefile                <- Makefile with commands like `make data` or `make train`
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),
│                              the creator's initials, and a short `-` delimited description, e.g.
│                              `1.0-jqp-initial-data-exploration`.
├── README.md               <- This file.
├── reports                 <- Holds rmd files for creating a lab notebook and a final report
|   ├── figs                <- Store your nice figures for reporting.  Could be generated from <project>/src/figures
│   ├── master              <- Holds master docs and bibliography
│   ├── output              <- Holds your knitted rmd files in several formats (.docx, .pdf, .html)
│   ├── presentations       <- Save here your slides and presentations.
│   ├── rmd                 <- Several rmd files for documentation process: Daily reporting, meeting 
|   |                          notes, experiment notes, paper analysis, preliminary results, among others
│   └── utils               <- Some utility files for knitting the master docs.
├── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
│                              generated with `pip freeze > requirements.txt`
├── src
│   ├── data-processing     <- Scripts to download or generate, and process data
│   ├── plotting            <- Scripts for making plots
│   └── utils               <- Utilitary scripts.  See inside for more information.
├── test_environment.py
└── tox.ini


```

## Contributing

I'm working on this. If you have any idea, please, drop me an [email](mailto: javier.palma@cinv.cl) or a message over here

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
