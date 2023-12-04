# pulumi-localstack-demo

## keep in mind

- dont create a custom provider object in the executed code. this will override the stack config and cause difficult to debug errors.

## setup

``` bash

# start local stack
localstack start

# this holds the pulumi state locally so you dont have to login
pulumi login --local

# activate python venv
cd src && source venv/bin/activate

pulumi up
```