# patients

This repo was created to hold my current portfolio project that creates a database using PostgreSQL to hold patient information, including their glasses and contact lens prescriptions, if active.
I've been halted by a few problems, such as completing my API for appropriate HTTP requests (GET, POST, PUT), but I'm still determined to continue and adding more features to this project.

Update 1/29/2023:
I have successfully completed my server and API functionality to POST and GET my prescriptions and patients information, even through an ID request with the appropriate URL endpoint. The most challenging part was connecting the relations between prescriptions and patients, but after I did a bit of database revision, I realized I had a column missing with the appropriate constraints. After this issue was cleared, my applicatin has been running smoothly.
My next task is to display each patient's respective prescription when calling their ID through the GET request. I don't think this will cause problems due to the relations being appropriately established, but I plan on adding more features as I go.
