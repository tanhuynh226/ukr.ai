# Welcome to [ukr.ai](https://ukrai.netlify.app/)!

[Try our project out](https://ukrai.netlify.app/)—it's best used on mobile.

<p style="text-align: center;" align="center"><img src="https://github.com/tanhuynh226/hackuci2022-backend/blob/main/images/cover.png"></p>

## Inspiration

**Social media is the king of disinformation.** Astroturfing political elections through the widespread use of Twitter bots, creating narratives based on doctored images, or nations using widespread propaganda through mass media to seize control of regions—when controversy strikes, the internet is there to make sure the facts and fiction are intertwined.

In recent years, political parties have leveraged this to spur on disinformation campaigns. These massive information wars between nations have made it difficult to find something credible and trustworthy. When news struck that Russia had launched an attack on Ukraine, we knew that there would be widespread efforts to misconstrue the truth and further confuse the public.

We believe that creating an AI that could constantly review this mass influx of data and learn to sort the facts from fiction will help counteract the damage done by disinformation and propaganda campaigns.

## What it does

The UI is simple. There’s a text box where a user can enter some news they’ve heard, a link to a tweet, or a “fact” that doesn’t sit right. This message is parsed and analyzed by our fine-tuned GPT-3 AI model. Our application will tell you if the statement is misleading or not.

<p style="text-align: center;" align="center"><img src="https://github.com/tanhuynh226/hackuci2022-backend/blob/main/images/demonstrate_tweet.gif"></p>

## How we built it

### AI and back-end

For our AI model, we leveraged OpenAI's GPT-3 Curie and Ada engines. To train our models, we needed a large dataset that could tell the AI if a statement was misleading or not. We stumbled across Twitter's Birdwatch, a periodically-updated dataset containing entries of tweet IDs and their respective trustworthiness. Using Birdwatch, we mapped each tweet ID to its text content through Twitter API lookup, determined if the tweet is relevant to the current conflict, parsed the text, and added the label to our training dataset containing statements and their truth value. After formatting our data for GPT-3, we fed it into our AI, which learned what kind of statement was true and what was false.

With a knowledgeable AI, the front-end could query our model with text or a Twitter link—if it was a link, we fetched the tweet's text from Twitter API—and responded with our AI's classification (i.e. misleading, not misleading, unknown) and levels of confidence.

Once we were finished with all of the code, we deployed it using Google Cloud Functions, allowing the front-end to have access to the event-driven serverless functions.

### Web application

In the front-end, we developed a mobile-first responsive application that used the latest technologies. We were design-oriented from the start, by focusing on how the user would interact with the application. We featured a simple text box with clearly worded instructions within a modern design.

We also wanted to tackle the issue that our ML model would need time to "think", so we created interesting visuals such as a spinning 3D globe and animations to keep the user's attention as the API request to the server loaded.

We used Vue.js and Vite for a modular, easy-to-develop application. We knew that we would have to populate content from the back-end to the UI, which Vue can do clearly. Vite has exceptional speed when building and prototyping applications, making development easier.

We also leveraged Three.JS, one of the core libraries used for 3D graphics on the web. This library allowed for precise control over

## Accomplishments that we're proud of

* AI often returns proper response even with how limited our dataset is
* Obtaining Tweet text-label mappings using Birdwatch and Twitter API
* Fetching, formatting, cleaning up, and determining relevance of tweets
* Simple and elegant query and response between front-end and back-end
* Seamlessly implementing fluid graphics into the front-end
* Using Google Cloud Functions having no prior experience with serverless APIs

## Challenges we ran into

* **Properly training our AI with our own data set**
  * It was difficult to obtain a meaningful dataset from what we parsed from Twitter's Birdwatch fact-checking data
  * Our dataset was very limited given how little time has passed since the initial invasion
  * Difficult to filter out irrelevant tweets and false reports from Birdwatch's dataset
  * Each time we implemented a new dataset into the AI, the fine-tuning process can be very time consuming (up to 18 minutes)
* Implementing 3D animations and graphics
* Some UI challenges we faced was making our application responsive for different screen sizes

## What we learned

* Training, fine-tuning, and receiving a response from a GPT-3 model to be able to classify claims as misleading or non-misleading
  * Finding and labeling data points is challenging 
* Our first time working with Google Cloud Functions to deploy the back-end, which allows front-end to make event-triggered function calls
* How to use Three.JS to create responsive and interactive 3D animations in the browser
* How to use Pandas to parse imbalanced .tsv/.csv data into .jsonl files that GPT-3 can use to optimize its model
* Configuring and setting up Python environments

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
* Hugging Face's Transformers

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
