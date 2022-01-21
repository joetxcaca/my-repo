FROM python

RUN apt-get update

RUN apt-get -y install dos2unix
RUN apt-get -y install libboost-dev
RUN apt-get -y install libgmp-dev
RUN apt-get -y install vim

RUN pip install --upgrade pip
RUN pip --version

RUN pip install black
RUN pip install coverage
RUN pip install mypy
RUN pip install numpy
RUN pip install pylint

RUN git clone https://github.com/DOMjudge/checktestdata checktestdata && \
    cd checktestdata                                                  && \
    git checkout release                                              && \
    ./bootstrap                                                       && \
    make                                                              && \
    cp checktestdata /usr/bin                                         && \
    cd -

CMD bash
