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

### Chart 1 and Chart 2
>How much have the temperture of the current changed in the past 15 years? Is the termperture change increaseing due to global warming?   

This question can be answered using a chart of temperture against time.
It should also be noted that the data in the dataset came from different locations, it would be useful to the users if they can select a location and see only the data from that location. 

>Is the annual salinity consistent in the past 15 year? Does the pattern of change coincide with the temperture change

This is very similar to the first chart, but instead of temperture, salinity should be plotted.Keeping 
Again, the users should have the ability to plot only the data from certain locations.

Both of these graphs are concerned with the trend of the data in regard to time. On IBM's Design Language website, Line, Area, Boxplot, Histogram and Stream are recommended for showing trends. The first 4 chart are all avaiable in plotly express. In my opinion, a line chart would be the best choice since it is clear and often have the lowest ink to data ratio. 
However, our target audience is expected to have experince in reading charts, it is possible that they will prefer chart like boxplot that provide extra information, therefore, there should be an option for the user to choose between line and boxplot. If there is enough time, hostograms can be added as an option as well.

### Chart 3 and Chart 4 (Should Have)
>Is the annual salinity consistent in the past 15 year? Does the pattern of change coincide with the temperture change
From the second part of this question, it arised that the temperture could be plotted against the salinity to show their relation. Since correlation is what we are interested in, IBM recommend a scatter plot, heatmap ot parallel coordinate. Scatter plot would be very easier to create and might intergrate well with a ML algorithm if we are to create one at later stage. 
Heatmaps on the other hand wouldn't be a suitable graph for this correlation. It would be much more suitable for datas that involve frequency or density.

>How much have the temperture of the current changed in the past 15 years? Is the termperture change increaseing due to global warming? 

In the process of designing, it occured to me that it might be useful to the users if a comparision between locations are shown. This comparision could be shown as a grouped bar chart where bars from different locations are grouped together.
If there is sufficient time, a bubble graph on a map might also be useful to visualise the comparision.
There should be be an option for this graph to choose locations to compare, an option for temperture or salinity and an option for year to compare.
### Could Have Charts
>Did the ocean current change direction? If yes, how?

This is a much more difficult question to answer than the other 2 question we are considering, therefore it is counted as a could have feature rather than a must have feature. When I was proposing the question, I had envision a ML algorithm to have been design at this stage, therefore it may not be feasible at this stage to plot. 

## Overall Design of the dashboard
### Designing the visuals
One priciple to keep in mind of while designing the dashboard is the Gestalt Principles. It is the idea that human group silimilar element and recognize patterns when we precievive objects.
As an interface between users and the data, it is important that we help user navagate as effortlessly as possible.
On the whole, we could apply the law of common region on the dash board design. Which means we should group similar elements in a common, closed region. For example, we could present data sniplet eg. means and standard deivations on the side and the graphs on the other side. This allows the user to understand that they are different element on their first glance.   
Likewise, the law of proximity means that human see object close to each other as 1 entity. 
The law of Multi-Stability means that we could highlight the important information with contrast in colour. We want to present the information as the 'foreground', which often means the lightest colour in the page.    
Applying these priciple, we want to divide the dashboard into different parts. My plan is to have 3 part to it. An options block, chart(s) and sniplet of the data. I want each of them to be viewed as a seperate entity. Therefore the options need to be together and colour can be used to seperate the chart and data sniplet.   
### Chart Design
>Above all else, show the data    

>“A graphical method is successful only if the decoding is effective. No matter how clever and how technologically impressive the encoding, it fails if the decoding process fails.”   
   
Keep in mind of these principle. We should keep the graphs as simple as possible.   
In addition, according to Cleveland and McGill (1984), the human mind find positions on a scale the easiest to interpret while colour and shading is the most difficult to interpertate.
This suggest that scatter graph are the most effective in presenting data. Following that, length, direction and angle is also easy to understand. These points to graphs such as bar chart or line chart.
Surprisingly, coloured graphs such as heat map or bubble graph are not recommended size they could mask the insight with their visual design.
## Evaluate the final dashboard and visualisations
In designing the dashboard, I decided to focus on a minimal number of data
# Dash app

Add any notes here (optional).

# Testing

Add evidence here (groups).
