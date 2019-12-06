


# Tools for analytics Project

**Group name**: Project Group 27
**Team members**: Ying Gu, Yiwen Sun
**UNIs**: [yg2689, ys3292]
**Section:** 001

## What We've Implemented

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

 **/map**
 
 **/sightings**
 
 **/sightings/(unique-squirrel-id)**
 
 **/sighintgs/add**
 
 **/sightings/stats**
 
## Dependencies

* [Django](https://maven.apache.org/) - Dependency Management
* [Bootstrap](https://maven.apache.org/) - Dependency Management
* [Jquery](https://rometools.github.io/rome/) - Used to generate RSS Feeds
* [BootstrapValidator](https://rometools.github.io/rome/) - Used to generate RSS Feeds
* [SQlite](https://rometools.github.io/rome/) - Used to generate RSS Feeds
* [Django Leaflet](https://django-leaflet.readthedocs.io/en/latest/) - Used to generate map views

## Authors

* **Ying Gu** - * management commands, update, add, delete, all sightings * - 
* **Yiwen Sun** - * map, stats * - 
