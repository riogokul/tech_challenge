# Tech_challenge

The `main.py` is the main module with all the functionalities executed in the order of the given tasks and the accompanying `test.py` contains the unit tests. I have used pandas for all the analysis and matplotlib to plot the result.

I tried to use the multiprocessing module to enhance the performance, but it wasn't helpful. Since the dataset is very small, the overhead associated with creating and managing multiprocessing is high and it outweighs the benefits of parallelization. Based on my runs with parallelization it takes around 3 seconds to run, whereas it runs within 0.5 secs without multiprocessing.

To install all libraries used in the module
```bash
    pip install -r requirements.txt
```
##To run the program
```bash
    python main.py
```
##To run the tests
```bash
    python -m unittest test.py -v
```
