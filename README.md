# doc_collection
> A tool for collecting documentation of python libs.


## Install


`git clone https://github.com/omemaxim/doc_collection`

## How to use

Firstly, you need to pip list of packages to be able to collect data from it:

```python
pip_top_hundred()
```

Now you are ready to extract data from all libs you've pipped and it's dependencies:

```python
extract()
```

    --------------- error during tensorflow-io-gcs-filesystem documentation extracting
    --------------- error during theano documentation extracting





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
      <th>paths</th>
      <th>library</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Python Library Documentation: Any in module tr...</td>
      <td>[ipykernel.comm.Comm.log]</td>
      <td>ipykernel</td>
      <td>ipykernel.comm.Comm.log</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Python Library Documentation: AxisProperty\n\n...</td>
      <td>[pandas.DataFrame.columns]</td>
      <td>pandas</td>
      <td>pandas.DataFrame.columns</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Python Library Documentation: AxisProperty\n\n...</td>
      <td>[pandas.Series.index]</td>
      <td>pandas</td>
      <td>pandas.Series.index</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Python Library Documentation: AxisProperty\n\n...</td>
      <td>[pandas.DataFrame.index]</td>
      <td>pandas</td>
      <td>pandas.DataFrame.index</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Python Library Documentation: Bool in module o...</td>
      <td>[openpyxl.chart.AreaChart.roundedCorners]</td>
      <td>openpyxl</td>
      <td>openpyxl.chart.AreaChart.roundedCorners</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>31263</th>
      <td>Python Library Documentation: property\n\n    ...</td>
      <td>[faiss.BufferList.wp]</td>
      <td>faiss</td>
      <td>faiss.BufferList.wp</td>
    </tr>
    <tr>
      <th>31264</th>
      <td>Python Library Documentation: reify\n\n</td>
      <td>[aiohttp.ClientResponse.content_disposition]</td>
      <td>aiohttp</td>
      <td>aiohttp.ClientResponse.content_disposition</td>
    </tr>
    <tr>
      <th>31265</th>
      <td>Python Library Documentation: reify\n\n    A s...</td>
      <td>[aiohttp.ClientResponse.history]</td>
      <td>aiohttp</td>
      <td>aiohttp.ClientResponse.history</td>
    </tr>
    <tr>
      <th>31266</th>
      <td>Python Library Documentation: reify\n\n    Ret...</td>
      <td>[aiohttp.BodyPartReader.filename]</td>
      <td>aiohttp</td>
      <td>aiohttp.BodyPartReader.filename</td>
    </tr>
    <tr>
      <th>31267</th>
      <td>Python Library Documentation: reify\n\n    Ret...</td>
      <td>[aiohttp.BodyPartReader.name]</td>
      <td>aiohttp</td>
      <td>aiohttp.BodyPartReader.name</td>
    </tr>
  </tbody>
</table>
<p>31268 rows × 4 columns</p>
</div>



Command above will return DataFrame of four columns: __text__ contains documentation of an object, __paths__ contains all names of an object (can be more than one), __name__ contains the shortest name and __library__ contains library of an object.

# Elasticsearch 
## !!! 8.3.2 version of elastic was used
To create index and load mentioned dataframe to elastic. 

```python
# es_add_bulk(extract()) - !!! Commented only to pass tests (tester does not have elastic program). Don't pay attantion
```

The index's name is __doc__ and other fields are the same as in dataframe.
