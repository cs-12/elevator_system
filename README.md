
# Elevator-System-django

A challenge to implement the business logic for a simplified elevator model in Python. It decides whether the elevator should go up, go down, or stop. An elevator system, which can be initialised with N elevators and maintains the elevator states as well.


API Endpoints:

.Endpoint: `/elevator/elevator/`
      METHODS: [GET, POST]

   Example Payload for creating new elevator:

    {  
            "location": "main",  
            "current_floor": 0,  
            "destination_floor": null,  
            "direction": null,  
            "working": true,  
            "min_floor": 0,  
            "max_floor": 10,  
            "max_occupancy": 10,  
            "current_occupancy": 0,  
            "status": 1  
        }

.Endpoint: `/elevator/elevator/{elevator-id}`
       METHODS: [GET, DELETE, PUT]

    Example JSON Payload for update:
    {  
            "location": "main",  
            "current_floor": 0,  
            "destination_floor": null,  
            "direction": null,  
            "working": true,  
            "min_floor": 0,  
            "max_floor": 10,  
            "max_occupancy": 10,  
            "current_occupancy": 0,  
            "status": 1  
    }

.Endpoint: `/elevator/use/`
    METHODS: [POST]

   Example payload for using an elevator (elevator_name is optional, if id is not provided it is used) :

    {
        "elevator_id": 1,  
        "elevator_name": "main",  
        "current_floor": 1,
        "destination_floor": 7
    }

.Endpoint: `/elevator/maintainence/`
   METHODS: [POST]

   Example payload to put elevator in maintainance and in normal mode (action supports "start" and "finish") :

  {
    "elevator_id": 1,
    "action": "start"
  }



Running on local machine

1-Clone this project

https://github.com/cs-12/elevator_system.git

2-Create and activate a virtual environment (optional)

python -m venv venv
source venv/bin/activate

3-Install the python dependencies

pip install -r requirements.txt

4-run migrations to add tables to db

python manage.py migrate

5-Run the development server

python manage.py runerver 0.0.0.0:8000



