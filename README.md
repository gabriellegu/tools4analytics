


# Tools for analytics Project

**Group name**: Project Group 27
**Team members**: Ying Gu, Yiwen Sun
**UNIs**: [yg2689, ys3292]
**Section:** 001

## What we've implemented

### Management commands

We have implemented the management commands of importing CSV file and exporting to CSV file.

Import:
```
python manage.py import_squirrel_data /path/to/file.csv
```

Export:
```
python manage.py export_squirrel_data /path/to/file.csv
```
## Views
We have implemented the views listed as below.

 **/map**: Show map. Plot 50 randomly selected squirrel sightings.
 **/sightings**:Show all sightings (like a spreadsheet, with operations) with a paginator at the end of the page.
 **/sightings/(unique-squirrel-id)** :Update or delete, based on its method.
 Since uniqueID is concatenated by hectare, shift, date and hectareNum, these 4 fields are supported while uniqueID is not directly supported. Validate the data using bootstrapValidator.
 **/sightings/add**: Add new sightings
 **/sightings/stats**: Stats page 

We also implemented query by uniqueID. 
 
## Dependencies

* [Django](https://www.djangoproject.com) - 2.2.7 - The Web Framework
* [Bootstrap](https://getbootstrap.com) - v4.3.1 - For styling
* [Jquery](https://jquery.com) - 3.4.1 - Javascript Library
* [BootstrapValidator](http://bootstrapvalidator.votintsev.ru/) - v0.5.2 - Used to validate from fields
* [SQlite](https://www.sqlite.org/) - 3.30.0 - Database
* [Django Leaflet](https://django-leaflet.readthedocs.io/en/latest/) - 1.5.1 - Used to generate map views

## Authors

* **Ying Gu** - management commands, update, add, delete, all sightings - 
* **Yiwen Sun** - map, stats - 
