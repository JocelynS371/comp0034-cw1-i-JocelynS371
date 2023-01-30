[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9743317&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
2. Create and then activate a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [the pip documentation](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. 


# Set-up instructions

Add any instructions here for the markers on how to setup and run your Dash app.

Add the URL to your GitHub repo here e.g. https://github.com/ucl-comp0035name_of_your_repo

# Visualisation design
## Target Audience and questions to answer
As defined previously in COMP0035, the target audience for my app are scientist and reserchers that is most likely working in the oceantography field. Their goal is to understand and be able to draw insight on my dataset.   
I have identified their needs as:   
1. access a chosen range of data
2. be provided documentation
3. see simple statistical analysis done automatically
4. access some of the data offline
5. search for specific values or date
6. provide new entry into the database   

Among these requirements some are not suitable for the dashboard we are developing at this stage, therefore, I will be focusing on need 1 and 5 mainly.    
To be more specific, I have also identified that a scientist would have a high comfort level with data and graphs, however, it is quite possible that they will need to export graphs to access later. This is what seperate them from a more general user group.   
The questions to be answered is:   
1. How much have the temperture of the current changed in the past 15 years? Is the termperture change increaseing due to global warming?
2. Did the ocean current change direction? If yes, how?
3. Is the annual salinity consistent in the past 15 year? Does the pattern of change coincide with the temperture change
4. Can we predict how the current is going to change in the next 5 years and present it to users?
## **Explain** the design for the dashboard and each visualisation. The designs should be appropriate for the target audience and the question(s) the visualisation is designed to address. Give reasons for your choices. Use appropriate literature/references to support your decisions.
## Designing chart to include
In the section above, we can see that need 1 and 5 are directly satified with a web app data dashboard. However, need 3 and 6 are not possible or likely to be fulfill at this stage. In terms of requirement, the needs can be catergorised as 
1. access a chosen range of data -- **Must Have**
2. be provided documentation -- **Should Have**
3. see simple statistical analysis done automatically  -- **Won't Have**
4. access some of the data offline -- **Could Have**
5. search for specific values or date -- **Should Have**
6. provide new entry into the database -- **Won't Have** 

Need 1 can be satified by design charts based on the questions proposed. Upon a closer inspection, we can see that each question, other than question 4 can correspond to 1 or more than 1 chart.

### First Chart
>How much have the temperture of the current changed in the past 15 years? Is the termperture change increaseing due to global warming?   

This question can be answered using a chart of temperture against time. Because the trend is our main concern in this question, a line chart or scatter graph would be appopiate.    
It should also be noted that the data in the dataset came from different locations, it would be useful to the users if they can select a location and see only the data from that location. 

### Second Chart
>Is the annual salinity consistent in the past 15 year? Does the pattern of change coincide with the temperture change

This is very similar to the first chart, but instead of temperture, salinity should be plotted. For the same reason, this should be a line or scatter graph. Keeping in mind that a ML algorithm might be added at a later stage, a scatter graph might be more appopiate as a regression line can be fitted a bit more easily.   
Again, the users should have the ability to plot only the data from certain locations.

### Third Chart (Should Have)
>Is the annual salinity consistent in the past 15 year? Does the pattern of change coincide with the temperture change
From the second part of this question, it arised that the temperture could be plotted against the salinity to show their relation. Since relation is what we are interested in, a line chart would be suitable
### Could Have Charts
>Did the ocean current change direction? If yes, how?

This is a much more difficult question to answer than the other 2 question we are considering, therefore it is counted as a could have feature rather than a must have feature. When I was proposing the question, I had envision a ML algorithm to have been design at this stage, therefore it may not be feasible at this stage to plot. 

## Overall Design of the dashboard
 
## **Evaluate** the final dashboard and visualisations with respect to the design and intended audience and purpose.
*When answering this essay question word, the key is to provide your opinion or verdict concerning the extent to which an argument or set of research findings is accurate. You may also be required to demonstrate the extent to which you agree with a particular argument or hypothesis.*

# Dash app

Add any notes here (optional).

# Testing

Add evidence here (groups).
