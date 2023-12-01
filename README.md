![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Track-Your-Weight

Track Your Weight is a terminal tool, that runs in the Code Institute mock terminal on Heroku.

Track Your Weight allows the user to enter their old weight and their new weight in a easy way, the tool will then calculate and tell the user how much weight the user have lost or gained.

Track Your Weight will also add the user weight inputs and weight difference to a gooogle spreadsheet.

[Link to spreadsheet](https://docs.google.com/spreadsheets/d/1lWFG9SQwQRJ0U6RkMB9GRJZyBvwutzNW-z8vFAwBce4/edit#gid=901748384)

[Link to Track Your Weight](https://track-your-weight-2b6009af9b3e.herokuapp.com/)

![picture of Track Your Weight](/assets/images/Ui-dev.png)


## Tabel Of Content

[Track Your Weight](#Track-Your-Weight)

[Features](#Features)

[Testing](#Testing)

[Technologies Used](#Technologies-Used)

[Deployment](#Deployment)

[Credits](#Credits)

## Features

Track Your Weight is connected to a google spreadsheet named track-your-weight, the spreadsheet has 3 different worksheets, Old, New and difference.

The 'Old' worksheet contain all the inputs of old weights.

The 'New' worksheet contain all the inputs of new weights.

The 'Difference' worksheet contain the difference between old weight and new weight

 (Old weight - New weight = Difference). 

* The first thing the user will see is a welcome message, and being asked to input their old weight.

![Picture of welcome message and to input old weight](/assets/images/welcome.png)

* When the user has entered their input of their old weight, the track-your-weight spreadsheet will be updated and the user will be asked to input their new weight.

![picture of input new weight](/assets/images/new.png)

* When the new weight input has been entered successfully the track-your-weight spreadsheet will be updated once again.

* After both weight inputs has been entered succesfully, the user will be given their result of how much weight they have gained or lost. Which also will be updated to the spreadsheet.

![picture of result](/assets/images/result.png)

* If the input entered is invalid the user will get an error message and be asked to enter their weight again.

Here is a example where I typed in 'wrong'.

![picure of error message](/assets/images/wrong.png)

### Features to add

* One feature I would likke to add is to give the users a choice to enter their name so it is easy to keep track in the spreadsheet. or give the user the opportunity to input the date so they can see when they updated the spreasheet.

## Testing

I have conducted testing by giving it all sorts of differnt inputs valid and invalid, both before deployment and after it.

The code has been tested in PEP8 and their is no errors.

### Bugs

#### Resolved Bugs

* I had a problem with updating the difference worksheet, but after staring at the code for quite a while I could see that it was a typo.

Bugged line:

difference.worksheet = SHEET.worksheet("difference")

fixed line:

difference_worksheet = SHEET.worksheet("difference")

* I got this comment in PEP8, 98: E501 line too long (85 > 79 characters).

I managed to fixed that by changing this line:

print(f"You have {'gained' if difference > 0 else 'lost'} {abs(difference)} Kg.")

to this:

print(f"You have {'gained' if difference > 0 else 'lost'} "
      
      f"{abs(difference)} Kg.")



#### Remaning Bugs

* No bugs currently.

### Validation

* No errors on PEP8.

## Technologies-Used


## Deployment


## Credits
* Code Institute for deployment terminal

* Code Institute [Love Sandwiches](https://github.com/Code-Institute-Org/p3-template)
were very helpful by making me understand how to write the code for this project.