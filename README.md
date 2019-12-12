![Kickstart Coding Logo](./apps/core/static/images/logo.png)

# CodeBoard

The application for coders to collaborat on someone else's project or post project they started up for collaboration.

See latest version of the app ![here](http://www.codeboard.org)

### To run the app locally use the following steps:

1. Clone the repo
2. Have pipenv installed 
3. Enter the shell by running ```pipenv shell```
4. Install django and teh rest of teh development dependancies by running ```pipenv install --dev```
5. Update your django sqlite database by running ```python manage.py migrate```
6. Now finally, run the app with ```python manage.py```


#### Further development road could include:

Ability for a user to create groups/organizations, become members of those organizations and see what other projects memebers of same group collaboarte on. 
And even further development would include option of projects being closed to people outside of the group members.
