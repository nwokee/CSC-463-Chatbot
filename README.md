# CSC-463-Chatbot

Final Project Documentation for our Copilot Agent with Biblical Sentiment Analysis, including the entire knowledge base, topics, and evaluation sets.

## Requirements

- Copilot Studio Enterprise
- Python 3.12

## Setup

### Agent Setup

1. Open Copilot Studio Enterprise
2. Go to "Agents" Section on Left Side Panel
3. In the Top Right Corner, press "Create Blank Agent"
4. Wait for it to load the Agent Environment

### Agent Environment Setup

**Overview Section - Instructions:**

1. Navigate to the Instructions Section
2. Enter bot instructions into the respective window from `Instructions.txt`
3. The Instructions are the base prompt for every interaction and give the Agent its identity:
   - Overall Role
   - Tone and Behavior
   - Usage of Knowledge Base
   - Bible Verse Implementation
   - Examples of Responses

### Bible Verse Web Scraper Setup

**Purpose:** Collect accurate and vetted Bible verses from OpenGateway.com and combine them with Response-Keyword Matching to provide users with biblical encouragement and guidance throughout the conversation. The scraper engages the primary user base of the chatbot, which is primarily Christian College Students.

**Steps:**

1. Download `openbiblescraper.py` and `keywords.csv` from files section
2. Open a terminal ("Terminal" for MacOS/Linux, "Command Prompt" for Windows), VSCode, or PyCharm
3. Ensure the machine is running Python 3.12
   - For MacOS/Linux enter in terminal: `python3 --version`
   - For Windows enter in terminal: `python --version`

4. **If Python 3.12 not downloaded:**
   - Download from: https://www.python.org/downloads/release/python-3120/
   
   **Windows Installation:**
   1. Run the Installer: Locate the downloaded `.exe` file (e.g., `python-3.12.0-amd64.exe`) and double-click it
   2. **Crucial Step:** Check the box "Add python.exe to PATH" at the bottom of the first setup window
   3. Choose Installation Type: Select "Install Now" and confirm any UAC prompts
   4. Complete Installation: Click "Close" when finished
   
   **macOS Installation:**
   1. Run the Installer: Locate the downloaded `.pkg` file (e.g., `python-3.12.0-macos11.pkg`) and double-click it
   2. Follow the Prompts: Click "Continue" through introduction and license agreements
   3. Install: Click "Install" and enter your macOS password if prompted
   4. Finish: Click "Close" when installation completes

5. Repeat step 3 to verify correct version is installed
6. Install required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
7. (Optional) To increase verses per topic, adjust `verse_ct` in the main section at the bottom of the script
8. Run the scraper:
   ```bash
   python openbiblescraper.py
   ```

### Topics Setup

**Important Notes:**
- Ensure all Knowledge Base files are downloaded
- All Topics are independent from one another and can be created in any order
- Premade system Topics (Greeting, Thank you, Goodbye, etc.) cannot be deleted and are required for smooth operation

#### Creating a Topic from Scratch (Example: Academic Calendar)

1. Go to Topics Section and click "Add a Topic" → "From Blank"
2. Label the Topic "Academic Calendar"
3. Configure the trigger node:
   - Keep the setting "The agent chooses"
   - Add this description:
     ```
     This topic handles questions regarding important dates and deadlines at Oral Roberts University. It covers start and end dates for classes, holidays (Fall Break, Spring Break, Thanksgiving), final exam schedules, add/drop deadlines, and tuition refund schedules for Residential, Online, and Graduate programs. Use this for queries like 'When does school start?', 'When is finals week?', or 'What is the refund schedule?'
     ```

4. **Add Generative Answers Node:**
   - Press "+" below the trigger node
   - Go to "Advanced" section at bottom of pop-up
   - Select "Generative Answers"

5. **Configure Knowledge Source:**
   - Click "Edit" under "Data sources"
   - Select "Add Knowledge"
   - Drop the "Academic Calendar" files (6 PDFs):
     - Fall 2025 - Spring 2026 Online & Lifelong Learning PDF
     - Fall 2025 - Spring 2026 Residential & Virtual Calendar and Refund Schedule
     - Fall 2025 and Spring 2026 Advantage calendar and refund schedule
     - Fall 2027 - Spring 2028 Residential & Virtual Academic Calendar & Refund Schedule
     - Summer 2026 Calendar & Refund Schedule
     - Fall 2026 - Spring 2027 Residential & Virtual Academic Calendar & Refund Schedule
   - Toggle "Group these files"
   
6. **Add Description:**
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
   - Click "input" on the Generative Answer Node
   - Go to "System" in the pop-up panel
   - Find and select `Activity.Text`
   - Press Save

#### Quick Setup Using YAML Files

Due to the complexity of creating topics from scratch, all flow chart code has been exported to `.yaml` files:

1. Create a new topic from blank
2. Open the code editor (click the 3 dots)
3. Paste in the corresponding YAML file from the Topics folder
4. Repeat for each topic in alphabetical order

## Topics Overview

### Academic Calendar
Provides comprehensive scheduling information for academic years, extending up to two years into the future.

### Admissions
Offers detailed information regarding the admissions process, course registration procedures, and available housing and meal plan options.

### Athletics
Supplies detailed information about ORU's 16 intercollegiate sports teams, including official rosters, schedules, and recruitment guidelines.

### Campus Events & Visitation
Delivers information on significant campus happenings, such as Culture Fest and student organization activities, along with instructions for scheduling campus visits.

### Dining Information
Provides current operating hours for all campus dining facilities and details regarding designated meal exchange times.

### Direct Verse Usage
Offers biblically grounded guidance by supplying multiple scripture verses relevant to the user's specific request or need.

### FAQ 1, 2, 3
Addresses concise, single-query questions not categorized under a primary topical area.

### Financial Aid
Offers detailed guidance on the cost of attendance, FAFSA application procedures, and available scholarship opportunities.

### IT
Manages technical support inquiries related to ORU user accounts, campus technology infrastructure, and digital services.

### Library Reservation
Guides users through the process of reserving private study rooms within the university library facilities.

### ORU Program Information
Provides targeted, in-depth information for users seeking details on specific academic majors offered at the university.

### Petition Formatting
Directs users to the appropriate online portal for academic petitions and provides clear instructions on required formatting and submission procedures.

### Residential Services
Handles all inquiries exclusively pertaining to on-campus residence halls and student accommodations at Oral Roberts University.

### Student Classifier
Activates when a user mentions elements related to academic status (e.g., class, major, minor, instructor, exam) or familial academic inquiries (e.g., son, daughter, student).

### Student Life
Addresses inquiries concerning the broader campus living environment, student services, and extracurricular engagement at Oral Roberts University.
