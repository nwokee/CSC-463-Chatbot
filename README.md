# **CSC-463 Copilot Agent -- README**

## **Description**

This project contains a fully configured Copilot Studio agent built for
Biblical sentiment analysis and Oral Roberts University (ORU) student
support. It includes the agent instructions, knowledge base files, all
custom topics, a Bible verse scraping tool, and evaluation test sets.
The agent is designed to give accurate, context-aware responses
supplemented with relevant scripture.

## **File Organization**

    /agent-info
        prompt.txt
        /topics
            *.yaml
        /knowledge-base
            *.pdf
            *.xlsx
            *.docx
    /openbible-scraper
        openbiblescraper.py
        keywords.csv
    /evaluation-sets
        Main Test Set.csv
        Alternate Test Set 1.csv
        Alternate Test Set 2.csv
        Alternate Test Set 3.csv
    README.md

## **Machine Requirements**

-   **Copilot Studio Enterprise**
-   **Python 3.12**
-   Python libraries:
    -   `requests`
    -   `beautifulsoup4`

## **Agent Setup**

### **Navigating Copilot Studio**

1.  Open **Copilot Studio Enterprise**.
2.  Go to the **Agents** section.
3.  Select **Create Blank Agent**.
4.  Wait for the environment to initialize.

### **Entering the Prompt**

1.  In the Agent **Overview**, find the **Instructions** panel.
2.  Paste the contents of `Instructions.txt`.
3.  These instructions define the agent's identity, tone, knowledge
    usage rules, and verse-insertion behavior.

## **Knowledge Base Setup**

### **OpenBibleScraper**

The scraper gathers verses from OpenGateways using keyword mapping.

**Steps** 1. Download `openbiblescraper.py` and `keywords.csv`. 2.
Confirm Python 3.12 is installed. 3. Install required libraries:
`pip install requests beautifulsoup4` 4. (Optional) Adjust `verse_ct` in
the script to change the number of verses per keyword. 5. Run the
scraper: `python openbiblescraper.py` 6. Import the generated verse
files into the knowledge base.

### **Importing Files Into the Knowledge Base**

1.  Go to **Knowledge** → **Add Knowledge** → **Upload**.
2.  Import all PDFs, documents, and verse files.
3.  For multi-file sets (e.g., Academic Calendars), toggle **Group these
    files**.
4.  Add a description + instructions for each group to guide retrieval.

## **Topic Setup**

### **What a Topic Is**

A Topic is an independent flow triggered by user intent. Each Topic
includes: - A trigger node ("The agent chooses") - A Generative Answers
node tied to a knowledge source - Optional branching logic

### **Example (Academic Calendar Topic)**

1.  Create Topic → **From Blank**.
2.  Keep the trigger node as **The agent chooses**.
3.  Add a description such as: *"Handles all questions about ORU
    academic dates, deadlines, holidays, exam weeks, and refund
    schedules."*
4.  Add a **Generative Answers** node (Advanced → Generative Answers).
5.  Attach the **Academic Calendar** knowledge group.
6.  Add instructions:
    -   Distinguish between Residential / Online / Graduate
    -   Default to current or next semester
    -   Provide exact refund percentages
7.  Set input → System → **Activity.Text**.

### **Copying the Premade Topics**

1.  Create a **Blank Topic**.
2.  Open the code editor (three dots → **Edit code**).
3.  Paste the contents of the `.yaml` file from `/topics`.
4.  Save and repeat for each Topic.

### **Current Topics Included**

-   Academic Calendar
-   Admissions
-   Athletics
-   Campus Events & Visitation
-   Dining Information
-   Direct Verse Usage
-   FAQ 1 / FAQ 2 / FAQ 3
-   Financial Aid
-   IT
-   Library Reservation
-   ORU Program Information
-   Petition Formatting
-   Residential Services
-   Student Classifier
-   Student Life

## **Interacting With the Agent**

### **Navigating the Test Pane**

1.  Click **Test your agent** in Copilot Studio.
2.  Send messages to trigger Topics.
3.  The pane shows:
    -   Which Topic fired
    -   The node path
    -   Knowledge sources used
    -   Model reasoning summaries (if enabled)

## **Evaluation Setup**

### **What the Test Sets Contain**

The evaluation JSON files include: - Prompts - Expected Topic - Expected
result or behavior - Edge cases - Verse-matching scenarios -
Knowledge-retrieval questions - Hallucination-prevention checks

### **How to Import and Run**

1.  Navigate to **Evaluate**.
2.  Click **Import Test Set** and upload JSON files from `/evaluation`.
3.  Select the agent and environment.
4.  Run the evaluation.
5.  Review:
    -   Topic accuracy
    -   Knowledge retrieval correctness
    -   Verse alignment
    -   Failure cases and recommended fixes
