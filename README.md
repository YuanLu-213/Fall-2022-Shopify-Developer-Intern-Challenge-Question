# Fall-2022-Shopify-Developer-Intern-Challenge-Question
This repo contains the code for the Fall 2022 Shopify Developer Intern Challenge. The application is built with FLASK, and in order to run the application please install FLASK and python3.

The appliication is a simple inventory tracking and managemeny system where administrator can create new item to the inventory, edit existing item, view the list of all items in the inventory, and also delete item from the inventory with a deletion comment. It also enable administrator to view the history of deletions that have been made and undo them.

The database for this application is coded in the backend. However, it is totally feasible to work with whatever databases the inventory uses.

To run the application, open a terminal in the folder where the code files are located and run the following commands:

export FLASK_APP=server.py

Because Replit only runs flask projects on host "0.0.0.0", we will use following command to run it on the correct host

flask run -h 0.0.0.0


When the browser opens up in the Replit window, the layout is changed due to the limited size of the window. Please open it in a new tab or enlarge the window by dragging the sides of the window to see the correct layout.