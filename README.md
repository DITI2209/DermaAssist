# DermaAssist-firebase

As our third-year mini project, we have created a skin cancer classification system using Deep Learning. 

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Usage](#usage)
  - [Installation](#installation)
  - [Navigation](#navigation)
- [Team](#team)
  - [Mentors:](#mentors)
  - [Members:](#members)


## Usage

### Installation 

<details>
    <summary><b>Windows, Ubuntu and MacOs</b></summary>

   1. Make sure you have the Python Interpreter with the following modules installed :
      -flask
      -twilio
      -tensorflow
      -firebase_admin
      -numpy
      -pandas
      -os
      -PyPDF2
      -jinja2
      -smtplib
      -random
  2. Clone the repository or Download the Code
  3. Open your terminal and run the python file: <code> python app.py </code>
  4. A link will appear after running this file.
  5. Click on this link and use DermaAssist.
</details>

### Navigation

<details>
    <summary><b>Instructions for using DermaAssist web application</b></summary>

   1. After you open the website on your preffered browser, login or signup as pathologist using firebase authentication.
   2. After loggin in, the pathologist
   will be presented with options to either add a new doctor to the system, view existing doctors or directly add a patient for an existing doctor.
   3. After a patient is added/selected successfully, the pathologist is presented with an option to upload the skin lesion image for classification.
   3. The deep learning model will then process the image and provide you with the appropriate diagnosis of the skin lesion image.
   5. After successful diagnosis, the pathologist will be presented with an option to generate a medical report.
   6. If selected, the medical report template allows the pathologist to digitally sign and verify the report having the appropriate diagnosis of the patient.
   7. Once the report is finalized, pathologist can mail the report to the doctor in an encrypted format.
   8. The password to the encrypted medical report pdf which is mailed to the doctor's email ID can be accessed by entering the randomly generated alpha-numeric code sent as SMS on doctor's phone for two-factor encryption.
</details>

## Team

### Project Guide:
Mrs. Pooja Malhotra <br>

### Members:
| Sr No. | Name               | E-mail                       | git-profile     |
| -------| -------------------| -----------------------------| ----------------|
| 1.     | Shriya Pingulkar   | shriya.pingulkar@somaiya.edu | shriya02-coder  |
| 2.     | Aryaman Tiwary     | aryaman.tiwary@somaiya.edu   | Aryaman0809     |
| 3.     | Diti Divekar       | diti.divekar@somaiya.edu     | DITI2209        |




