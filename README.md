
<h1 align="center">
  <b>BaTe</b>
  </h1>

<p align="center">
   <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/MADE%20WITH%20-Python-blueviolet" height="20">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Platform-Windows-black">
  </a>
  </p>

<h2>Introduction</h2>

<p>Over time, batteries lose their designed charging capacity and their ability to store the charge decreases. It is a little bit cumbersome to know the current laptop battery charging capacity. BaTe helps in achieving this by checking the battery charging capacity and logs it into a spreadsheet file. This task could be automated completely by using Windows' Task Scheduler.</p>


<h2>Pre-requisites</h2>

<p> BaTe makes use of the following Python libraries : 
<ul>
  <li>xlrd</li>
  <li>xlutils</li>
  <li>xlwt</li>
  </ul>
  </p>

<h2>Supported Platforms</h2>

<p>Windows</p>

<h2>Usage</h2>

<ul type="disc">

  <li>Clone this repository using :
  
  ```
  git clone https://github.com/InvincibleJuggernaut/BaTe.git
  ```
  </li>
  <li> Next, go inside the repository directory using :

   ```
  cd BaTe
  ```
  </li>
  <li> Install all the dependencies using:

```
pip3 install -r requirements.txt
```
</li>
  <li>There are two scripts: <i>battery-test.bat</i> and <i>battery-logger.bat</i> You could run each file individually in the same order or schedule them using Task Scheduler.</li>
</ul>

<h2>License</h2>

<a href="LICENSE">GPLv3</a>
