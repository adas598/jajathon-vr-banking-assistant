# JaJathon: GenAI-Based Virtual Banking Assistant

<img width="959" alt="ogp-en" src="https://github.com/adas598/jajathon-vr-banking-assistant/assets/141790766/2a7cddaf-726a-4b32-9b22-2f85cd176227">

Using chatVRM and ChatGPT API, Virtual genAI provides personalised customer service using the customers banking transactions history data that has coloumns: date_of_transaction, amount, description, account_balance. The API is first pre-processed: it is told that it is a data processing expert and that it needs to categorised the banking history into different categories such as Food, Eating out, Travel, Entertainment, Utilities. Next it is pre-told that,
_"You are a financial advising expert. You can design a financial plan for a user by taking in user banking data as context and develop a financial road map to acheive the customer's financial goal.
Please provide an timeline-based roadmap to achieve the goal:
    (1) How to acheive it with the current monthly income (assuming there is no increments)?
    (2) How much additional income might be required to reach the goal?
    (3) Create a succinct monthly budget to achieve this.
Ensure the output is point based and aesthetically pleasing as reponse will be displayed in the terminal. If using tables please make it `pretty` for the terminal."_

With pre-processing, and additional user banking data provided such as the past 400 categorised transactions, a reasonable prompt would be to "Recommend me where I can spend less money and save for a $5,000 overseas holiday in Paraguay. Also, provide me with tips on different ways I can save money in these areas, if I earn X much, fortnightly".

Some limitations include: the token limit where are unable to provide the system with data larger than 400 transactions. Also, the model has not been pre-trained leaving some performance in the tank.

For future research, we would look at a financial model that has been pre-trained on financial data, and have it fine-tuned with a database containing solutions to both common and complex finacial problems. Next Retrieval Augmented Generation would be added which give the system access to additional public and private data which it can cite when giving its responses to prompts. Lastly, the VRM has not been integrated with the API, so the input and output would need to be pipelined to each system which would not be difficult to setup.





