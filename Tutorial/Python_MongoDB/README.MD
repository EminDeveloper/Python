# Write application logs into MongoDB.


**Step 1.**
First of all create you own virtual enviroment in your machine. How to do this?
Solution:
- Install venv into machine:
`python -m venv env`
- Go to virtual enviroment path.
- Activate virtual enviroment: 
`env\Scripts\activate`
- May be you want, you can deactive virtual enviroment:
`deactivate`

**Step 2.**
Install pymongo into machine:

`python -m pip install pymongo`

**Step 3.**
Get MongoDB url, username, password. Maybe your using MongoDB running in you local machine.
For example can get this information:
` URL: http://localhost:27017/`


**Step 4.**
For example let's, run MongoDB in a docker container:

```yml
version: '3.8'
services:
  mongodb:
    image: mongo
    container_name: mongodb
    ports:
      - '27017:27017'
    volumes:
      - 'data:/data'
    environment:
      - MONGO_INITDB_ROOT_USERNAME=rootuser
      - MONGO_INITDB_ROOT_PASSWORD=rootpass
  mongo-express:
    image: mongo-express
    container_name: mongo-express
    restart: always
    ports:
      - '8081:8081'
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=rootuser
      - ME_CONFIG_MONGODB_ADMINPASSWORD=rootpass
      - ME_CONFIG_MONGODB_SERVER=mongodb
volumes:
  data: {}
networks:
  default:
    name: mongodb_network
```



**Step 5.**
Create collection in MongoDB for stored application logs.
For example(Your MongoDB located in Docker container.):

- First, ensure that your MongoDB container is running. You can use the following command to access the MongoDB shell within the Docker container:

`docker ps`

`docker exec -it 7b9df05a9d63  //bin//bash`

- Now you come on linux machine.
- Log in to the MongoDB shell.:

`mongosh mongodb://localhost:27017 -u rootuser -p rootpass`

`show dbs;`

- In the MongoDB shell, you can create a new database using the `use` command. For example, to create a database called **"applogdb":**
`use applogdb`


Example collection format:
```mongodb
{
  "image_path": "/path/to/image.jpg",
  "image_name": "image.jpg",
  "image_size": "2.5 MB",
  "method_used": "base64",
  "AI_prompt_message": "Analyzing image for object recognition",
  "AI_response": {
    "recognized_object": "cat",
    "confidence_level": 0.87
  }
}
```


