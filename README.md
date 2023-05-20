# ChatGPT Complete Guide

## Writing Prompts - The Basics


## Prompt Engineering

- It is about writing good prompts and getting good results.

### Core Prompt Elements

#### Prompt 1:

```prompt
Give me five great travel destinations for summer.

Format your response like below:

Location: 
Best time to visit: 
Avg. Temparature(Celsius): 
Hours of Sunshine: 
Rainy Days per month:
```


#### Prompt 2:

```prompt
You are an AI Assistant that specialized on sumamrizing articles.

Summarize the below article:

'''
For the past 50 years, the National Cancer Institute’s Clinical Trials Cooperative Group Program has played a key role in developing new and improved cancer therapies and preventive strategies. NCI-sponsored trials have studied distinct cancer subpopulations and those with rare cancers, elucidated the role of therapeutic and chemoprevention agents such as tamoxifen for breast cancer, and evaluated quality-of-life issues for patients with cancer. But a new report from the Institute of Medicine (IOM) of the National Academies concludes that the Clinical Trials Cooperative Group Program is in a “state of crisis.”
The IOM report recommends 12 sweeping changes in the ways that their clinical trials are reviewed, prioritized, and funded-changes that are likely to affect players as diverse as NCI and the FDA, clinical research investigators, cancer patients, and even heath-care insurers and the pharmaceutical industry. More than 25,000 cancer patients, 3,100 institutions, and 14,000 investigators from cancer centers and community oncology practices participate in Cooperative Group clinical trials each year-and they would all likely be affected by the IOM’s recommended changes.
“Many people involved in the Cooperative Group clinical trials, including NCI and those doing research in the academic community and practice community, shared the same frustrations. The Cooperative Group trials system had become inefficient and slow, and we were not adequately funding and incentivizing people to participate-including patients and physicians,” said John Mendelsohn, MD, Chair of the IOM committee and President of The University of Texas M. D. Anderson Cancer Center. “There was too much recycling of efforts, and too much gathering of opinions and counteropinions to design the trials. Everything needed to be streamlined.”
'''

Summarize the article starting like this:

The key take aways of the article are:
- 

```

### Prompt 3:

Question:
---------
Use python & jaavscript to encode into inpput text by shifting every character one character to the left.



Prompt:
--------

```prompt
You are an experienced Python and Javascript developer.

Give me the code for a program that takes some text as user input. The program should then encode that text by shifting every character one character to the left.
For example, "B" becomes "A", "E becomes "D" and so on.

Finally, program should output that encoded text.


Write the program for both python and javascript developers
```


### Contextual Prompting


### Emotional Prompting

Example:

```prompt
Write an email response to the following custoner complaint:

"
Your products are garbage. The new chair broke 1 day after it was shipped. You will hear from my
lawyer.
"

When drafting the response, take the sentiment and tone of the customer into account.
```

### Laddering Prompting

#### Example:

```prompt
Set up a basic ndoejs rest api with the following endpoints:

- GET /events (returns a list of events)
- GET /events/:id (returns a single event)
- POST /events (creates a new event)
- PUT /events/:id (updates an existing event)
- DELETE /events/:id (deletes an existing event)

Only add very simple dummy code for these endpoints.
This first step is just about setting up the general API + endpoints.
```
