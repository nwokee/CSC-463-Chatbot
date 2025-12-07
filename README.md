# CSC-463 Copilot Agent - Comprehensive README

## Authorship, AI Assistance, and External Tools 

This repository was created as a final project for CSC‑463 at Oral Roberts University. The project team is responsible for the overall design of the agent, the selection of topics, the construction of the knowledge base, and the testing/evaluation process. 

### Use of Generative AI Tools 
During development, the team used generative AI tools (such as online agents like Perplexity Comet and/or large language models like ChatGPT / Microsoft Copilot) in the following ways: 
- To help draft and edit portions of this README and other documentation, including some setup steps, topic descriptions, and instructions. 
- To suggest wording for parts of the agent system prompt (`prompt.txt`) and for generating keywords and descriptions contained in the `/topics` YAML files. 
- To provide code suggestions and refactoring ideas for the Python OpenBible verse scraper (`openbiblescraper.py`) and related scripts. 
- To brainstorm or refine some example user prompts and evaluation items in the `/evaluation-sets` CSV files. All AI-generated or AI-suggested content was **reviewed, edited, and validated by the project authors** for correctness, alignment with course requirements, and consistency with ORU policies and values. 

### What Was Not Delegated to AI 
The following aspects of the project were not simply turned over to an AI tool and required substantial human decision-making: 
- Selection and curation of ORU-specific documents and links for the knowledge base. 
- Design of which Topics to include and how they should route user intents. 
- Definition of the high-level agent behavior and the integration of Biblical sentiment analysis with practical ORU information. 
- Interpretation and use of evaluation results to improve the agent. 

Any remaining errors, omissions, or misstatements are the responsibility of the student authors, not the AI tools. More information on how AI was used in each project file can be found under `AI_USAGE.md`




## Description

This project contains a fully configured Copilot Studio agent built for Biblical sentiment analysis and Oral Roberts University (ORU) student support. It includes the agent instructions, knowledge base files, all custom topics, a Bible verse scraping tool, and evaluation test sets. The agent is designed to give accurate, context-aware responses supplemented with relevant scripture, engaging primarily with people affiliated with ORU.

## File Organization

```
/agent-info
    prompt.txt (or Agent Prompt.txt)
    /topics
       *.yaml
    /knowledge-base
       Bible Verses.xlsx
       Crisis Protocol.xlsx
       Department Directory.xlsx
       Department Personnel.xlsx
       FAQs.xlsx
       ORU Site Links.xlsx
       Quest Event Information File.txt
       /academic-calendars
          *.pdf
       /academic-catalogues
          *.pdf
       /guide-info
          ORU Library Reservation Steps.docx
          ORU Petition Context.xlsx
          ORU Petition Steps.docx
          ORU Petition Types.xlsx
       /targeted-links
          Direct Knowledge Base Links.csv
/openbible-scraper
    openbiblescraper.py
    keywords.csv
/evaluation-sets
    Main Test Set.csv
    Alternate Test Set 1.csv
    Alternate Test Set 2.csv
    Alternate Test Set 3.csv
README.md
```

## Machine Requirements

- **Copilot Studio Enterprise**
- **Python 3.12**
- Python libraries:
  - `requests`
  - `beautifulsoup4`

## Agent Setup

### Navigating Copilot Studio

1. Open **Copilot Studio Enterprise**
2. Go to the **Agents** section on the left side panel
3. In the top right corner, select **Create Blank Agent**
4. Wait for the agent environment to initialize

### Entering the Agent Instructions

1. Navigate to the **Overview** section and find the **Instructions** panel
2. Paste the contents of `prompt.txt` (located in `/agent-info`)
3. These instructions define the agent's:
   - Overall role and identity
   - Tone and behavior
   - Knowledge base usage rules
   - Bible verse implementation
   - Examples of appropriate responses

## Knowledge Base Setup

### Bible Verse Web Scraper (OpenBibleScraper)

**Purpose:** The scraper collects verse metadata from OpenBible.info, sorted by topic, and organizes the data into a clean CSV file to add to the agent's knowledge base. Any additions or modifications to the base topic and keyword list can be made by modifying `keywords.csv`. As long as the topic is an existing OpenBible link, it can be added to the keywords for more extensive scraping.

**Setup Steps:**

1. Download `openbiblescraper.py` and `keywords.csv` from the files section
2. Open a terminal:
   - **MacOS/Linux:** Terminal
   - **Windows:** Command Prompt
3. Verify Python 3.12 is installed:
   - **MacOS/Linux:** `python3 --version`
   - **Windows:** `python --version`

4. **If Python 3.12 is not installed:**
   - Download from: https://www.python.org/downloads/release/python-3120/
   
   **Windows Installation:**
   1. Locate and double-click the downloaded `.exe` file (e.g., `python-3.12.0-amd64.exe`)
   2. **Crucial Step:** Check the box "Add python.exe to PATH" at the bottom of the first setup window
   3. Select "Install Now" and confirm any UAC prompts
   4. Click "Close" when finished
   
   **macOS Installation:**
   1. Locate and double-click the downloaded `.pkg` file (e.g., `python-3.12.0-macos11.pkg`)
   2. Click "Continue" through the introduction and license agreements
   3. Click "Install" and enter your macOS password if prompted
   4. Click "Close" when installation completes

5. Repeat step 3 to verify the correct version is installed
6. Install required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
7. **(Optional)** To increase verses per topic, adjust the `verse_ct` variable in the main section at the bottom of the script
8. Run the scraper:
   ```bash
   python openbiblescraper.py
   ```

Alternatively, if you do not want to scrape, we have provided our scraped data in our knowledge base, which you can import with the rest of the files.

### Importing Files Into the Knowledge Base

1. Download all files from the agent-info/knowledge-base directory
2. Go to Knowledge → Add Knowledge → Upload
3. Import all PDFs, documents, and verse files under `/agent-info/knowledge-base`
   - For `targeted-links` , open `Direct Knowledge Base Links.csv` and manually enter those links into the knowledge base, as the agent's topics use some of those direct links
   - For multi-file sets (e.g., Academic Calendars), toggle Group these files
4. Add a description and instructions for each group to guide retrieval and ensure accurate responses
5. Add any additional relevant files you may want to use
   - For links, ensure that the link does not exceed a nested path of more than 2 (oru.edu/life-at-oru/housing-and-dining/faq would be disallowed, but oru.edu/life-at-oru/housing-and-dining is fair game)


## Topic Setup

### What a Topic Is

A Topic is an independent conversational flow triggered by user intent. Each Topic includes:
- A trigger node (set to "The agent chooses")
- A Generative Answers node tied to a knowledge source
- Optional branching logic for complex workflows

**Important Notes:**
- Ensure all Knowledge Base files are downloaded before creating Topics
- All Topics are independent from one another and can be created in any order
- Premade system Topics (Greeting, Thank you, Goodbye, etc.) cannot be deleted and are required for smooth operation

### Creating a Topic from Scratch (Example: Academic Calendar)

1. Go to **Topics** section and click **Add a Topic** → **From Blank**
2. Label the Topic "Academic Calendar"
3. **Configure the trigger node:**
   - Keep the setting as **"The agent chooses"**
   - Add this description:
     ```
     This topic handles questions regarding important dates and deadlines at Oral Roberts University. It covers start and end dates for classes, holidays (Fall Break, Spring Break, Thanksgiving), final exam schedules, add/drop deadlines, and tuition refund schedules for Residential, Online, and Graduate programs. Use this for queries like 'When does school start?', 'When is finals week?', or 'What is the refund schedule?'
     ```

4. **Add a Generative Answers Node:**
   - Press the **"+"** button below the trigger node
   - Go to the **Advanced** section at the bottom of the pop-up
   - Select **Generative Answers**

5. **Configure the Knowledge Source:**
   - Click **Edit** under "Data sources"
   - Select **Add Knowledge**
   - Upload the Academic Calendar files (6 PDFs):
     - Fall 2025 - Spring 2026 Online & Lifelong Learning PDF
     - Fall 2025 - Spring 2026 Residential & Virtual Calendar and Refund Schedule
     - Fall 2025 and Spring 2026 Advantage calendar and refund schedule
     - Fall 2027 - Spring 2028 Residential & Virtual Academic Calendar & Refund Schedule
     - Summer 2026 Calendar & Refund Schedule
     - Fall 2026 - Spring 2027 Residential & Virtual Academic Calendar & Refund Schedule
   - Toggle **"Group these files"**

6. **Add a Description:**
   ```
   Official ORU Academic Calendars and Refund Schedules for 2025 through 2028. This file group covers Residential, Online, Graduate, and Advantage student programs. It contains all critical dates including start of classes, add/drop deadlines, withdrawal deadlines, holidays (Fall/Spring Break), final exam schedules, and tuition refund percentages.
   ```

7. **Add Instructions:**
   ```
   Use this source to answer questions about ORU academic dates, deadlines, and refunds.
   Always check if the user is asking about Residential, Online, or Graduate programs, as their dates differ.
   If the user does not specify a year, assume they are asking about the current or upcoming semester (e.g., Spring 2026).
   Distinguish clearly between 'Move-in dates' and 'Classes Begin' dates.
   For refund questions, provide the specific percentage breakdowns based on the date ranges in the schedule.
   ```

8. **Configure Input:**
   - Click **"input"** on the Generative Answer Node
   - Go to **System** in the pop-up panel
   - Find and select `Activity.Text`
   - Press **Save**

### Quick Setup Using YAML Files

Due to the complexity of creating topics from scratch, all flowchart code has been exported to `.yaml` files in the `/topics` folder:

1. Create a new topic from blank
2. Open the code editor (click the 3 dots → **Open code editor**)
3. Paste in the corresponding YAML file contents from the `/topics` folder
4. Save and repeat for each topic in alphabetical order

### Current Topics Included

#### Academic Calendar
Provides comprehensive scheduling information for academic years, extending up to two years into the future, including semester dates, holidays, exam schedules, and refund policies.

#### Admissions
Offers detailed information regarding the admissions process, course registration procedures, and available housing and meal plan options.

#### Athletics
Supplies detailed information about ORU's 16 intercollegiate sports teams, including official rosters, schedules, and recruitment guidelines.

#### Campus Events & Visitation
Delivers information on significant campus happenings, such as Culture Fest and student organization activities, along with instructions for scheduling campus visits.

#### Dining Information
Provides current operating hours for all campus dining facilities and details regarding designated meal exchange times.

#### Direct Verse Usage
Offers biblically grounded guidance by supplying multiple scripture verses relevant to the user's specific request or need.

#### FAQ 1, FAQ 2, FAQ 3
Addresses concise, single-query questions not categorized under a primary topical area.

#### Financial Aid
Offers detailed guidance on the cost of attendance, FAFSA application procedures, and available scholarship opportunities.

#### IT
Manages technical support inquiries related to ORU user accounts, campus technology infrastructure, and digital services.

#### Library Reservation
Guides users through the process of reserving private study rooms within the university library facilities.

#### ORU Program Information
Provides targeted, in-depth information for users seeking details on specific academic majors offered at the university.

#### Petition Formatting
Directs users to the appropriate online portal for academic petitions and provides clear instructions on required formatting and submission procedures.

#### Residential Services
Handles all inquiries exclusively pertaining to on-campus residence halls and student accommodations at Oral Roberts University.

#### Student Classifier
Activates when a user mentions elements related to academic status (e.g., class, major, minor, instructor, exam) or familial academic inquiries (e.g., son, daughter, student).

#### Student Life
Addresses inquiries concerning the broader campus living environment, student services, and extracurricular engagement at Oral Roberts University.

## Interacting With the Agent

### Navigating the Test Pane

1. Click **Test your agent** in Copilot Studio
2. Send messages to trigger Topics
3. The test pane displays:
   - Which Topic was triggered
   - The node execution path
   - Knowledge sources utilized
   - Model rationale summaries (if enabled)

## Evaluation Setup

### What the Test Sets Contain

The evaluation CSV files include:
- Test prompts
- Grading method (General Quality)

### How to Import and Run Evaluation Tests

1. Navigate to the **Evaluate** section
2. Click **Import Test Set** and upload files from the `/evaluation-sets` folder:
   - Main Test Set.csv
   - Alternate Test Set 1.csv
   - Alternate Test Set 2.csv
   - Alternate Test Set 3.csv
3. Select the agent and environment
4. Run the evaluation
5. Review the results:
   - Topic accuracy
   - Knowledge retrieval correctness
   - Verse alignment and relevance
   - Failure cases and recommended fixes

## Sources and Institutional Content 

Many of the topics and knowledge-base files in this project describe real policies, dates, and procedures at Oral Roberts University (ORU), such as academic calendars, admissions processes, financial aid information, housing & dining details, library reservations, and program descriptions. The **authoritative sources** for that information are official ORU webpages and documents (e.g., Academic Calendars, Catalogs, Financial Aid pages, Athletics, and Library sites), the names of which are reflected in the file titles in `/agent-info/knowledge-base` and related folders. This repository does **not** replace those official sources, and any discrepancies between the chatbot responses and official ORU publications should be resolved in favor of the official ORU documents.



## Additional Information

This agent is specifically designed for the ORU student population and integrates Biblical sentiment analysis to provide spiritually enriching responses alongside practical university information. The combination of comprehensive knowledge bases, targeted Topics, and scripture integration creates a unique support experience for Christian college students.
