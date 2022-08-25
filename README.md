# doc_collection
> A __universal__ tool for collecting documentation of python libraries.


## How to install


`git clone https://github.com/omemaxim/doc_collection`

## Purpose

Every well-maintained PyPi module has documentation in it's source. This tool provides functionality to collect, store and search in that documentation. 

# How to use

## 1. Collection

You can either collect documentation of one specific library or documentation of all packages in your python (including standard ones):

### One library

As mentioned above, there are two main functions: ``extract_one`` and ``extract``. The first one allows you to create a dataframe of documentation of specific library:

```python
from doc_collection.core import extract_one
```

```python
extract_one('pandas')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>pandas.DataFrame.columns. AxisProperty\n\n    ...</td>
      <td>pandas.DataFrame.columns</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pandas.Series.index. AxisProperty\n\n    The i...</td>
      <td>pandas.Series.index</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pandas.DataFrame.index. AxisProperty\n\n    Th...</td>
      <td>pandas.DataFrame.index</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pandas.IntervalIndex.is_non_overlapping_monoto...</td>
      <td>pandas.IntervalIndex.is_non_overlapping_monotonic</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pandas.IntervalIndex.is_unique. CachedProperty...</td>
      <td>pandas.IntervalIndex.is_unique</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2631</th>
      <td>pandas.core.internals.SingleArrayManager.is_vi...</td>
      <td>pandas.core.internals.SingleArrayManager.is_view</td>
    </tr>
    <tr>
      <th>2632</th>
      <td>pandas.core.internals.SingleBlockManager.is_vi...</td>
      <td>pandas.core.internals.SingleBlockManager.is_view</td>
    </tr>
    <tr>
      <th>2633</th>
      <td>pandas.HDFStore.is_open. property\n\n    retur...</td>
      <td>pandas.HDFStore.is_open</td>
    </tr>
    <tr>
      <th>2634</th>
      <td>pandas.RangeIndex.is_unique. property\n\n    r...</td>
      <td>pandas.RangeIndex.is_unique</td>
    </tr>
    <tr>
      <th>2635</th>
      <td>pandas.HDFStore.root. property\n\n    return t...</td>
      <td>pandas.HDFStore.root</td>
    </tr>
  </tbody>
</table>
<p>2636 rows × 2 columns</p>
</div>



Function above returns dataframe of two columns: __text__ column contains documentation and __name__ column contains name of  corresponding method/class/etc

### All libraries at once

Function below iterates over all modules in your local python and calls ``extract_one`` for all of it one by one

```python
from doc_collection.core import extract
```

```python
extract()
```

    --------------- exception during theano documentation extracting
    --------------- exception during tensorflow-io-gcs-filesystem documentation extracting





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>name</th>
      <th>library</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>pandas.DataFrame.columns. AxisProperty\n\n    ...</td>
      <td>pandas.DataFrame.columns</td>
      <td>pandas</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pandas.Series.index. AxisProperty\n\n    The i...</td>
      <td>pandas.Series.index</td>
      <td>pandas</td>
    </tr>
    <tr>
      <th>2</th>
      <td>pandas.DataFrame.index. AxisProperty\n\n    Th...</td>
      <td>pandas.DataFrame.index</td>
      <td>pandas</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ipykernel.comm.Comm.topic. Bytes in module tra...</td>
      <td>ipykernel.comm.Comm.topic</td>
      <td>ipykernel</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ipywidgets.Audio.value. Bytes in module traitl...</td>
      <td>ipywidgets.Audio.value</td>
      <td>ipykernel</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>57211</th>
      <td>aiohttp.ClientResponse.url. reify\n\n</td>
      <td>aiohttp.ClientResponse.url</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>57212</th>
      <td>aiohttp.ClientResponse.url_obj. reify\n\n</td>
      <td>aiohttp.ClientResponse.url_obj</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>57213</th>
      <td>aiohttp.ClientResponse.history. reify\n\n    A...</td>
      <td>aiohttp.ClientResponse.history</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>57214</th>
      <td>aiohttp.BodyPartReader.filename. reify\n\n    ...</td>
      <td>aiohttp.BodyPartReader.filename</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>57215</th>
      <td>aiohttp.BodyPartReader.name. reify\n\n    Retu...</td>
      <td>aiohttp.BodyPartReader.name</td>
      <td>aiohttp</td>
    </tr>
  </tbody>
</table>
<p>57216 rows × 3 columns</p>
</div>



Command above will return DataFrame of three columns: __text__ contains documentation of an object, __name__ contains the name and __library__ contains library of an object.

### Enrichment of python

Want to create a huge dataframe of documentation but don't have enough installed packages? This section is for you! ``pip_top_n`` function is able to pip top __n__ popular packages from [this website](https://hugovk.github.io/top-pypi-packages/). For example, let's pip top 5 pachages:

```python
from doc_collection.core import pip_top_n
```

```python
pip_top_n(5)
```

    boto3 was successfully pipped
    botocore was successfully pipped
    urllib3 was successfully pipped
    setuptools was successfully pipped
    requests was successfully pipped


## 2. Storing

A tool uses __ElasticSearch__ to store and search data, __sentence_transformers__ library to calculate embeddings for better search quallity.

### Prelims

Make sure you initialised __elasticsearch__ and sequence2vec model like below

```python
es = Elasticsearch('https://localhost:9200')

model_name = 'sentence-transformers/all-mpnet-base-v2'
model = SentenceTransformer(model_name)
```

### Creating index & indexing data

There are function to create index and index data from dataframe mentioned above:

```python
from doc_collection.search import index_data
```

```python
# index_data(d, es, model)
```

### Search

```python
from doc_collection.search import query
```

There are several ways to present data that was found. 
Query with following signature returns raw elasticsearch response:

```python
# query(text, size, es, model)
```

By specifying ``field`` parameter into __name__, you can get only names of methods.

```python
# query(text='How to drop a column of dataframe?', size=10, es=es, model=model, field='name')
```




    ['pandas.DataFrame.drop',
     'pandas.Series.drop',
     'pandas.DataFrame.dropna',
     'pyarrow.Table.drop',
     'datasets.Dataset.drop_index',
     'pandas.DataFrame.droplevel',
     'datasets.IterableDatasetDict.remove_columns',
     'datasets.IterableDataset.remove_columns',
     'pandas.Series.droplevel',
     'datasets.DatasetDict.remove_columns']



By spicifying ``field`` parameter into __text__, you'll be able to get documentation:

```python
# print(query(text='How to drop a column of dataframe?', size=1, es=es, model=model, field='text')[0])
```

    pandas.DataFrame.drop. function drop in module pandas.core.frame
    
    ddrroopp(self, labels=None, axis: 'Axis' = 0, index=None, columns=None, level: 'Level | None' = None, inplace: 'bool' = False, errors: 'str' = 'raise')
        Drop specified labels from rows or columns.
        
        Remove rows or columns by specifying label names and corresponding
        axis, or by specifying directly index or column names. When using a
        multi-index, labels on different levels can be removed by specifying
        the level. See the `user guide <advanced.shown_levels>`
        for more information about the now unused levels.
        
        Parameters
        ----------
        labels : single label or list-like
            Index or column labels to drop. A tuple will be used as a single
            label and not treated as a list-like.
        axis : {0 or 'index', 1 or 'columns'}, default 0
            Whether to drop labels from the index (0 or 'index') or
            columns (1 or 'columns').
        index : single label or list-like
            Alternative to specifying axis (``labels, axis=0``
            is equivalent to ``index=labels``).
        columns : single label or list-like
            Alternative to specifying axis (``labels, axis=1``
            is equivalent to ``columns=labels``).
        level : int or level name, optional
            For MultiIndex, level from which the labels will be removed.
        inplace : bool, default False
            If False, return a copy. Otherwise, do operation
            inplace and return None.
        errors : {'ignore', 'raise'}, default 'raise'
            If 'ignore', suppress error and only existing labels are
            dropped.
        
        Returns
        -------
        DataFrame or None
            DataFrame without the removed index or column labels or
            None if ``inplace=True``.
        
        Raises
        ------
        KeyError
            If any of the labels is not found in the selected axis.
        
        See Also
        --------
        DataFrame.loc : Label-location based indexer for selection by label.
        DataFrame.dropna : Return DataFrame with labels on given axis omitted
            where (all or any) data are missing.
        DataFrame.drop_duplicates : Return DataFrame with duplicate rows
            removed, optionally only considering certain columns.
        Series.drop : Return Series with specified index labels removed.
        
        Examples
        --------
        >>> df = pd.DataFrame(np.arange(12).reshape(3, 4),
        ...                   columns=['A', 'B', 'C', 'D'])
        >>> df
           A  B   C   D
        0  0  1   2   3
        1  4  5   6   7
        2  8  9  10  11
        
        Drop columns
        
        >>> df.drop(['B', 'C'], axis=1)
           A   D
        0  0   3
        1  4   7
        2  8  11
        
        >>> df.drop(columns=['B', 'C'])
           A   D
        0  0   3
        1  4   7
        2  8  11
        
        Drop a row by index
        
        >>> df.drop([0, 1])
           A  B   C   D
        2  8  9  10  11
        
        Drop columns and/or rows of MultiIndex DataFrame
        
        >>> midx = pd.MultiIndex(levels=[['lama', 'cow', 'falcon'],
        ...                              ['speed', 'weight', 'length']],
        ...                      codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],
        ...                             [0, 1, 2, 0, 1, 2, 0, 1, 2]])
        >>> df = pd.DataFrame(index=midx, columns=['big', 'small'],
        ...                   data=[[45, 30], [200, 100], [1.5, 1], [30, 20],
        ...                         [250, 150], [1.5, 0.8], [320, 250],
        ...                         [1, 0.8], [0.3, 0.2]])
        >>> df
                        big     small
        lama    speed   45.0    30.0
                weight  200.0   100.0
                length  1.5     1.0
        cow     speed   30.0    20.0
                weight  250.0   150.0
                length  1.5     0.8
        falcon  speed   320.0   250.0
                weight  1.0     0.8
                length  0.3     0.2
        
        Drop a specific index combination from the MultiIndex
        DataFrame, i.e., drop the combination ``'falcon'`` and
        ``'weight'``, which deletes only the corresponding row
        
        >>> df.drop(index=('falcon', 'weight'))
                        big     small
        lama    speed   45.0    30.0
                weight  200.0   100.0
                length  1.5     1.0
        cow     speed   30.0    20.0
                weight  250.0   150.0
                length  1.5     0.8
        falcon  speed   320.0   250.0
                length  0.3     0.2
        
        >>> df.drop(index='cow', columns='small')
                        big
        lama    speed   45.0
                weight  200.0
                length  1.5
        falcon  speed   320.0
                weight  1.0
                length  0.3
        
        >>> df.drop(index='length', level=1)
                        big     small
        lama    speed   45.0    30.0
                weight  200.0   100.0
        cow     speed   30.0    20.0
                weight  250.0   150.0
        falcon  speed   320.0   250.0
                weight  1.0     0.8
    


# Afterwords

This tool highly depends on python build of the one who run code. That's why unexpected behavior is likely to happen. Feel free to add issues if you have one!
