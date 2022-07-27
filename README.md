# doc_collection
> A tool for collecting documentation of python libs.


## Install

`pip install doc_collection`

## How to use

Firstly, you need to pip list of packages to be able to collect data from it:

```python
pip_top_hundred()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [7], in <cell line: 1>()
    ----> 1 pip_top_hundred()


    File ~/projects/doc_collection/doc_collection/core.py:17, in pip_top_hundred()
         16 def pip_top_hundred():
    ---> 17     lib_names = get_top_hundred()
         18     lib_names = replace(lib_names, 'msrest', 'msrestazure')
         19     for lib_name in lib_names:


    File ~/projects/doc_collection/doc_collection/core.py:7, in get_top_hundred()
          6 def get_top_hundred():
    ----> 7     if not os.path.isfile('data/top.json'):
          8         os.system('curl -X GET "https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json" > data/top.json')
         10     f = open('data/top.json')


    NameError: name 'os' is not defined


Now you are ready to extract data from all libs you've pipped and it's dependencies:

```python
extract()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [16], in <cell line: 1>()
    ----> 1 extract()


    File ~/projects/doc_collection/doc_collection/core.py:24, in extract()
         23 def extract():
    ---> 24     warnings.simplefilter(action='ignore', category=FutureWarning)
         25     warnings.filterwarnings("ignore", category=DeprecationWarning)
         27     installed_packages = pkg_resources.working_set


    NameError: name 'warnings' is not defined


Command above will return DataFrame of three columns: __text__ contains documentation of an object, __paths__ contains all names of an object (can be more than one) and __library__ contains library of an object.
