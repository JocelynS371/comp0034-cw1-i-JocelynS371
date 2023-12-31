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

https://github.com/ucl-comp0035/comp0034-cw1-i-JocelynS371.git

THat is the url to my repository.
To use the app, install the modules in requirement.txt and run app.py

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
## Explain the design for the dashboard and each visualisation
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
In designing the dashboard, I decided to focus on a minimal number of data visualixation, which is 2 charts. THe charts are place on different tabs to keep the pages uncluttered. 
   
In the end instead of seperate charts, I combined chart 1,2,3,4 designed above into 1 chart in the tab trend exploration. THis allows the user to experiment and explore the data on the same tab.
Since my data vary with both time and space. I think a map plot would be a good way to visualise the position of locations where the data are taken. This graph mainly present the location rather than magintute of data. THerefore I find it acceptable that it may not show much insight in regard to temperture or salinity in each location.   
However, to assist I added a statistic panel on the left to aid readers in seeing the data. It was planned for the panel to varies when the user click on each point. However it did not work and a key type error keep occuring and hence was not implement. THe issue lays most likely in the clickedData values returned by the graph. For now the users are allowed to choose a location from a dropdown list
   
THe other graph is a scatter plot. THe plot allows user to select variables on both x and y axis and location. It also allows users to choose a trendline for the dashboard to plot. 
Since my target sudiences are scientist, it is expected that they are sufficiently skilled in statistic to know common trend line options. This should meet their requirement as it visualise trends between variables and perform very simple statistical analysis as defined in the requirements at a earlier stage.

As for the overall design, with the law of multistability in mind, I decided to use a white backgroud and highlight important information using a darker background. THe more important the section is, the darker the background and lighter the text.

# Dash app

THere is 2 thing that I wanted to acheive but was not able to.   
1st, I want to keep the responds time in each chart under 1 minute but it was not possible.
2nd, I wanted to update the stat panel as users click on the graph but was not able to. After reading documentations, I decided that it was not achvieable in this time frame and used a dropdown list to allow users to chose location instead.

# Tools & Techniques

https://github.com/ucl-comp0035/comp0034-cw1-i-JocelynS371.git

The above is the url to my gitbub repository

I also used continous intergration in gothub to lint my code. Evidence can be seen in actions in github.  
![linting](/pylint.png)

Some error are ignored becuase I did not find an alternative way to acheive the desired result.
# Reference List
Cairo, A. (n.d.). Graphics Lies, Misleading Visuals. [online] Available at: https://faculty.ucmerced.edu/jvevea/classes/Spark/readings/Cairo2015_Chapter_GraphicsLiesMisleadingVisuals.pdf.   

Cleveland, W.S. and McGill, R. (1984). Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods. Journal of the American Statistical Association, 79(387), pp.531–554. doi:https://doi.org/10.1080/01621459.1984.10478080.   

Gutierrez, A. (2021). How to design data visualizations that are actually valuable. [online] Medium. Available at: https://uxdesign.cc/how-to-design-data-visualizations-that-are-actually-valuable-e8b752835b9a [Accessed 15 Feb. 2023].   

IBM (n.d.). IBM Design Language. [online] www.ibm.com. Available at: https://www.ibm.com/design/language/.   

Interaction Design Foundation (2016). What are Gestalt Principles? [online] The Interaction Design Foundation. Available at: https://www.interaction-design.org/literature/topics/gestalt-principles.   

Spring 2019, M. 2629 (2019). A Reader on Data Visualization. [online] mschermann.github.io. Santa Clara University. Available at: https://mschermann.github.io/data_viz_reader/.   
