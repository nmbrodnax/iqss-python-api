## Introduction to Using APIs with Python
[NaLette Brodnax](http://www.nalettebrodnax.com)<br>


## Workshop Exercises

 1. Complete the one-minute poll at [bit.ly/dsspoll](http://bit.ly/dsspoll)

 2. Search for an institution from the [Integrated Postsecondary Education Data System](https://nces.ed.gov/ipeds/datacenter/InstitutionByName.aspx).  Click to expand *Institution Characteristics* and make note of the `UnitID`.

 3. Review the [API documentation](https://github.com/DataUSA/datausa-api/wiki/Data-API#ipeds) for the IPEDS data available from [DataUSA](https://datausa.io).

 4. Modify the script `ipeds_api.py` by replacing the `UnitID` on Row 23 with the `UnitID` for the institution you wish to query.  You can also change the variables returned based on what is available (see the [API documentation](https://github.com/DataUSA/datausa-api/wiki/Data-API#ipeds)).

 5. Run your script from the IDE or from the command line.