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

[Using ChatGPT for Content Generation](#using-chatgpt-for-content-generation)

[Using chatgpt as interviewer](#using-chatgpt-as-interviewer)

[Using ChatGPT for Programming and Development](#using-chatgpt-for-programming-and-development)
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


### Using ChatGPT for Content Generation

### Writing an article / blogpost


```prompt
write an article about the iphone history and how it changed the world.
```

### Adding Constraints:


```prompt
1. Target Audience: 20-30 year olds

2. Topic related keywords.

3. Tone: Friendly, Informative, Positive

4. Length: 1000 words

5. Adding a title: "The History of the iPhone"

6. Adding images: 2 images
```

### Using a single prompt to create articles

```prompt
You are a professional blogger. Your job is to write an engaging article about the development of the iPhone based on these bullet points:

1. article should start with a short introduction about the iPhone.
2. target audience are tech related people.
3. article should be 1000 words long.
4. you should hightlight the most important milestones in the development of the iPhone.
5. article should contain different section with subheaders.
6. article should contain at least 2 images, if you cannot find any images, add an image description.
```

### Using chatgpt as copywriter

```prompt

You are a professional copywriter. Your job is to help online store markets and sell their products in the best possible way.

create an engaging landing page text for an online fashion store based on the following bullet points:

1. page sells styling clothes for young people between 14 and 21 years old.
2. the fashion can only be bought online, the company does not have any physical stores.
3. the brand only create shirts, hoodies and sneakers.
4. the brand is known for its high quality and unique designs.
5. two weeks ago the brand released a new collection of hoodies and sneakers.
6. the fashion is only available in limited quantities.

the text should be 500 words long and should be written in a friendly and positive tone. Also come up with a title for the landing page.
```

### Using chatgpt as interviewer

```prompt
you have to prepare an interview a software developer for the same position. write 15 technical interview questions.
```

### JSON & CSV & Table & Markdown

```prompt
create a json array . it should contain 5 recipes. each recipee should contain atleast 5 ingredients.
```

```prompt
provide data for 50 largest cities in the world in csv format with the following headers: City, COuntry, Region, Population, Currency.
```

```prompt
I need output in tabular format for dummy data for an online store. the columns should be: Product, Price, Quantity, Total Price. the table should contain 20 rows  
```

## Using ChatGPT for Programming and Development

### Writing a python script

```prompt
write a python script that takes a list of numbers as input and returns the sum of all numbers in the list.
```

### Writing a javascript function

```prompt
write a javascript function that takes a list of numbers as input and returns the sum of all numbers in the list.
```

### Writing a javascript class

```prompt
You are an experienced developer. 

Write a prgram that scans all files in a given folder and organizes them into subfolders based on their file extension.

- Audio files should be moved to a folder called "audio"
- Video files should be moved to a folder called "video"
- Image files should be moved to a folder called "images"
- Text files should be moved to a folder called "text"
- All other files should be moved to a folder called "other"
```


### Creating a website
```prompt   
You are an experienced developer.

Create a website that has the following pages:

- A starting page with a short introduction about yourself.
- A page with a list of your projects.
- A page with a contact form.

The website should be responsive and work on mobile devices.
```

