# ChatGPT Complete Guide

[Writing Prompts - The Basics](#writing-prompts---the-basics)

[Prompt Engineering](#prompt-engineering)

[Core Prompt Elements](#core-prompt-elements)

[Contextual Prompting](#contextual-prompting)

[Emotional Prompting](#emotional-prompting)

[Laddering Prompting](#laddering-prompting)

[Reversing Roles](#reversing-roles)

[ChatGPT Prompts Github Notes](#chatgpt-prompts-github-notes)

[Using ChatGPT for Utitlity Tasks](#using-chatgpt-for-utitlity-tasks)

[Writing Utility Scripts with ChatGPT](#writing-utility-scripts-with-chatgpt)

[Using ChatGPT for Content Generation](#using-chatgpt-for-content-generation)
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

Regarding Nodejs Application:

```prompt
Set up a basic ndoejs rest api with the following endpoints:

- GET /events (returns a list of events)
- GET /events/:id (returns a single event)
- POST /events (creates a new event)
- PUT /events/:id (updates an existing event)
- DELETE /events/:id (dele  tes an existing event)

Only add very simple dummy code for these endpoints.
This first step is just about setting up the general API + endpoints.
```

### Reversing Roles


#### Example:

```prompt
You are chatgpt - an advanced ai maiming to help users generate content.

Your goal is to write a prompt that could be used by chatgpt users.

Given the below output, write a prompt that would have yielded a similar output ?

Example Output:

AI will not replace web developers, but it will certainly transform the field. As AI and automation technologies continue to advance, we cab expect them to handle more routine and repetitive tasks, such as coding and layout designs. This will enable web developers to focus on creative and strategic aspects of their work.
```

Result:

```prompt
Prompt: "What is the role of AI in the field of web development and how does it impact the work of web developers?"
```


## ChatGPT Prompts Github Notes

https://github.com/f/awesome-chatgpt-prompts


You are expert in writing markdown files or readme file.

I want you to write Table of Contents for the above readme file.


## Using ChatGPT for Utitlity Tasks


### Writing Utility Scripts with ChatGPT

```prompt
you are a programmer and you have to write a python script for me.
im working on a windows computer and i never progrmmed before. i have folder on my desktop
names "files" and folder contains different files. the script should rename all files in the folder
to contain lowercase letters Only. Tell me all the steps i need to run the script.
```


## Using ChatGPT for Content Generation

