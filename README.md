<p align="center"><a href="https://www.getberi.site/"><img src="https://user-images.githubusercontent.com/20953530/43921054-48163858-9be0-11e8-8ddb-385e1cd9c056.jpg" width=450></a></p>

<p align="center"><i>Are you a bioinformatician frustrated by R’s inability to resolve common dependency issues? Help develop <a href="https://github.com/datasnakes/beRi">beRi</a>, a package management, reproducible workflow, and installation toolkit for the R programming language.</i></p>

# beRi  [![Gitter chat](https://badges.gitter.im/CRANbeRi/Lobby.svg)](https://gitter.im/CRANbeRi/Lobby)

beRi "beri environments for R installations" is a package management system for R. The project was initially conceptualized by [Robert Gilmore](https://github.com/grabear) with a little help from his colleague [Shaurita Hutchins](https://github.com/sdhutchins). Gilmore proposed the project to [hackseq18](https://www.hackseq.com/) where it was developed over 3 days by a great team of [developers](#hackseq18-team-members). It ultimately went on to win **favorite project** by the hackseq18 participants.

<p align="center"><img src="https://i.imgur.com/tkZEmS8.png" width=450></p>

## Introduction

R has many issues that stem from a lack of having proper management tools such as a project manager, a virtual environment manager, or a package manager. Many of the tools that are available are R packages, which makes it incredibly difficult to manage R from the command line. While Rstudio has developed a useful tool called packrat for managing projects, it still has performance issues including painfully long build times and poor integration with Bioconductor, one of the most widely used package repositories for R outside of CRAN. The task of building an R CLI is also a very daunting task even for advanced R users.

## beRi much better

In order to solve the above issues with R, we propose the beRi suite of tools for managing R. beRi is a set of Python packages which is composed of an R virtual environment manager ([renv](https://github.com/datasnakes/renv)), an R installation manager ([rinse](https://github.com/datasnakes/rinse)), and an R utility tool for installing packages, managing native R configuration files, and setting up local CRAN-like repositories ([rut](https://github.com/datasnakes/rut)). Since these packages/tools will be developed as standalone or fully independent CLI’s in separate repositories, beRi will integrate these packages and complement their functionalities in a separate CLI.

# Project Goals

- [ ] Develop standalone CLI's for renv, rut, and rinse using click
    - [ ] Build beRi CLI by grouping the standalone CLI.
    - [ ] Make sure the standalone CLI's can always be used with or without beRi.
- [ ] Design a file-system for beRi in ~/.beRi or ~/.local/beRi with cookiecutter
    - [ ]     R installs by default in .beRi file system
    - [ ]     packages install by default to .beRi file system
    - [ ]     projects are stored in .beRi file system
    - [ ]     repos are stored in .beRi file system
    - [ ]     beRi - configuration file (~/.beRi/<file_name>.yaml)
- [ ] Develop initially for linux
- [ ] Developing for user level workflows (no sudo/system)

View subproject level goals: https://github.com/datasnakes/renv/issues/23, https://github.com/datasnakes/rut/issues/5, https://github.com/datasnakes/rinse/issues/3

## Dependencies

*  R - [remotes](https://github.com/r-lib/remotes), [packrat](https://github.com/rstudio/packrat), [remotes](https://github.com/r-lib/remotes), [jetpack](https://github.com/datasnakes/jetpack)
   
* Python (3.6) - [click](https://github.com/pallets/click), [poetry](https://github.com/sdispater/poetry), [PyYaml](http://pyyaml.org/wiki/PyYAMLDocumentation)

## hackseq18 team members

* [Robert Gilmore](https://github.com/grabear) · **Team Lead**
* [Kristen Bystrom](https://github.com/ksbystrom)
* [Bruno Grande](https://github.com/scientificbruno)
* [Shaurita Hutchins](https://github.com/sdhutchins)
* [Michelle Lee](https://github.com/bitttyyyy)
* [Santina Lin](https://github.com/santina)
* [Zhi Yuh Ou Yang](https://github.com/ZhiYuh)
* [Hamid Younesy](https://github.com/hyounesy)

## References

In order to create something valuable to the R community including RStudio and the R maintainers, it is critical that we develop something that has credibility and creates reproducible environments. Below are some useful links and packages that have acted as a guide for helping to create this package:

  * https://cran.r-project.org/web/packages/startup/vignettes/startup-intro.html
  * https://www.osc.edu/resources/getting_started/howto/howto_install_local_r_packages
  * https://csgillespie.github.io/efficientR/r-startup.html
  * https://www.r-bloggers.com/how-to-pimp-your-rprofile/
  * https://github.com/HenrikBengtsson/startup
  * https://github.com/jdblischak/workflowr
  * https://rstudio.github.io/reticulate/
  * https://rpy2.github.io/doc/latest/html/index.html
  * https://github.com/talgalili/installr
