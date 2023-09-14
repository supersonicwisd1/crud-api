# How to run crud-api
- visit `https://crud-api-xuko.onrender.com/api`
- execute CRUD operation on it.
  
## Create Operation
A new user can be created. The details of the person are:
- name
- email
- track
- gender
- github_profile
- password
### endpoint
send a create action to 
`https://crud-api-xuko.onrender.com/api`
  
## Read ALl user at once 
You can read all users at once but a function to view numbers of users is available. 
You can select the limit of users you want and skip to a particular ID of a user
### endpoint
sent a read action to 
`https://crud-api-xuko.onrender.com/api`

## Read one a user at a time
A user detail can be fetched using the user's name. 
All names going into the DB are unique because of the instruction that a name may be passed to fetch user details
### endpoint
send a read action to 
`https://crud-api-xuko.onrender.com/api/{user_name}`

## Delete user
A user can be deleted using the user name. It is a bad practice but the instruction states that a name may be passed to fetch user details
### endpoint
send a delete action to 
`https://crud-api-xuko.onrender.com/api/{user_name}`

## Update user
A user can be updated using the user name. It is a bad practice but the instruction states that a name may be passed to fetch user details
### endpoint
send a delete action to 
`https://crud-api-xuko.onrender.com/api/{user_name}`

`Note:` You can test the API by visiting `https://crud-api-xuko.onrender.com/docs` . The API was built with FastAPI, therefore came with a pre-installed docs to test out the fuctionality of the api 
