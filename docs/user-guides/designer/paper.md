---
tags: [designer]
---

# The Paper

From a school's perspective, the **Paper** can be referred to as Modules, Courses or Subjects, etc. depending on what term it bears in your school.

> Note: Multiple Papers can be created under an Exam.

#### Creating an Exam Paper

Here are the processes to follow in order to create a Paper. We assume you are starting fresh. If, however, you have already created an Exam, you can skip to **Step 3**.

1. Click on `File` 

    ![Designer First Step](../../assets/images/Designer_Images/Intro_Designer_first_start.jpg)

2. From the resulting drop-down, Click on `New Exam Project`. This creates an `Untitled Exam` for you.

3. Right click on the Exam title from the `Exam Explorer`, in this case ours is `Untitled Exam`, You may have renamed the 'Untitled Exam', the menu options reveal the option for `New Exam Paper`, click on it and a paper with a default title is created. In this case, the title is `Paper 1`. You can modify the title of the Paper from the Paper properties. However, no two papers can bear the same name.

4. Clicking on the `Paper 1` activates the Paper Properties from which you can edit and set feature preferences.

    ![Paper Environment](../../assets/images/Designer_Images/Paper_Environment.jpg)
    *The Designer application shows when a newly created Paper is selected.*

#### **Paper Properties and Settings**

Papers can be customized to meet your preferences. This section explains some of the available properties and explains the options. 

![Paper Properties](../../assets/images/Designer_Images/Paper_Properties1.jpg)

- **Paper Title:** This is the name of Paper/Subject the examinee is to write, and like the Exam name, it is also visible to the examinee. e.g. Use of English, Aptitude111, Math 101, Bio 201 etc.

- **Paper Description and Paper Instruction:**  Unlike the Instruction and Description fields on The Exam Properties, this isn't compulsory, unless you select the `Show Description and Instruction before paper starts` checkbox.

- **Paper Duration:** This is the Time duration of the Paper in minutes. The minimum allowed time is 5 minutes.

- **Section Arrangement:**  Section Arrangement defines how the questions would be lined up or presented to examinees will taking the exam. i.e. if you wish the questions to flow in sequence or appear randomly. 

    (e.g. In The Use of English, If you have three sections listed in order 
    - Oral English
    - Comprehension 
    - Nearest in meaning 
    
    With **RANDOMIZED** setting, the system gets to pick questions randomly in no particular order from the above listed sections. 
    However, When on a **SEQUENTIAL** setting, the questions will first come from 'Oral English', next from 'Comprehension' and finally from 'Nearest in Meaning'.)

  ![Paper Sequence](../../assets/images/Designer_Images/PaperSectionArrangementRandomizedSequential.jpg)

Clicking on the `Contents and Sections` tab at the foot of the page, reveals further settings which can be utilized to effect changes on the Paper Contents and Paper Sections.
e.g. you can assign the number of questions to be answered from each section, while also deciding if the questions within a single section is randomized or sequenced.

- **Questions to Answer:** This defines the number of questions which examinees would be presented to answer while taking the Paper. 

  This is most useful if you wish to allow questions to be selected randomly as a subset of a 'question bank'.
This means that there may be times when you have created or imported a pool of questions from which you would want examinees to answer from, desginating a specific number of questions to answer will ensure the systems presents just that to the examinee. 

  It is advisable to set this after all Questions have been created, this is because further question addition after selecting the number of **Questions to Answer** invalidates this settings, returning it to the total number of questions add to The Paper. 

- **Calculator Type:**  Gives options to either allow or deny the use of calculator for each paper. Calculator types are Simple (for basic operations), Advanced (for scientific calculator operations) and Base (for Bin, Hex, Oct and Decimal operations).

- **Show Question Marks:** By default each question is assumed 1 mark, however you can allocate different marks to different questions. So, this feature controls the option to show the mark associated with each question while the examinee is taking an exam.

#### Importing Questions from a File or another Project

![Import or Download Questions](../../assets/images/Designer_Images/Download_or_Import_Questions.jpg)

- To import questions from a text file, word pad or another SmartExaminer project file (*.smexproj, .smex*), right click on an Exam `Paper` you have created to reveal a context menu.

- Then Click on `Import Questions from File`.

Importing questions from file is an interesting process which has its own dedicated page which you can [read here](importing-questions.md).
