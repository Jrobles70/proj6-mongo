# proj6-mongo
Simple webpage that prints out memos in a Mongo Database. User can add new memos or delete old ones.

## Requirements
A credentials.ini file is required with the following lines filled in

- DB : The name of your MongoDB database, which may include multiple collections
- DB_USER : A use name for your application.  
- DB_USER_PW : The password your application gives to access your database
- ADMIN_USER : The administrative user for your MongoDB
installation.  If you install MongoDB on your own computer, you need
this for creating a database.  You don't need it if you use a
cloud-hosted MongoDB service. 
- ADMIN_PW : Password for the administrative user.  You need this if
you use create_db.py to initialize your database.  You don't need it
if you use a cloud-hosted MongoDB service
- DB_HOST : The host computer on which your MongoDB database runs.  This
might be 'localhost' or it might be something like ds884198.mlab.com
- DB_PORT : The network port on which your MongoDB database listens.
  If you run MongoDB on your own computer, the default is 27017.  If
  you run MongoDB on MLab or a similar cloud service, it will be a port
  assigned by your cloud service. 

## Install
```
make install
```

## How to run
You must run the mongod server in order to connect to the database
If mongod is in your PATH use
```
mongod
```
Once the server is running open a new terminal and run
```
make run
```

# Known Bugs
I am making this last commit after the fact because I am not sure why my days are coming out wrong. I know this was mentioned
on the project page but I could not get it working correctly so I added in a temporary fix that displays the correct day.
The day displays now as yesterday so I shifted the days by 1.

# Author
* Justin Robles - Jrobles@uoregon.edu


