# IPL_dataset_analysis
data analysis, querying and programming of the IPL dataset.<br/>

<b>In file analysis.ipynb</b>: 
Following queries are conducted.<br/>
1. query to get the dismissal types with count.<br/>
2. listing of team and the number of sixes (6s) scored by each team.<br/>
3. query to find total runsscored by the batsman for each team he played. (Assume
   all players are batsman).<br/>
4. query to get match_Id, Man of the match and runs scored by man of the match.<br/>
5. query to get list of team and boundary scored when the team won the toss and
  decided to bat first. (boundary includes 4s and 6s).<br/>
6. query to return a report for Venue and City and average runs scored per match
  in powerplay in 1st inning. [powerplay means 1 to 6th Over including 6th Over]<br/>
  
<b>In section3.py file.</b><br/>
* First we created database in local MySQL database.<br/>
* imported the csv into tables.<br/>
*In source code created a class Database that has the following features:<br/>
   1. Constructor to initialise dB connection and other variables.<br/>
   2. Methods implemented to return resultset for first two queries listed above.<br/>
   3. The resultset returned as a json object.<br/>
 
