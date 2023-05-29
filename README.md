# Zeply Backend Test
### Description

I defined a REST API for generating valid cryptocurrency addresses and displaying them.   Specifically, the API provide three endpoints, as follows:
- Generate Address
- List Address 
- Retrieve Address


## How to run the project

### Localy

to run the project locally, you need :
- Python and SQLite3 
- install the requirments.txt file 
 ```sh
python -r requirements.txt
 ```
- you can try to migrate (under the project root)
 ```sh
python manage.py migrate 
 ```
 - run the project
 ```sh
python manage.py runserver 
 ```
### Coins
 - To add coins : 
 - inside folder Bucket, inherite the class Coin under the same package
 - add the coin in variable COINS under Django Settings

## Endpoint Description
 - access to swagger : 
>http://127.0.0.1:8000/swagger/

## Endpoint Description
- please note that The PrivateKey is generated in incremental order.