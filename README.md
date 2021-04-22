# VFOB
Vanderbilt ME#9 Senior Design Team Code Repo


Run Instructions:
- Clone repository to raspberry pi
- Run main.py

main.py:
- Main first checks location and distance, then moves to that location
- Main receives and sends distance/location to second pi
- Main acts as server and executer

Selected Library Files:
- Bolt_finder.py:
    - Class objectdet finds and returns coordinates of a bolt within the camera view
    - Run function profit() to find bolt
- Combined.py
    - Class BoltState contains get and set methods for a “state” of the bolt location. Also contains function to run the car towards the bolt.
    - Class Ultrasonic is contained with combined.py for simplification, this class gets the distance to the bolt from the ultrasonic sensor
