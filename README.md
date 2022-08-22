# doc_collection
> A tool for collecting documentation of python libs.


## Install


`git clone https://github.com/omemaxim/doc_collection`

## How to use

Firstly, you need to pip list of packages to be able to collect data from it:

```python
pip_top_hundred()
```

Now you are ready to extract data from all libs you have in your Python (where are can be some exceptions):

```python
extract()
```

    --------------- exception during tensorflow-io-gcs-filesystem documentation extracting
    --------------- exception during theano documentation extracting





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
      <th>56399</th>
      <td>aiohttp.ClientResponse.url. reify\n\n</td>
      <td>aiohttp.ClientResponse.url</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>56400</th>
      <td>aiohttp.ClientResponse.url_obj. reify\n\n</td>
      <td>aiohttp.ClientResponse.url_obj</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>56401</th>
      <td>aiohttp.ClientResponse.history. reify\n\n    A...</td>
      <td>aiohttp.ClientResponse.history</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>56402</th>
      <td>aiohttp.BodyPartReader.filename. reify\n\n    ...</td>
      <td>aiohttp.BodyPartReader.filename</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>56403</th>
      <td>aiohttp.BodyPartReader.name. reify\n\n    Retu...</td>
      <td>aiohttp.BodyPartReader.name</td>
      <td>aiohttp</td>
    </tr>
  </tbody>
</table>
<p>56404 rows × 3 columns</p>
</div>



Command above will return DataFrame of three columns: __text__ contains documentation of an object, __name__ contains the name and __library__ contains library of an object.
