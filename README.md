# extract_color

A simple python script using too much dependencies to get the main colors of an image with kmeans.  
The process is stochastic and no seed were set so each run will give a different result (can be changed with the argument `random_state` in kmeans).  

To install the dependencies:
```bash
pip install -r requirements.txt
```

After installing all dependencies (in a virtualenv or in the system) run:

```bash
python main.py path/to/image
```

## example

![](https://github.com/jackred/extract_color/raw/master/example/result2.png)
