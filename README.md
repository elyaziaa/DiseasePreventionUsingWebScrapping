
# A clear description of the data your scraper uncovers and its purpose#

The website we are scrapping is the Care Health Insurance website. This is an Indian health insurance company established in July 2012. The data we ar scrapping is two things: 1- The Disease/Symptom Name, and 2- The prevention tip corresponding to that disease name. 
After using the inspect tool we found that the Symptoms/Disease Names can be scrapped by looking for the h3 tags. So our program takes the disease names cleans and stores it in a list. These diseases are then displayed to the user in an ordered list to choose from and learn more about the prevention tip associated to it.
The second part of the scraper extracts prevention tips for each disease by locating specific p and tags containing the "tips to prevent" information. What made this simpler to extract is the specific format the website uses, the prevention tips paragraph is followed by a title in format p and strong.  These tips are stored in a corresponding list.
The purpose of this scrapper is to scrape both the disease names and the prevention tips and store them in two corresponding lists. Since the scrapping has an order and we are appending these strings into two separate lists, we are going to access them through indexing, and provide the user with the prevention tip corresponding to the disease they want to learn about.


# The website used and why it was chosen#

One thing we had to keep in mind while choosing the website is that it needs to be a website that another group has not chosen so this was the main goal when looking for websites. Aside from that we were looking for a health website and decided to look into diseases, and found this website. The Care Health Insurance website targets people living in India that want to have access to health insurance. They posted this blog and one thing we noticed is a very rhythmic and simple pattern the blog has. The Symptoms/Disease Names can be scrapped by looking for the h3 tags, and the the prevention tips paragraph is followed by a title in format p and strong>, and the paragraph itself is in p form.



# How can someone run this #

1- I had to use python3 -m venv .venv instead of just -m venv .venv , as this was giving me zsh: command not found: -m (Not sure if this is just my laptop version/mac user)
2- Make sure to install the dependency:  pip install -r requirements.txt
