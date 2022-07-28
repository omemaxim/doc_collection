# doc_collection
> A tool for collecting documentation of python libs.


## Install

`pip install doc_collection`

## How to use

Firstly, you need to pip list of packages to be able to collect data from it:

```python
pip_top_hundred()
```

    Requirement already satisfied: boto3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.24.32)
    Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from boto3) (1.0.1)
    Requirement already satisfied: s3transfer<0.7.0,>=0.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from boto3) (0.6.0)
    Requirement already satisfied: botocore<1.28.0,>=1.27.32 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from boto3) (1.27.36)
    
    ...
    
    Requirement already satisfied: et-xmlfile in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from openpyxl) (1.1.0)
    Requirement already satisfied: et-xmlfile in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.1.0)
    Requirement already satisfied: psycopg2-binary in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.9.3)
    Requirement already satisfied: iniconfig in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.1.1)


Now you are ready to extract data from all libs you've pipped and it's dependencies:

```python
extract()
```

    1 files from absl added
    41 files from adal added
    1 files from aiobotocore added
    709 files from aiohttp added
    59 files from aioitertools added
    
    ...
    
    18 files from webencodings added
    155 files from websocket added
    330 files from werkzeug added
    1 files from wheel added
    2 files from widgetsnbextension added
    36 files from wrapt added
    33 files from wsproto added
    76 files from xxhash added
    66 files from yarl added
    86 files from zipp added





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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Python Library Documentation: Any in module tr...</td>
      <td>[ipykernel.comm.Comm.log]</td>
      <td>ipykernel</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Python Library Documentation: AxisProperty\n\n...</td>
      <td>[pandas.DataFrame.columns]</td>
      <td>pandas</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Python Library Documentation: AxisProperty\n\n...</td>
      <td>[pandas.Series.index]</td>
      <td>pandas</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Python Library Documentation: AxisProperty\n\n...</td>
      <td>[pandas.DataFrame.index]</td>
      <td>pandas</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Python Library Documentation: Bool in module o...</td>
      <td>[openpyxl.chart.AreaChart.roundedCorners]</td>
      <td>openpyxl</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>30112</th>
      <td>Python Library Documentation: property\n\n    ...</td>
      <td>[faiss.BufferList.wp]</td>
      <td>faiss</td>
    </tr>
    <tr>
      <th>30113</th>
      <td>Python Library Documentation: reify\n\n</td>
      <td>[aiohttp.ClientResponse.content_disposition]</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>30114</th>
      <td>Python Library Documentation: reify\n\n    A s...</td>
      <td>[aiohttp.ClientResponse.history]</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>30115</th>
      <td>Python Library Documentation: reify\n\n    Ret...</td>
      <td>[aiohttp.BodyPartReader.filename]</td>
      <td>aiohttp</td>
    </tr>
    <tr>
      <th>30116</th>
      <td>Python Library Documentation: reify\n\n    Ret...</td>
      <td>[aiohttp.BodyPartReader.name]</td>
      <td>aiohttp</td>
    </tr>
  </tbody>
</table>
<p>30117 rows × 3 columns</p>
</div>



Command above will return DataFrame of three columns: __text__ contains documentation of an object, __paths__ contains all names of an object (can be more than one) and __library__ contains library of an object.