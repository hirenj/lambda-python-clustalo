# Lambda implementation of Clustal Omega

Wrapping Clustal Omega in python-clustalo, wrapped in a lambda function for AWS.

## Building

Build python-clustalo and clustal omega in a docker container, and then take the generated egg file and unzip into the clustalo directory.

## Deploy function
```
    zip -r deploy.zip align_sequences.py clustalo
```