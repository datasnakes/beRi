<p align="center"><a href="https://www.datasnakes.org/get-beri/"><img src="https://user-images.githubusercontent.com/20953530/43921054-48163858-9be0-11e8-8ddb-385e1cd9c056.jpg" width=450></a></p>

# Saturday 10-19 Status Report

We are currently working hard to complete the Windows implementation of rinse.  It's almost ready to test.  The MacOS implementation
goes beyond the scope of our abilities for this hackathon.  For renv we have made some great headway for MacOS, and for Windows we 
have just made the first commit.  By tomorrow morning we should be in the testing/debugging stage for most of our software (excluding rinse for MacOS).

# beRi  [![Gitter chat](https://badges.gitter.im/CRANbeRi/Lobby.svg)](https://gitter.im/CRANbeRi/Lobby)

beRi "beri environments for R installations" is an R environment, R installation, and R package management system for R. 

The project was initially conceptualized by [Robert Gilmore](https://github.com/grabear), and developed by a team at hackseq 2018 at UBC in Vancouver, BC.
 
<p align="center"><a href="https://twitter.com/hackseq/status/1051628032228655104"><img src="https://i.imgur.com/tkZEmS8.png" width=450></a></p>
<br>
<p align="center"><a href="https://hackseq.github.io/hs18/2018/08/12/README.txt.html"><img src="https://i.imgur.com/B9WCmSh.png" width=450></a></p>

## hackseq19

For hackseq19 we will be working towards making beRi cross compatible between operating systems.  Because beRi is composed of 3 separate python packages (rinse, renv, and rut), we will be focusing on 
creating implementations for two of these packages while we are here.  By the end of the project we would like to be able to install renv and rinse on Linux, MacOS, and Windows.
Please continue to the **hackseq19 README branches** for more information (see below).  You can also
view our [isc proposal](https://github.com/datasnakes/beri-isc-proposal) to the R Consortium for a greater understanding of the project as a whole.

* renv - https://github.com/datasnakes/renv/tree/hs19-readme
* rinse - https://github.com/datasnakes/rinse/tree/hackseq19-readme

## Development Tools
  
* Python (3.6) - [click](https://github.com/pallets/click), [poetry](https://github.com/sdispater/poetry), [PyYaml](http://pyyaml.org/wiki/PyYAMLDocumentation)

## hackseq19 team members

* [Robert Gilmore](https://github.com/grabear) · **hackseq18 Team Lead & Project Manager**
* [Shaurita Hutchins](https://github.com/sdhutchins) · **Lead Maintainer**
* [Roshan Pawar](http://github.com/r614)
* [Zongqi Wang](https://github.com/zongqi-wang)

## hackseq18 team members

* [Bruno Grande](https://github.com/scientificbruno) · **Lead Maintainer**
* [Santina Lin](https://github.com/santina) · **Lead Maintainer**
* [Kristen Bystrom](https://github.com/ksbystrom)
* [Michelle Lee](https://github.com/bitttyyyy)
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
