<p align="center"><a href="https://www.getberi.site/"><img src="https://user-images.githubusercontent.com/20953530/43921054-48163858-9be0-11e8-8ddb-385e1cd9c056.jpg" width=450></a></p>

<p align="center"><i>Are you a  bioinformatician who desires to manage R environments, install R, and install R packages using the command-line? Help develop <a href="https://github.com/datasnakes/beRi">beRi</a>!</i></p>

# beRi  [![Gitter chat](https://badges.gitter.im/CRANbeRi/Lobby.svg)](https://gitter.im/CRANbeRi/Lobby)

beRi "beri environments for R installations" is an R environment, R installation, and R package management system for R. 

The project was initially conceptualized by [Robert Gilmore](https://github.com/grabear). Gilmore proposed the project to [hackseq18](https://www.hackseq.com/) where it was developed over 3 days by a great team of [developers](#hackseq18-team-members). It ultimately went on to win hackseq18.

<p align="center"><a href="https://twitter.com/hackseq/status/1051628032228655104"><img src="https://i.imgur.com/tkZEmS8.png" width=450></a></p>
<br>
<p align="center"><a href="https://hackseq.github.io/hs18/2018/08/12/README.txt.html"><img src="https://i.imgur.com/B9WCmSh.png" width=450></a></p>


## What is beRi?

beRi is a suite of Python packages composed of the following components: (1) [renv](https://github.com/datasnakes/renv), a virtual environment manager for R; [rinse](https://github.com/datasnakes/rinse), an R installation and R version manager; and (3) [rut](https://github.com/datasnakes/rut), an R utility tool for installing packages, managing native R configuration files, and setting up local CRAN-like repositories. These packages will be developed in separate repositories as standalone command-line interfaces (CLIs). [beRi](https://github.com/datasnakes/beRi) will also be developed in a separate repository but will depend on the other three packages.

## Why beRi

View our [isc proposal](https://github.com/datasnakes/beri-isc-proposal) to the R Consortium for beRi and learn more about why beRi is needed and how we plan to integrate it.

## Dependencies

*  R - [remotes](https://github.com/r-lib/remotes), [packrat](https://github.com/rstudio/packrat), [jetpack](https://github.com/datasnakes/jetpack), [checkpoint](https://github.com/RevolutionAnalytics/checkpoint)
   
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

In order to create something valuable to the R community including RStudio and rOpenSci, it is critical that we develop something that has credibility and creates reproducible environments. Below are some useful links and packages that have acted as a guide for helping to create this package:

  * https://cran.r-project.org/web/packages/startup/vignettes/startup-intro.html
  * https://www.osc.edu/resources/getting_started/howto/howto_install_local_r_packages
  * https://csgillespie.github.io/efficientR/r-startup.html
  * https://www.r-bloggers.com/how-to-pimp-your-rprofile/
  * https://github.com/HenrikBengtsson/startup
  * https://github.com/jdblischak/workflowr
  * https://rstudio.github.io/reticulate/
  * https://rpy2.github.io/doc/latest/html/index.html
  * https://github.com/talgalili/installr
