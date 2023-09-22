# Study Case Soul Parking - To Do List

## Feature

| Route             	| Method 	| Description      	|
|-------------------	|--------	|------------------	|
| /todo             	| POST   	| Create todo      	|
| /todo             	| GET    	| Get all todo     	|
| /todo/\<id>        	| GET    	| Get todo by ID   	|
| /todo/\<id>        	| PUT    	| Update todo      	|
| /todo/\<id>/finish 	| POST   	| Finish todo      	|
| /todo/\<id>        	| DELETE 	| Soft delete todo 	|

## Data Object
### Classname: TodoList

| Attribute   	| Description   	|
|-------------	|---------------	|
| Id          	| Unique Id     	|
| title       	|               	|
| description 	|               	|
| finished_at 	| Finished time 	|
| created_at  	| Created time  	|
| updated_at  	| Updated time  	|
| deleted_at  	| Deleted_time  	|


## Requirements
- Python 3

## How to start
### 1. Linux
```bash 
pip install virtualenv # for environment
python3 -m virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
python3 run main.py
```