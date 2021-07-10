# Euro 2020 Predictor
### Video Demo:  
<https://www.youtube.com/watch?v=AfXmCmeTW3g>

### Description:  
A game based around the European Football Championship where users predict the scoreline of every match in the tournament and are awarded points based on the correctness of their predictions. Users compete in the Overall league table and can also create and join private leagues.  

A user scores points by correctly predicting the outcome of a match, with a bonus point awarded for correctly predicting a team's number of goals scored. There is a maximum of 5 points awarded per game with the points breakdown as follows:
- **5 points:** Correctly guessing the exact score (e.g. user predicts Italy wins against Turkey 2 goals to 1, and Italy actually wins against Turkey 2 goals to 1).
- **4 points:** Correctly guessing the match outcome and one of the teams goals scored (e.g. user predicts Italy wins against Turkey 3 goals to 2, and Italy actually wins against Turkey 3 goals to 0).
- **3 points:** Correctly guessing the match outcome but neither of the teams goals scored (e.g. user predicts Italy draws with Turkey 1 goal to 1, and Italy actually draw with Turkey 2 goals to 2).
- **1 point:** Incorrectly guessing the match outcome but correctly predicting one of the teams goals scored (e.g. user predicts Italy wins against Turkey 3 goal to 2, and Italy actually draw with Turkey 1 goal to 1).

Users can submit scores up to the time that a round of fixtures starts, and make as many changes as desired until then. This gives users the option of predicting the entire tournament (55 matches) at once or to enter scores as the tournament progresses. For the group stages, group tables are shown to help the user check that the teams they would expect to qualify for the knockout stages do based on their match predictions. A dynamic third-placed teams table is also provided to see which 4 of the 6 third-placed teams qualify for the knockout stages.  

All users are automatically added to the global Overall league where they can see their rank against all other users. The website also allows users to create private leagues so that they can directly compete against friends, family, colleagues, etc.  

### Design:  
I decided to split my application into a front and backend so that I could use React js and create a single page application rather than a multipage application. Instead of using Flask to render templates, I produced a REST API which would serve data to the frontend. This also allowed me to use JSON Web Tokens (JWT) for authentication which was something I was interesting in learning more about.  
- The app follows the Model View Controller (MVC) design pattern.
- Classes were created for the different models each of which was unit tested using unittest. The player class handles the logic for the user and authentication.
- Database queries were separated into repositories by class. I used Postgres for the database and <api-football.com> to retrieve real time football (soccer) data.
- User points are updated daily by a scheduler programmed to make a call to <api-football.com> which fetches real match data.
- In the frontend I used the create-react-app framework and React js library. I was able to experiment with hooks creating a custom hook for private routes that required authentication, using the browsers local storage, and using the context hook, amongst others.
- Bootstrap was used for styling.

### Technologies Used:
- Python
- Flask
- PostgreSQL
- api-football.com
- React
- Bootstrap
- HTML
- CSS

### 