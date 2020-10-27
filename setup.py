import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='mlflow_custom_pytorch',  
     version='0.11',
     scripts=[] ,
     author="Michał Pogoda",
     author_email="michalpogoda@hotmail.com",
     description="Utility library that allows to implement custom predict() function in pytorch models",
     long_description=long_description,
   long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
