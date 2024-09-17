# Purpose of data collection
The reason why we are collecting data in this code is in order to scrape a webpage, which is the care health insurance website,  for information about common diseases or symptoms and their respective prevention tips paragraphs. We store these informations in two separate lists, and present it to the user based on the number they selected that corresponds to the disease they want to learn about. 

# Ethics & Respecting the Site policies:
As for our website, since it could be considered as a small more so national website, in the sense that it is not used internationally as it is a health insurance company in India. That being said, they did not have a very detailed or specific part of their website that indicated anything about web scraping. However they did have a part that mentioned protecting their clients personal details. 

In our program we are only scrapping a blog that the company had posted, rather than touching on any stats based on client details- that could perhaps be a more challenging aspect to touch on as respecting their privacy matters a lot to the site and the clients as well. 

As for what we are scrapping, it is important that we limit our scraping and scrape only what we will utilize. For that reason, we used the inspect tool to know more about the formats of exactly what we want to scrape. So, we made sure to have our program contain very specific if statements that match with the format of the information we want to scrape in order to print only the information we want to use, which is the disease/symptom name an dth prevention tip only.

Additionally, when it comes tot he .gitignore file, we included that as it will ensure that the files and directories are not stored in our git repository. This helps a lot as it to keeps the site’s data not in version control which allows for our project to be most secure and clean. 

Lastly, we want to conclude by mentioning that our program was built solely for educational purposes and to inform the user and enlighten them with prevention tips for the diseases. 
