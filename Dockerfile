FROM quay.io/qiime2/miniconda3
ADD resource/ /opt/resource/
RUN conda update conda -y
RUN conda install -c conda-forge google-auth -y
RUN conda install -c conda-forge google-api-python-client  -y
