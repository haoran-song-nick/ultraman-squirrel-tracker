# Squirrel Tracker
This is an app that keeps track of all the known squirrels starts with Central Park. It is built with functions to import the 2018 Central Park Squirrel Census data and allows to add, update and view the squirrel data.

## Functions
There are two management commands:
- import_squirrel_data
  * import data (in CSV format) to the database
- export_squirrel_data
  * export data in CSV format
 
## Views
There are five views:
- Map
  * located at: */map*
  * displays the 100 location of the squirrel sightings on an OpenStreets map
- List of all sightings
  * located at: */sightings*
  * lists all squirrel sightings with links to edit each and a single link to the “add” sighting view
- Update
  * located at: */sightings/<unique-squirrel-id>*
  * updates a particular sighting providing unique-squirrel-id
- Add
  * located at: */sightings/add*
  * create new sightings
  * fields supported: Fields supported: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent, Runs from
- Stats
  * located at: */sightings/stats*
  * shows general stats about the sightings
   
## Group Name
Project Ultraman, Section 3(?)

## UNIs
UNIs: [jl5772, hs3229]

## Link to server
空缺！！
