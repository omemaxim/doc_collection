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
    Requirement already satisfied: urllib3<1.27,>=1.25.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.28.0,>=1.27.32->boto3) (1.26.10)
    Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.28.0,>=1.27.32->boto3) (2.8.2)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.28.0,>=1.27.32->boto3) (1.16.0)
    Requirement already satisfied: botocore in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.27.36)
    Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore) (1.0.1)
    Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore) (2.8.2)
    Requirement already satisfied: urllib3<1.27,>=1.25.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore) (1.26.10)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil<3.0.0,>=2.1->botocore) (1.16.0)
    Requirement already satisfied: urllib3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.26.10)
    Requirement already satisfied: setuptools in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (62.6.0)
    Requirement already satisfied: requests in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.28.1)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests) (2022.6.15)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests) (2.1.0)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests) (3.3)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests) (1.26.10)
    Requirement already satisfied: s3transfer in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.6.0)
    Requirement already satisfied: botocore<2.0a.0,>=1.12.36 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from s3transfer) (1.27.36)
    Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<2.0a.0,>=1.12.36->s3transfer) (2.8.2)
    Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<2.0a.0,>=1.12.36->s3transfer) (1.0.1)
    Requirement already satisfied: urllib3<1.27,>=1.25.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<2.0a.0,>=1.12.36->s3transfer) (1.26.10)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<2.0a.0,>=1.12.36->s3transfer) (1.16.0)
    Requirement already satisfied: six in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.16.0)
    Requirement already satisfied: python-dateutil in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.8.2)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil) (1.16.0)
    Requirement already satisfied: certifi in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2022.6.15)
    Requirement already satisfied: idna in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.3)
    Requirement already satisfied: pyyaml in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (5.4.1)
    Requirement already satisfied: typing-extensions in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.3.0)
    Requirement already satisfied: charset-normalizer in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.1.0)
    Requirement already satisfied: pip in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (22.2)
    Requirement already satisfied: numpy in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.23.1)
    Requirement already satisfied: google-api-core in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.8.2)
    Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.56.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core) (1.56.4)
    Requirement already satisfied: google-auth<3.0dev,>=1.25.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core) (2.9.1)
    Requirement already satisfied: protobuf<5.0.0dev,>=3.15.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core) (3.19.4)
    Requirement already satisfied: requests<3.0.0dev,>=2.18.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core) (2.28.1)
    Requirement already satisfied: six>=1.9.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-api-core) (1.16.0)
    Requirement already satisfied: cachetools<6.0,>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-api-core) (5.2.0)
    Requirement already satisfied: rsa<5,>=3.1.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-api-core) (4.7.2)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-api-core) (0.2.8)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core) (1.26.10)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core) (2.1.0)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core) (3.3)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core) (2022.6.15)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0dev,>=1.25.0->google-api-core) (0.4.8)
    Requirement already satisfied: wheel in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.37.1)
    Requirement already satisfied: cryptography in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (37.0.4)
    Requirement already satisfied: cffi>=1.12 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cryptography) (1.15.1)
    Requirement already satisfied: pycparser in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cffi>=1.12->cryptography) (2.21)
    Requirement already satisfied: pyparsing in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.0.9)
    Requirement already satisfied: packaging in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (21.3)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from packaging) (3.0.9)
    Requirement already satisfied: jmespath in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.0.1)
    Requirement already satisfied: awscli in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.25.36)
    Requirement already satisfied: rsa<4.8,>=3.1.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from awscli) (4.7.2)
    Requirement already satisfied: PyYAML<5.5,>=3.10 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from awscli) (5.4.1)
    Requirement already satisfied: docutils<0.17,>=0.10 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from awscli) (0.16)
    Requirement already satisfied: botocore==1.27.36 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from awscli) (1.27.36)
    Requirement already satisfied: s3transfer<0.7.0,>=0.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from awscli) (0.6.0)
    Requirement already satisfied: colorama<0.4.5,>=0.2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from awscli) (0.4.4)
    Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore==1.27.36->awscli) (2.8.2)
    Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore==1.27.36->awscli) (1.0.1)
    Requirement already satisfied: urllib3<1.27,>=1.25.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore==1.27.36->awscli) (1.26.10)
    Requirement already satisfied: pyasn1>=0.1.3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from rsa<4.8,>=3.1.2->awscli) (0.4.8)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil<3.0.0,>=2.1->botocore==1.27.36->awscli) (1.16.0)
    Requirement already satisfied: rsa in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.7.2)
    Requirement already satisfied: pyasn1>=0.1.3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from rsa) (0.4.8)
    Requirement already satisfied: pyasn1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.4.8)
    Requirement already satisfied: importlib-metadata in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.12.0)
    Requirement already satisfied: zipp>=0.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from importlib-metadata) (3.8.1)
    Requirement already satisfied: zipp in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.8.1)
    Requirement already satisfied: pyjwt in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.4.0)
    Requirement already satisfied: colorama in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.4.4)
    Requirement already satisfied: pytz in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2022.1)
    Requirement already satisfied: click in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (8.1.3)
    Requirement already satisfied: pandas in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.4.3)
    Requirement already satisfied: numpy>=1.18.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pandas) (1.23.1)
    Requirement already satisfied: python-dateutil>=2.8.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pandas) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pandas) (2022.1)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)
    Requirement already satisfied: protobuf in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.19.4)
    Requirement already satisfied: attrs in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (21.4.0)
    Requirement already satisfied: cffi in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.15.1)
    Requirement already satisfied: pycparser in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cffi) (2.21)
    Requirement already satisfied: oauthlib in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.2.0)
    Requirement already satisfied: jinja2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.1.2)
    Requirement already satisfied: MarkupSafe>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from jinja2) (2.1.1)
    Requirement already satisfied: requests-oauthlib in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.3.1)
    Requirement already satisfied: requests>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests-oauthlib) (2.28.1)
    Requirement already satisfied: oauthlib>=3.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests-oauthlib) (3.2.0)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.0.0->requests-oauthlib) (2022.6.15)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.0.0->requests-oauthlib) (1.26.10)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.0.0->requests-oauthlib) (2.1.0)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.0.0->requests-oauthlib) (3.3)
    Requirement already satisfied: markupsafe in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.1.1)
    Requirement already satisfied: pycparser in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.21)
    Requirement already satisfied: docutils in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.16)
    Requirement already satisfied: google-auth in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.9.1)
    Requirement already satisfied: rsa<5,>=3.1.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth) (4.7.2)
    Requirement already satisfied: cachetools<6.0,>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth) (5.2.0)
    Requirement already satisfied: six>=1.9.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth) (1.16.0)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth) (0.2.8)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyasn1-modules>=0.2.1->google-auth) (0.4.8)
    Requirement already satisfied: cachetools in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (5.2.0)
    Requirement already satisfied: pyasn1-modules in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.2.8)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyasn1-modules) (0.4.8)
    Requirement already satisfied: wrapt in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.14.1)
    Requirement already satisfied: googleapis-common-protos in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.56.4)
    Requirement already satisfied: protobuf<5.0.0dev,>=3.15.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from googleapis-common-protos) (3.19.4)
    Requirement already satisfied: psutil in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (5.9.1)
    Requirement already satisfied: isodate in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.6.1)
    Requirement already satisfied: six in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from isodate) (1.16.0)
    Requirement already satisfied: pyarrow in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (8.0.0)
    Requirement already satisfied: numpy>=1.16.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyarrow) (1.23.1)
    Requirement already satisfied: sqlalchemy in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.4.39)
    Requirement already satisfied: greenlet!=0.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from sqlalchemy) (1.1.2)
    Requirement already satisfied: azure-core in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.24.2)
    Requirement already satisfied: six>=1.11.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-core) (1.16.0)
    Requirement already satisfied: requests>=2.18.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-core) (2.28.1)
    Requirement already satisfied: typing-extensions>=4.0.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-core) (4.3.0)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.18.4->azure-core) (2.1.0)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.18.4->azure-core) (1.26.10)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.18.4->azure-core) (3.3)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.18.4->azure-core) (2022.6.15)
    Requirement already satisfied: lxml in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.9.1)
    Requirement already satisfied: chardet in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (5.0.0)
    Requirement already satisfied: tomli in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.0.1)
    Requirement already satisfied: msrestazure in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.6.4)
    Requirement already satisfied: six in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrestazure) (1.16.0)
    Requirement already satisfied: adal<2.0.0,>=0.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrestazure) (1.2.7)
    Requirement already satisfied: msrest<2.0.0,>=0.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrestazure) (0.7.1)
    Requirement already satisfied: PyJWT<3,>=1.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from adal<2.0.0,>=0.6.0->msrestazure) (2.4.0)
    Requirement already satisfied: cryptography>=1.1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from adal<2.0.0,>=0.6.0->msrestazure) (37.0.4)
    Requirement already satisfied: python-dateutil<3,>=2.1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from adal<2.0.0,>=0.6.0->msrestazure) (2.8.2)
    Requirement already satisfied: requests<3,>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from adal<2.0.0,>=0.6.0->msrestazure) (2.28.1)
    Requirement already satisfied: requests-oauthlib>=0.5.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrest<2.0.0,>=0.6.0->msrestazure) (1.3.1)
    Requirement already satisfied: azure-core>=1.24.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrest<2.0.0,>=0.6.0->msrestazure) (1.24.2)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrest<2.0.0,>=0.6.0->msrestazure) (2022.6.15)
    Requirement already satisfied: isodate>=0.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrest<2.0.0,>=0.6.0->msrestazure) (0.6.1)
    Requirement already satisfied: typing-extensions>=4.0.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-core>=1.24.0->msrest<2.0.0,>=0.6.0->msrestazure) (4.3.0)
    Requirement already satisfied: cffi>=1.12 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cryptography>=1.1.0->adal<2.0.0,>=0.6.0->msrestazure) (1.15.1)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3,>=2.0.0->adal<2.0.0,>=0.6.0->msrestazure) (3.3)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3,>=2.0.0->adal<2.0.0,>=0.6.0->msrestazure) (1.26.10)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3,>=2.0.0->adal<2.0.0,>=0.6.0->msrestazure) (2.1.0)
    Requirement already satisfied: oauthlib>=3.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests-oauthlib>=0.5.0->msrest<2.0.0,>=0.6.0->msrestazure) (3.2.0)
    Requirement already satisfied: pycparser in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cffi>=1.12->cryptography>=1.1.0->adal<2.0.0,>=0.6.0->msrestazure) (2.21)
    Requirement already satisfied: async-timeout in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.0.2)
    Requirement already satisfied: grpcio in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.47.0)
    Requirement already satisfied: six>=1.5.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from grpcio) (1.16.0)
    Requirement already satisfied: decorator in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (5.1.1)
    Requirement already satisfied: aiobotocore in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.3.4)
    Requirement already satisfied: aioitertools>=0.5.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiobotocore) (0.10.0)
    Collecting botocore<1.24.22,>=1.24.21
      Using cached botocore-1.24.21-py3-none-any.whl (8.6 MB)
    Requirement already satisfied: aiohttp>=3.3.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiobotocore) (3.8.1)
    Requirement already satisfied: wrapt>=1.10.10 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiobotocore) (1.14.1)
    Requirement already satisfied: aiosignal>=1.1.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp>=3.3.1->aiobotocore) (1.2.0)
    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp>=3.3.1->aiobotocore) (4.0.2)
    Requirement already satisfied: yarl<2.0,>=1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp>=3.3.1->aiobotocore) (1.7.2)
    Requirement already satisfied: frozenlist>=1.1.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp>=3.3.1->aiobotocore) (1.3.0)
    Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp>=3.3.1->aiobotocore) (2.1.0)
    Requirement already satisfied: attrs>=17.3.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp>=3.3.1->aiobotocore) (21.4.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp>=3.3.1->aiobotocore) (6.0.2)
    Requirement already satisfied: typing_extensions>=4.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aioitertools>=0.5.1->aiobotocore) (4.3.0)
    Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.24.22,>=1.24.21->aiobotocore) (1.0.1)
    Requirement already satisfied: urllib3<1.27,>=1.25.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.24.22,>=1.24.21->aiobotocore) (1.26.10)
    Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.24.22,>=1.24.21->aiobotocore) (2.8.2)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.24.22,>=1.24.21->aiobotocore) (1.16.0)
    Requirement already satisfied: idna>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from yarl<2.0,>=1.0->aiohttp>=3.3.1->aiobotocore) (3.3)
    Installing collected packages: botocore
      Attempting uninstall: botocore
        Found existing installation: botocore 1.27.36
        Uninstalling botocore-1.27.36:
          Successfully uninstalled botocore-1.27.36


    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    boto3 1.24.32 requires botocore<1.28.0,>=1.27.32, but you have botocore 1.24.21 which is incompatible.
    awscli 1.25.36 requires botocore==1.27.36, but you have botocore 1.24.21 which is incompatible.


    Successfully installed botocore-1.24.21
    Requirement already satisfied: werkzeug in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.1.2)
    Requirement already satisfied: pillow in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (9.2.0)
    Requirement already satisfied: aiohttp in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.8.1)
    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp) (4.0.2)
    Requirement already satisfied: attrs>=17.3.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp) (21.4.0)
    Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp) (2.1.0)
    Requirement already satisfied: frozenlist>=1.1.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp) (1.3.0)
    Requirement already satisfied: yarl<2.0,>=1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp) (1.7.2)
    Requirement already satisfied: multidict<7.0,>=4.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp) (6.0.2)
    Requirement already satisfied: aiosignal>=1.1.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp) (1.2.0)
    Requirement already satisfied: idna>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from yarl<2.0,>=1.0->aiohttp) (3.3)
    Requirement already satisfied: multidict in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (6.0.2)
    Requirement already satisfied: beautifulsoup4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.11.1)
    Requirement already satisfied: soupsieve>1.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from beautifulsoup4) (2.3.2.post1)
    Requirement already satisfied: soupsieve in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.3.2.post1)
    Requirement already satisfied: scipy in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.8.1)
    Requirement already satisfied: numpy<1.25.0,>=1.17.3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from scipy) (1.23.1)
    Requirement already satisfied: yarl in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.7.2)
    Requirement already satisfied: idna>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from yarl) (3.3)
    Requirement already satisfied: multidict>=4.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from yarl) (6.0.2)
    Requirement already satisfied: google-cloud-storage in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.4.0)
    Requirement already satisfied: google-auth<3.0dev,>=1.25.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-storage) (2.9.1)
    Requirement already satisfied: google-cloud-core<3.0dev,>=2.3.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-storage) (2.3.2)
    Requirement already satisfied: requests<3.0.0dev,>=2.18.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-storage) (2.28.1)
    Requirement already satisfied: google-resumable-media>=2.3.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-storage) (2.3.3)
    Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-storage) (2.8.2)
    Requirement already satisfied: protobuf<5.0.0dev,>=3.15.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-storage) (3.19.4)
    Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.56.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-storage) (1.56.4)
    Requirement already satisfied: cachetools<6.0,>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-storage) (5.2.0)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-storage) (0.2.8)
    Requirement already satisfied: six>=1.9.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-storage) (1.16.0)
    Requirement already satisfied: rsa<5,>=3.1.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-storage) (4.7.2)
    Requirement already satisfied: google-crc32c<2.0dev,>=1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-resumable-media>=2.3.2->google-cloud-storage) (1.3.0)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-storage) (3.3)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-storage) (2022.6.15)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-storage) (2.1.0)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-storage) (1.26.10)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0dev,>=1.25.0->google-cloud-storage) (0.4.8)
    Requirement already satisfied: py in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.11.0)
    Requirement already satisfied: fsspec in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2022.5.0)
    Requirement already satisfied: google-cloud-bigquery in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.2.0)
    Requirement already satisfied: protobuf<4.0.0dev,>=3.12.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (3.19.4)
    Requirement already satisfied: google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (2.8.2)
    Requirement already satisfied: google-resumable-media<3.0dev,>=0.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (2.3.3)
    Requirement already satisfied: pyarrow<9.0dev,>=3.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (8.0.0)
    Requirement already satisfied: google-cloud-bigquery-storage<3.0.0dev,>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (2.14.1)
    Requirement already satisfied: google-cloud-core<3.0.0dev,>=1.4.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (2.3.2)
    Requirement already satisfied: grpcio<2.0dev,>=1.38.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (1.47.0)
    Requirement already satisfied: python-dateutil<3.0dev,>=2.7.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (2.8.2)
    Requirement already satisfied: requests<3.0.0dev,>=2.18.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (2.28.1)
    Requirement already satisfied: proto-plus<2.0.0dev,>=1.15.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (1.20.6)
    Requirement already satisfied: packaging<22.0.0dev,>=14.3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-bigquery) (21.3)
    Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.56.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (1.56.4)
    Requirement already satisfied: google-auth<3.0dev,>=1.25.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (2.9.1)
    Requirement already satisfied: grpcio-status<2.0dev,>=1.33.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (1.47.0)
    Requirement already satisfied: google-crc32c<2.0dev,>=1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-resumable-media<3.0dev,>=0.6.0->google-cloud-bigquery) (1.3.0)
    Requirement already satisfied: six>=1.5.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from grpcio<2.0dev,>=1.38.1->google-cloud-bigquery) (1.16.0)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from packaging<22.0.0dev,>=14.3->google-cloud-bigquery) (3.0.9)
    Requirement already satisfied: numpy>=1.16.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyarrow<9.0dev,>=3.0.0->google-cloud-bigquery) (1.23.1)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-bigquery) (1.26.10)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-bigquery) (2022.6.15)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-bigquery) (2.1.0)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-cloud-bigquery) (3.3)
    Requirement already satisfied: cachetools<6.0,>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (5.2.0)
    Requirement already satisfied: rsa<5,>=3.1.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (4.7.2)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (0.2.8)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0dev,>=1.25.0->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-cloud-bigquery) (0.4.8)
    Requirement already satisfied: importlib-resources in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (5.8.0)
    Requirement already satisfied: zipp>=3.1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from importlib-resources) (3.8.1)
    Requirement already satisfied: pytest in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (7.1.2)
    Requirement already satisfied: packaging in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pytest) (21.3)
    Requirement already satisfied: py>=1.8.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pytest) (1.11.0)
    Requirement already satisfied: iniconfig in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pytest) (1.1.1)
    Requirement already satisfied: attrs>=19.2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pytest) (21.4.0)
    Requirement already satisfied: pluggy<2.0,>=0.12 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pytest) (1.0.0)
    Requirement already satisfied: tomli>=1.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pytest) (2.0.1)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from packaging->pytest) (3.0.9)
    Requirement already satisfied: greenlet in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.1.2)
    Requirement already satisfied: azure-storage-blob in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (12.13.0)
    Requirement already satisfied: azure-core<2.0.0,>=1.23.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-storage-blob) (1.24.2)
    Requirement already satisfied: cryptography>=2.1.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-storage-blob) (37.0.4)
    Requirement already satisfied: msrest>=0.6.21 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-storage-blob) (0.7.1)
    Requirement already satisfied: requests>=2.18.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-core<2.0.0,>=1.23.1->azure-storage-blob) (2.28.1)
    Requirement already satisfied: six>=1.11.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-core<2.0.0,>=1.23.1->azure-storage-blob) (1.16.0)
    Requirement already satisfied: typing-extensions>=4.0.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from azure-core<2.0.0,>=1.23.1->azure-storage-blob) (4.3.0)
    Requirement already satisfied: cffi>=1.12 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cryptography>=2.1.4->azure-storage-blob) (1.15.1)
    Requirement already satisfied: isodate>=0.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrest>=0.6.21->azure-storage-blob) (0.6.1)
    Requirement already satisfied: requests-oauthlib>=0.5.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrest>=0.6.21->azure-storage-blob) (1.3.1)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from msrest>=0.6.21->azure-storage-blob) (2022.6.15)
    Requirement already satisfied: pycparser in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cffi>=1.12->cryptography>=2.1.4->azure-storage-blob) (2.21)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.18.4->azure-core<2.0.0,>=1.23.1->azure-storage-blob) (2.1.0)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.18.4->azure-core<2.0.0,>=1.23.1->azure-storage-blob) (3.3)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests>=2.18.4->azure-core<2.0.0,>=1.23.1->azure-storage-blob) (1.26.10)
    Requirement already satisfied: oauthlib>=3.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests-oauthlib>=0.5.0->msrest>=0.6.21->azure-storage-blob) (3.2.0)
    Requirement already satisfied: jsonschema in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.7.2)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from jsonschema) (0.18.1)
    Requirement already satisfied: importlib-resources>=1.4.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from jsonschema) (5.8.0)
    Requirement already satisfied: attrs>=17.4.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from jsonschema) (21.4.0)
    Requirement already satisfied: zipp>=3.1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from importlib-resources>=1.4.0->jsonschema) (3.8.1)
    Requirement already satisfied: pluggy in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.0.0)
    Requirement already satisfied: tqdm in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (4.64.0)
    Requirement already satisfied: pyopenssl in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (22.0.0)
    Requirement already satisfied: cryptography>=35.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyopenssl) (37.0.4)
    Requirement already satisfied: cffi>=1.12 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cryptography>=35.0->pyopenssl) (1.15.1)
    Requirement already satisfied: pycparser in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from cffi>=1.12->cryptography>=35.0->pyopenssl) (2.21)
    Requirement already satisfied: platformdirs in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.5.2)
    Requirement already satisfied: s3fs in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2022.5.0)
    Requirement already satisfied: fsspec==2022.5.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from s3fs) (2022.5.0)
    Requirement already satisfied: aiohttp<=4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from s3fs) (3.8.1)
    Requirement already satisfied: aiobotocore~=2.3.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from s3fs) (2.3.4)
    Requirement already satisfied: wrapt>=1.10.10 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiobotocore~=2.3.0->s3fs) (1.14.1)
    Requirement already satisfied: botocore<1.24.22,>=1.24.21 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiobotocore~=2.3.0->s3fs) (1.24.21)
    Requirement already satisfied: aioitertools>=0.5.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiobotocore~=2.3.0->s3fs) (0.10.0)
    Requirement already satisfied: aiosignal>=1.1.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp<=4->s3fs) (1.2.0)
    Requirement already satisfied: attrs>=17.3.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp<=4->s3fs) (21.4.0)
    Requirement already satisfied: multidict<7.0,>=4.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp<=4->s3fs) (6.0.2)
    Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp<=4->s3fs) (2.1.0)
    Requirement already satisfied: yarl<2.0,>=1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp<=4->s3fs) (1.7.2)
    Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp<=4->s3fs) (4.0.2)
    Requirement already satisfied: frozenlist>=1.1.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiohttp<=4->s3fs) (1.3.0)
    Requirement already satisfied: typing_extensions>=4.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aioitertools>=0.5.1->aiobotocore~=2.3.0->s3fs) (4.3.0)
    Requirement already satisfied: urllib3<1.27,>=1.25.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.24.22,>=1.24.21->aiobotocore~=2.3.0->s3fs) (1.26.10)
    Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.24.22,>=1.24.21->aiobotocore~=2.3.0->s3fs) (1.0.1)
    Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from botocore<1.24.22,>=1.24.21->aiobotocore~=2.3.0->s3fs) (2.8.2)
    Requirement already satisfied: idna>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from yarl<2.0,>=1.0->aiohttp<=4->s3fs) (3.3)
    Requirement already satisfied: six>=1.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.24.22,>=1.24.21->aiobotocore~=2.3.0->s3fs) (1.16.0)
    Requirement already satisfied: tabulate in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.8.10)
    Requirement already satisfied: frozenlist in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.3.0)
    Requirement already satisfied: aiosignal in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.2.0)
    Requirement already satisfied: frozenlist>=1.1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from aiosignal) (1.3.0)
    Requirement already satisfied: asn1crypto in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.5.1)
    Requirement already satisfied: pyrsistent in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.18.1)
    Requirement already satisfied: toml in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.10.2)
    Requirement already satisfied: filelock in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.7.1)
    Requirement already satisfied: flask in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.1.3)
    Requirement already satisfied: click>=8.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from flask) (8.1.3)
    Requirement already satisfied: itsdangerous>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from flask) (2.1.2)
    Requirement already satisfied: importlib-metadata>=3.6.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from flask) (4.12.0)
    Requirement already satisfied: Jinja2>=3.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from flask) (3.1.2)
    Requirement already satisfied: Werkzeug>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from flask) (2.1.2)
    Requirement already satisfied: zipp>=0.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from importlib-metadata>=3.6.0->flask) (3.8.1)
    Requirement already satisfied: MarkupSafe>=2.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from Jinja2>=3.0->flask) (2.1.1)
    Requirement already satisfied: websocket-client in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.3.3)
    Requirement already satisfied: google-cloud-core in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.3.2)
    Requirement already satisfied: google-auth<3.0dev,>=1.25.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-core) (2.9.1)
    Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-cloud-core) (2.8.2)
    Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.56.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6->google-cloud-core) (1.56.4)
    Requirement already satisfied: requests<3.0.0dev,>=2.18.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6->google-cloud-core) (2.28.1)
    Requirement already satisfied: protobuf<5.0.0dev,>=3.15.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6->google-cloud-core) (3.19.4)
    Requirement already satisfied: rsa<5,>=3.1.4 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-core) (4.7.2)
    Requirement already satisfied: pyasn1-modules>=0.2.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-core) (0.2.8)
    Requirement already satisfied: cachetools<6.0,>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-core) (5.2.0)
    Requirement already satisfied: six>=1.9.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-auth<3.0dev,>=1.25.0->google-cloud-core) (1.16.0)
    Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from pyasn1-modules>=0.2.1->google-auth<3.0dev,>=1.25.0->google-cloud-core) (0.4.8)
    Requirement already satisfied: charset-normalizer<3,>=2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6->google-cloud-core) (2.1.0)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6->google-cloud-core) (1.26.10)
    Requirement already satisfied: idna<4,>=2.5 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6->google-cloud-core) (3.3)
    Requirement already satisfied: certifi>=2017.4.17 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.6->google-cloud-core) (2022.6.15)
    Requirement already satisfied: google-resumable-media in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.3.3)
    Requirement already satisfied: google-crc32c<2.0dev,>=1.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from google-resumable-media) (1.3.0)
    Requirement already satisfied: future in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (0.18.2)
    Requirement already satisfied: azure-common in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.1.28)
    Requirement already satisfied: scikit-learn in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (1.1.1)
    Requirement already satisfied: scipy>=1.3.2 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from scikit-learn) (1.8.1)
    Requirement already satisfied: threadpoolctl>=2.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from scikit-learn) (3.1.0)
    Requirement already satisfied: joblib>=1.0.0 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from scikit-learn) (1.1.0)
    Requirement already satisfied: numpy>=1.17.3 in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (from scikit-learn) (1.23.1)
    Requirement already satisfied: pygments in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.12.0)
    Requirement already satisfied: itsdangerous in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (2.1.2)
    Requirement already satisfied: openpyxl in /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages (3.0.10)
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
    15 files from aiosignal added
    33 files from argon2 added
    1 files from asgiref added
    3 files from asn1crypto added
    35 files from asttokens added
    25 files from astunparse added
    12 files from async_generator added
    16 files from async_timeout added
    29 files from attrs added
    1 files from awscli added
    1 files from azure added
    1 files from azure added
    1 files from azure added
    3 files from backcall added
    20 files from backports.zoneinfo added
    2215 files from bs4 added
    35 files from beir added
    11 files from bleach added
    85 files from boto3 added
    111 files from botocore added
    198 files from cachetools added
    5 files from certifi added
    90 files from cffi added
    16 files from chardet added
    124 files from charset_normalizer added
    628 files from click added
    30 files from colorama added
    417 files from cryptography added
    18 files from cycler added
    1491 files from datasets added
    22 files from debugpy added
    28 files from decorator added
    18 files from defusedxml added
    98 files from dill added
    6 files from django added
    27 files from docutils added
    1101 files from elasticsearch added


    2022-07-27 16:44:13.790948: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'libcudart.so.11.0'; dlerror: libcudart.so.11.0: cannot open shared object file: No such file or directory
    2022-07-27 16:44:13.791032: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.


    131 files from eli5 added
    83 files from entrypoints added
    2 files from et_xmlfile added
    1 files from execnb added
    30 files from executing added
    8255 files from faiss added
    1 files from fastcore added
    290 files from fastjsonschema added
    20 files from fastrelease added
    50 files from filelock added
    473 files from flask added
    146 files from flatbuffers added
    4 files from fontTools added
    49 files from frozenlist added
    190 files from fsspec added
    1 files from future added
    126 files from gast added
    1 files from ghapi added
    4 files from google added
    4 files from google added
    3 files from google_auth_oauthlib added
    48 files from google added
    48 files from google added
    48 files from google added
    48 files from google added
    14 files from google_crc32c added
    7 files from pasta added
    48 files from google added
    48 files from google added
    197 files from graphviz added
    21 files from greenlet added
    522 files from grpc added
    1 files from grpc_status added
    77 files from h11 added
    236 files from h5py added
    251 files from huggingface_hub added
    43 files from idna added
    260 files from importlib_metadata added
    28 files from importlib_resources added
    18 files from iniconfig added
    5 files from install added
    149 files from ipykernel added
    1470 files from IPython added
    1 files from ipython_genutils added
    10050 files from ipywidgets added
    37 files from isodate added
    158 files from itsdangerous added
    1306 files from jedi added
    233 files from jinja2 added
    6 files from jmespath added
    168 files from joblib added
    170 files from jsonschema added
    1 files from jupyter added
    1604 files from jupyter_client added
    1 files from jupyter_console added
    4 files from jupyter_core added
    2 files from jupyterlab_pygments added
    1 files from jupyterlab_widgets added
    26273 files from keras added
    5 files from keras_preprocessing added
    50 files from kiwisolver added
    1 files from clang added
    222 files from lightgbm added
    3 files from lxml added
    53 files from markdown added
    95 files from markupsafe added
    201 files from matplotlib added
    1 files from matplotlib_inline added
    177 files from mistune added
    218 files from msrest added
    10 files from msrestazure added
    188 files from multidict added
    73 files from multiprocess added
    128 files from nbclient added
    3938 files from nbconvert added
    380 files from nbdev added
    214 files from nbformat added
    6 files from nest_asyncio added
    7703 files from nltk added
    3 files from notebook added
    7299 files from numpy added
    1670 files from oauthlib added
    2896 files from cv2 added
    930 files from openpyxl added
    41 files from opt_einsum added
    31 files from outcome added
    1 files from packaging added
    6900 files from pandas added
    87 files from pandocfilters added
    23 files from parso added
    114 files from pexpect added
    39 files from pickleshare added
    9 files from PIL added
    3 files from pip added
    94 files from platformdirs added
    52 files from pluggy added
    187 files from prometheus_client added


    /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils.
      warnings.warn("Setuptools is replacing distutils.")


    1332 files from prompt_toolkit added
    107 files from proto added
    48 files from google added
    243 files from psutil added
    80 files from psycopg2 added
    92 files from ptyprocess added
    16 files from pure_eval added
    1 files from py added
    2843 files from pyarrow added
    1 files from pyasn1 added
    1 files from pyasn1_modules added
    343 files from pycparser added
    136 files from pygments added
    97 files from jwt added
    1 files from OpenSSL added
    6736 files from pyparsing added
    337 files from pyrsistent added
    147 files from socks added
    64 files from sockshandler added
    71 files from pytest added
    145 files from dateutil added
    10 files from pytrec_eval added
    2 files from pytrec_eval_ext added
    71 files from pytz added
    2789 files from yaml added
    506 files from zmq added
    1 files from qtconsole added
    12 files from qtpy added
    42 files from regex added
    192 files from requests added
    114 files from requests_oauthlib added
    126 files from responses added
    61 files from rsa added
    213 files from s3fs added
    111 files from s3transfer added
    60 files from sacremoses added
    2710 files from sklearn added
    4083 files from scipy added
    1 files from selenium added
    11 files from send2trash added
    1614 files from sentence_transformers added
    189 files from sentencepiece added
    227 files from setuptools added
    64 files from six added
    2710 files from sklearn added
    6 files from sniffio added
    211 files from sortedcontainers added
    42 files from soupsieve added
    5090 files from sqlalchemy added
    60 files from sqlparse added
    119 files from stack_data added
    81 files from tabulate added
    89 files from tensorboard added
    3 files from tensorboard_data_server added
    1 files from tensorboard_plugin_wit added
    19532 files from tensorflow added
    15 files from tensorflow_estimator added
    121 files from tensorflow_io added
    --------------- error during tensorflow-io-gcs-filesystem documentation extracting
    5 files from termcolor added
    265 files from terminado added
    1 files from bin added
    --------------- error during theano documentation extracting
    76 files from threadpoolctl added
    21 files from tinycss2 added
    1 files from tk added
    923 files from tokenizers added
    116 files from toml added
    8 files from tomli added


    /home/satoru/projects/text-retrieval/my_project_env/lib/python3.8/site-packages/torch/distributed/distributed_c10d.py:181: UserWarning: torch.distributed.reduce_op is deprecated, please use torch.distributed.ReduceOp instead
      warnings.warn(


    66157 files from torch added
    7591 files from torchvision added
    2 files from tornado added
    165 files from tqdm added
    1894 files from traitlets added
    370 files from trio added
    70 files from trio_websocket added
    158 files from typing added
    231 files from urllib3 added
    6 files from wcwidth added
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
