# Data Coding Interview

This repo contains the assets for the Data team's coding interview question. It is shared with candidates prior to their scheduled interview.

**Candidates**

Please follow the instructions in this document to prepare for your coding interview.

## Setting Up Docker Environment

It is highly advisable that the candidate follow the following instructions prior to their schedule interview to setup the required docker environment. Otherwise, valuable interview time may be wasted on setting up the docker environment.

### Install Docker

You will require a docker system installed on the workstation you will be using for the interview.

Please see the [docker install documentation](https://docs.docker.com/engine/install/) for your operating system.

### Building Docker Image

Ensure that you have the [make](https://www.gnu.org/software/make/) tools installed on your workstation.

The [Makefile](Makefile) contains targets that can be used to build the image for [Dockerfile](docker/Dockerfile) by running:

```
make docker_image
```

#### Bash

If the docker image has been successfully built, you can now start the docker container and connect to it through a [bash](https://opensource.com/resources/what-bash) terminal with this target:

```
make docker_sh
```

##### Running Pytest Unit Tests

It is from the docker bash terminal that we will be executing Pytest unit tests for the coding interview question.

We use the [tox](https://tox.wiki/en/4.13.0/) automation tool to manage environments for running Pytest unit tests. So from the bash terminal run:

```
tox
```

See the [tox.ini](tox.ini) configuration file.


## Coding Interview Question


Under the [src](src) folder there is a [stories_metadata](src/stories_metadata) subfolder.

You will be asked to:
1. Implement the `build_ouput_df()` function in [spark_app.py](src/stories_metadata/spark_app.py).

1. Add the necessary tests cases for your implementation in [test_spark_app.py](src/stories_metadata/test_spark_app.py).

The detailed requirements for the coding interview will be provided during your interview.

It will be to your benefit to familiarize yourself with the sources in this repos beforehand.
