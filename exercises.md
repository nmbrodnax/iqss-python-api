## Introduction to Using APIs with Python
[NaLette Brodnax](http://www.nalettebrodnax.com)<br>


## Workshop Exercises

### Part 1: Introduction

 1. Complete the one-minute poll at [bit.ly/dsspoll](http://bit.ly/dsspoll). Click [here](https://github.com/nmbrodnax/iqss-python-api/tree/master/files) to access the files for the workshop.  
 
### Part 3: Simple API

 1. Search for an institution from the [Integrated Postsecondary Education Data System](https://nces.ed.gov/ipeds/datacenter/InstitutionByName.aspx).  Click to expand *Institution Characteristics* and make note of the `UnitID`.

 2. Review the [API documentation](https://github.com/DataUSA/datausa-api/wiki/Data-API) for the IPEDS data available from [DataUSA](https://datausa.io).

 3. Modify the script `ipeds_api.py` by replacing the `UnitID` on Row 19 with the `UnitID` for the institution you wish to query.  You can also change the variables returned based on what is available (see the [API documentation](https://github.com/DataUSA/datausa-api/wiki/Data-API#ipeds)).
 
 ### Part 4: Authentication
 
 1. Register as a developer to access the Google Maps API: [https://developers.google.com/maps/documentation/geocoding/start](https://developers.google.com/maps/documentation/geocoding/start).

     

 2. Go to **Web Services > Geocoding API**.  Click *GET A KEY* in the upper right-hand corner.  Copy your key to a plain text file called `google_auth.txt` and save it in the same directory as your script.

    Your script and authorization document (the text file with your API key) must be in the same directory, and filename must match what is provided in your script.  When you run the script, it should display your API key.

 3. Enter the following into a browser, replacing `<my_api_key>` with your key.

    ```
    https://maps.googleapis.com/maps/api/geocode/json?address=1737+Cambridge+St,
    +Cambridge,+MA+02138&key=<my_api_key>
    ```

