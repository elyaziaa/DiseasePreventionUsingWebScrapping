import requests #importing the requests an
from bs4 import BeautifulSoup

# we will have two scraping functions, one to scrape the disease name and the other to scrape it's corresponding prevention tip, and both will be added to their corresponding lists
def scrape_the_symptom(url):
    try: #using the try and except block so we can error check 
        response = requests.get(url) #tries to get the URL

        if response.status_code != 200: # we only care about the 200 status code becuase it indicates success, otherwise we will print the error message
            print(f"Failed to get the webpage: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # using the inspect tool we found a patter in all the disease/symptom names and that is the h3, 
        symptoms_list = soup.find_all('h3')
        symptoms = [item.text.strip() for item in symptoms_list] #here we are claning up the headers and storing them all in a list of strings that contain the disease/symptom name
        return symptoms #returning this list
         
    except Exception as e: #catching the errors if any 
        print(f"An error has occurred: {e}") 
        return []

def scrape_prevention(url):
    try:
        response = requests.get(url)#tries to get the URL
        if response.status_code != 200:# we only care about the 200 status code becuase it indicates success, otherwise we will print the error message
            print(f"Failed to get the webpage: {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')

        prevention_tips = []

        # to find the paragraph of the prevention tip, after inspecting we found that the prevention tip paragraph is followed by a title in both <string> and its in the form <p> as well
        for paragraph in soup.find_all('p'):
            strong_tag = paragraph.find('strong') # here we are finding all the strings that are labelled tips to prevent, as the paragraph referring to tips to prevent is right ater this 
            if strong_tag and 'tips to prevent' in strong_tag.text.lower():#checking for the tips to prevent format 
                prevention_tips.append(paragraph.text.strip())#here we are appending the prevention tip paragraphs all in an initially empty list called  prevention_tips = []
      #returning both lists

        return prevention_tips
    
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []

def display_symptoms(symptoms):
    print("List of Diseases:") #dispalying the list of disease, while also numbering them
    for index, symptom in enumerate(symptoms, start=1):
        print(f"{symptom}")

def display_prevention_tips(prevention_tips):
    print("\nPrevention Tips:")
    for index, tip in enumerate(prevention_tips, start=1): #here we are only displaying the prevention tip corresponding to what the user inputed as the number, and since indices start at 0, we made start=1
        print(f"{index}. {tip}")

def main():
    url = "https://www.careinsurance.com/blog/health-insurance-articles/most-common-diseases-in-summer-season"

    # scrape the symptoms and prevention tips from the site
    symptoms = scrape_the_symptom(url) #passing in the url to get the name of the symptom/disease
    prevention_tips = scrape_prevention(url) #passing in the url to get the passage for the prevention tip of that disease/symptom

 
    if symptoms:
        display_symptoms(symptoms)
    else:
        print("No diseases found.")



    # here we are just checking thatboth the symptoms and prevention tip lists are equal in length, because if not, that means we are missing either some symptom names or prevention passages
    if symptoms and prevention_tips and len(symptoms) == len(prevention_tips):
        while True: # while that true we do the following
            try:
                # we will ask the user to input the number corresponding to the disease they want to learn more about
                choice = int(input(f"\nSelect the number corresponding to the disease (1-{len(symptoms)}): "))
                
                # make sure they chose a valide disease number
                if 1 <= choice <= len(symptoms):
                    # printing the corresponding prevention tip(while having the -1 to adjust the index offset and match it to the number the user inputed)
                    print(f"\nYou selected: {symptoms[choice - 1]}")
                    print(f"Prevention Tip: {prevention_tips[choice - 1]}")
                    break
                else:
                    print(f"Please enter a number between 1 and {len(symptoms)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    else:
        print("The number of diseases does not match the number of prevention tips.")

if __name__ == "__main__":
    main()
