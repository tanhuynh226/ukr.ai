# Welcome to [ukr.ai](https://ukrai.netlify.app/)!

## Inspiration

Social media is the king of disinformation. Astroturfing political elections through the widespread use of Twitter bots, creating narratives based on doctored images, or nations using widespread propaganda through mass media to seize control of regions—when controversy strikes, the internet is there to make sure the facts and fiction are intertwined. In recent years, political parties have leveraged this to spur on disinformation campaigns. These massive information wars between nations have made it difficult to find something credible and trustworthy. When news struck that Russia had launched an attack on Ukraine, we knew that there would be widespread efforts to misconstrue the truth and further confuse the public.

We believe that creating an AI that could constantly review this mass influx of data and learn to sort the facts from fiction will help counteract the damage done by disinformation and propaganda campaigns.

## What it does

The UI is simple. There’s a text box where a user can enter some news they’ve heard, a link to a tweet, or a “fact” that doesn’t sit right. This message is parsed and analyzed by our fine-tuned GPT-3 AI model. Our application will tell you if the statement is misleading or not.

## How we built it

### AI and backend

To train our AI model, we utilized Twitter's Birdwatch, a dataset containing entries of tweet IDs and their respective trustiworthiness. We mapped each tweet ID to its text content through Twitter API lookup, determined if the tweet is relevant to the current conflict, parsed the text, and added the label to our training dataset. After formatting our data into a dataset that GPT-3 can read, we fed it into our AI so that it can train itself to identify what is fact and what is fiction.

With a knowledgeable AI, the frontend could query our model with text or a Twitter link--if it was a link, we fetched the tweet's text from Twitter API--and responded with our AI's classification and levels of confidence, i.e. Misleading, Not Misleading, and Unknown.

Once we were finished with all of the code, we deployed it using Google Cloud Functions, allowing the frontend to have access to the event-driven serverless functions.

### Web application

In the frontend, we developed a responsive application that used the latest technologies. We were design-oriented from the start, by focusing on how the user would interact with the application. We featured a simple text box with clearly worded instructions within a modern design. We also wanted to tackle the issue that our ML model would need time to "think", so we created interesting visuals such as a spinning 3D globe and animations to keep the user's attention as the API request to the server loaded. 

## Accomplishments that we're proud of

* AI still returns proper response (sometimes) even with how limited our dataset is
* Obtaining Tweet text-label mappings using Birdwatch and Twitter API
* Seamlessly implementing fluid graphics into the front end

## Challenges we ran into

* **Properly training our AI with our own data set**
  * It was difficult to obtain a meaningful dataset from what we parsed from Twitter's Birdwatch fact-checking data
  * Our dataset was very limited given how little time has passed since the initial invasion
  * Difficult to filter out irrelevant tweets and false reports from Birdwatch's dataset
  * Each time we implemented a new dataset into the AI, the fine-tuning process can be very time consuming (up to 18 minutes at times)
* Implementing 3D animations and graphics
* Some UI challenges we faced was making our application responsive for different screen sizes


## What's next for ukr.ai

Our AI is in the early stages of the learning process. As more data points are released into Birdwatch's fact-checking dataset and more users submit feedback on our AI's performance, we will continuously retrain and improve our model which will substantially boost its accuracy.

## Built with

### Languages
* Python - Fast development with ML libraries
* Javascript - The language for the browser

### Libraries and APIs
* Vue.js
* Pandas
* Twitter API
* Flask
* Three.JS

### Tools
* Figma
* Vite
* GPT-3
* Netlify
* Google Cloud
* Postman

## The team

* Pranav Grover
* Patrick Hu
* Tan Huynh
* Alex Rabinovich
* Stella Zhou

<!-- Elevator pitch
With Russia's invasion of Ukraine, there has been an influx of misinformation regarding the conflict spreading through various social media outlets. 
(promo pic 1) ukr dot ai uses machine learning to help others distinguish what media information can be misleading. 
(demo) we will demonstrate how our application works, bleh -->
 
