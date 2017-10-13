## Introduction to Using APIs with Python
[NaLette Brodnax](http://www.nalettebrodnax.com)<br>


## Workshop Exercises

 1. Complete the one-minute poll at [bit.ly/dsspoll](http://bit.ly/dsspoll)

 2. Register as a developer to access the Google Maps API: [https://developers.google.com/maps/documentation/geocoding/start](https://developers.google.com/maps/documentation/geocoding/start).

     Go to Web Services > Geocoding API.  Click *GET A KEY* in the upper right-hand corner.  Copy your key to a text file and save it in the same directory as your IDE scripts.

 3. Enter the following into your script.

    ```python
    local_file = 'google_auth.txt'
    with open(local_file) as txtfile:
        my_key = txtfile.read()
    print("API Key: " + my_key)
    ```

    Be sure that your script and authorization document (the text file with your API key) are in the same directory, and that the filename is correct.  When you run the script, it should display your API key.

 4. Enter the following into a browser, replacing `<my_api_key>` with your key.

    ```
    https://maps.googleapis.com/maps/api/geocode/json?address=1737+Cambridge+St,
    +Cambridge,+MA+02138&key=<my_api_key>
    ```

[Click here](https://dss.iq.harvard.edu/workshop-materials) to download the code for all exercises.