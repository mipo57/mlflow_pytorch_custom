# Custom mlflow pytorch model

Most of the code is copied from mlflow.pytorch.__init__.py. The only thing that changes it that now _load_pyfunc returns model directly instead of a wrapper.
That allows you to implement a custom predict() function