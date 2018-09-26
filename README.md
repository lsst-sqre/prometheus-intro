# prometheus
Introduction to the prometheus monitoring system

1. Clone this repo

```
git clone https://github.com/lsst-sqre/prometheus.git
```

2. Create a virtualenv

```
cd prometheus

virtualenv prometheus -p python3
source prometheus/bin/activate
pip install -r requirements.txt
```

3. Using the virtualenv in the Jupyter notebook

```
python -m ipykernel install --user --name=prometheus
jupyter notebook
```

(You should now see your kernel in the Jupyter notebook menu: `Kernel -> Change kernel` and be able so switch to it.)

Open the `prometheus.ipynb` notebook.
