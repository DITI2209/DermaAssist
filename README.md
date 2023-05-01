# DermaAssist-firebase
Dermassist is a skin disease classification system for pathologists created using Deep Learning.

<h3>Features</h3>
Skin disease classification using a Deep Learning model
PDF generation using jsPDF
Encrypted PDFs sent to doctors via email with a randomly generated alpha-numeric password sent via SMS using Twilio
<h3>Installation</h3>
<li>Clone the repository</li>
<li>Run the Flask app using <code>python app.py</code></li>
<h3>Usage</h3>
<li>Login as pathologist using firebase authentication </li>
<li>Add Doctors and their patients</li>
<li>Upload an image of the skin condition</li>
<li>The Deep Learning model will classify the condition and generate a report</li>
<li>The report is sent to the doctor as an encrypted PDF with the password sent via SMS </li>
<h3> Tech Stack </h3>
<li> Language used: Python </li>
<li> Framework used: Flask </li>
<li> Dataset used: HAM10000 </li>
<li> Database used: Firebase </li>
<li> Frontend stack: HTML, CSS (Tailwind), Javascript </li>
<li> API used: Twilio </li>
<li> Libraries used: Tensorflow, random, newjs, smtp, email, PyPDF2, os and jinja2 </li>
