# doc_collection
> A tool for collecting documentation of python libs.


## Install
PS, not working yet. Use git clone

`pip install doc_collection`

## How to use

Firstly, you need to pip list of packages to be able to collect data from it:

```python
pip_top_hundred()
```

Now you are ready to extract data from all libs you've pipped and it's dependencies:

```python
extract()
```

Command above will return DataFrame of three columns: __text__ contains documentation of an object, __paths__ contains all names of an object (can be more than one) and __library__ contains library of an object.

# Elasticsearch
To create index and load mentioned dataframe to elastic  

```python
es_add_bulk(extract())
```

The index's is __doc__ and other fields are like in dataframe.
