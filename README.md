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

[Flowchart](#flowchart)

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

## Flowchart

Here is a picture of the Flowchart I was using

![Picture of flowchart](/assets/images/Flowchart.png)

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

* [CodeAnywhere](https://app.codeanywhere.com)

* [VS Code](https://code.visualstudio.com)

* [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucidcharts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=354596046469&km_CPC_TargetID=kwd-84176206937&km_CPC_Country=2752&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=EAIaIQobChMIkuuH_fjuggMVVU-RBR0UMAI9EAAYASAAEgIV8vD_BwE)

[Github](https://github.com)

[Google Cloud](https://cloud.google.com/gcp?utm_source=google&utm_medium=cpc&utm_campaign=emea-se-all-en-bkws-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_500236818945-ADGP_Hybrid+%7C+BKWS+-+EXA+%7C+Txt+~+GCP+~+General%23v3-KWID_43700060393216001-aud-606988878614:kwd-6458750523-userloc_1012228&utm_term=KW_google+cloud-NET_g-PLAC_&&gad_source=1&gclid=CjwKCAiApaarBhB7EiwAYiMwqgUljs4RUwG9ctjd9bM7Ieav2Cl-Pyf9Tw01MDv8OSNhtL7vMaIYexoCcWcQAvD_BwE&gclsrc=aw.ds&hl=en)

[Google spreadsheet](https://docs.google.com/spreadsheets/u/0/?pli=1)

[Heroku](https://id.heroku.com/login)

## Deployment

Deployment was done using heroku.

1. first step is to login on heroku.
2. Then you press new and click on "create new app".
3. choose a name for your new app and choose a region.
4. Press settings and go down to config Vars
5. Click reveal Config vars and add on key named "PORT" and set it to "8000" then you add another one named "CREDS" and copy in your json credentials.
6. After that you go down to buildpack and add python and nodejs, it is very important to add python first.
7. then you go up and press deploy.
8. Use Github as deplyment method.
9. Type in the name of your github repository and click on it.
10. Go down to maual deploy and press "Deploy branch.

That is all the steps I took to deploy this site.

## Credits
* Code Institute for deployment terminal

* Code Institute [Love Sandwiches](https://github.com/Code-Institute-Org/p3-template)
were very helpful by making me understand how to write the code for this project.