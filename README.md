# prometheus-intro
Introduction to the prometheus monitoring system

1. Clone this repo

```
git clone https://github.com/lsst-sqre/prometheus-intro.git
```

2. Create a virtualenv

```
cd prometheus-intro

virtualenv prometheus-intro -p python3
source prometheus-intro/bin/activate
pip install -r requirements.txt
```

3. Using the virtualenv in the Jupyter notebook

```
python -m ipykernel install --user --name=prometheus-intro
jupyter notebook
```

(You should now see your kernel in the Jupyter notebook menu: `Kernel -> Change kernel` and be able so switch to it.)

Open the `prometheus-intro.ipynb` notebook.

4. Install docker

The notebook requires `docker-compose` to run the Prometheus server locally.
See for instance how to [Install Docker for Mac](https://docs.docker.com/docker-for-mac/install/).
