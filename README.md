# frejun-interview-project

## Task to be completed
- Create Signup, Login and Logout APIs (No frontend needed)
- Create an upload API using which you can upload a CSV file and create Candidate (Name, Phone number) objects in the database
  Note: These candidates should be created with respect to the user.
- Create an API to obtain these candidates with pagination as 10.

# Installation

creating virtualenv and install requirement
<pre> python3 -m venv env </pre>

<pre> pip install -r requirements.txt </pre>

# Running celery ( make sure rabbitmq/redis is working )
<pre> celery -A config worker -l info</pre>

# APIs

## Register api 
<pre>
curl -X POST \
  'http://127.0.0.1:8000/api/user/register/' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)' \
  --form 'username="developer"' \
  --form 'email="ddd@gmail.com"' \
  --form 'password="vinayak1@"' \
  --form 'password2="vinayak1@"'
</pre>

![Screenshot from 2021-07-30 02-45-54](https://user-images.githubusercontent.com/33996594/127600126-e2619622-48af-430c-94a4-8756e864bc96.png)



## Login api

<pre>
curl -X POST \
  'http://127.0.0.1:8000/api/user/login/' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)' \
  -H 'Authorization: Token 316e7a138d986b54acce3e4dfb64e5f61f254cec' \
  --form 'username="vinayak"' \
  --form 'password="vinayak"'
</pre>

![Screenshot from 2021-07-30 02-46-21](https://user-images.githubusercontent.com/33996594/127600157-bd3ecd1e-e764-4cf2-b405-2c53124ada84.png)



## upload csv file (gives error responce if any other formant)
make sure you have celery running

<pre>
curl -X PUT \
  'http://127.0.0.1:8000/api/candidate/upload/' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)' \
  -H 'Authorization: Token 74c07c1660babb615c5ad87a752c3dd7c6a9adef' \
  -F 'file=@/home/vinayak/config/example_v.csv'
</pre>

![Screenshot from 2021-07-30 02-47-37](https://user-images.githubusercontent.com/33996594/127600203-9c566d63-51b2-432c-a4f0-04298a0fec46.png)


## Show candidate api with pagination 10

<pre>
 curl -X GET \
  'http://127.0.0.1:8000/api/candidate/show/' \
  -H 'Accept: */*' \
  -H 'User-Agent: Thunder Client (https://www.thunderclient.io)' \
  -H 'Authorization: Token 74c07c1660babb615c5ad87a752c3dd7c6a9adef'
</pre>

![Screenshot from 2021-07-30 02-47-05](https://user-images.githubusercontent.com/33996594/127600223-2f6c7af8-48f1-4cdb-9e01-620a08ca49a0.png)


### for speeding up and to optimize the creation of object in database with minimum hits. I have used <b> .bulk_create(obj) </b> method which hits database only once

code used :
<pre>
 with transaction.atomic():
        Candidate.objects.bulk_create(obj)
</pre>
