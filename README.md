# beRi
beRi "beri environments for R installations" is a package management system for R.


## Introduction

  R unlike most other top level programming languages does not have a package manager.  beRi is a solution to this problem.  The name beRi stands for "beRi environments for R installations", which is a shout out to CRAN (as in cran*beRi*) as well as to Python's pip ("Pip Install Packages") package management tool.  The name can be changed at any point.
  
## Guidelines

  In order to create something valuable to the R community including RStudio, and the R maintainers, it's important that we write something that has credibility and creates reproducible environments.  It might be applicable for us to switch to an R CLI if absolutely necessary, but that's the least ideal solution.  Belwo are some useful links to help with creating this package in a meaningufl way:
  * https://cran.r-project.org/web/packages/startup/vignettes/startup-intro.html
  * https://www.osc.edu/resources/getting_started/howto/howto_install_local_r_packages
  * https://csgillespie.github.io/efficientR/r-startup.html
  * https://www.r-bloggers.com/how-to-pimp-your-rprofile/
  
## Other Potentially Useful Resources

* https://github.com/HenrikBengtsson/startup
* https://github.com/jdblischak/workflowr
* https://rstudio.github.io/reticulate/
* https://rpy2.github.io/doc/latest/html/index.html
* https://github.com/trinker/pacman
* https://github.com/talgalili/installr
* https://github.com/tidyverse/hms and https://github.com/tidyverse/lubridate
* https://github.com/tidyverse/glue
* https://github.com/tidyverse/dplyr
* https://github.com/kentonwhite/ProjectTemplate

  
## Ideas 

### First Major and Easily Attainable Goal

  Create a Python CLI that uses __utils::install.packages()__ function and the __devtools::install_\*()__ function.

### Second Goal

  * Create repositories for each specific version of R (MAJOR.MAJOR.MINOR) (3.4.4).  This has already been accomplished with the [r_environment_repository](https://github.com/bioinformatics-collaborative/r_environments/tree/master/minor_local_libs).
  * For each seperate repository/version of R, install various versions of packages in their own seperate directories.
    * Utilize the .Renviron file to save the *:* delimeted PATH to specific package versions.  The new environment variable could be called __R_LOADED_PACKAGES__.

### Side Goals

1. Virtual Environments

    * After figuring out the second goal it might be good to research how we could do virtual environments for R.  It could start with creating a packrat project.  And then we would have to create system links to folders and files.  This would have to be modeled after python's or condas virtual environment.
    * https://realpython.com/python-virtual-environments-a-primer/

## Known R Dependencies
  * [devtools](https://github.com/r-lib/devtools)
  * [packrat](https://github.com/rstudio/packrat)
  * [miniCRAN](https://github.com/andrie/miniCRAN)

## Known Python Dependencies
  * [click](https://github.com/pallets/click)
  * [poetry](https://github.com/sdispater/poetry)
  * [PyYaml](http://pyyaml.org/wiki/PyYAMLDocumentation)
