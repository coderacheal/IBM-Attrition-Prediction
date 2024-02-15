<a name="readme-top"></a>

<div align="center">
  <h1><b>Wine Grader</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Wine Grader ](#wine-grader-)
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors ](#-authors-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Wine Grader <a name="about-project"></a>

**Wine Grader** This is a Machine Learning API built with FastAPI to predict Wine grades.

Features
1. **Alcohol:** The alcohol content of the wine.
2. **Malic acid:** The amount of malic acid in the wine, which can affect the taste and acidity.
3. **Ash:** The ash content in the wine, representing the inorganic content after incineration.
4. **Alcalinity of ash:** The alkalinity of the ash, which can influence the taste and pH of the wine.
5. **Magnesium:** The amount of magnesium in the wine.
6. **Total phenols:** The total amount of phenolic compounds in the wine, which contribute to its flavor and color.
7. **Flavanoids:** The amount of flavonoids in the wine, which are responsible for various sensory attributes.
8. **Nonflavanoid phenols:** The amount of non-flavonoid phenolic compounds in the wine.
9. **Proanthocyanins:** The amount of proanthocyanins, a type of antioxidant, in the wine.
10. **Color intensity:** The color intensity of the wine, which can be influenced by various compounds.
11. **Hue:** The hue of the wine, representing the color shade.
12. **OD280/OD315 of diluted wines:** The optical density of the wine, which is measured at two different wavelengths. It can provide information about the color.
13. **Proline:** The amount of proline, an amino acid, in the wine.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="">Uvicorn</a></li>
  </ul>
</details>

<details>
<summary>Container</summary>
  <ul>
    <li><a href="">Docker</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">Sklearn</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Features <a name="key-features"></a>

- **An API endpoint to predict wine grades**
- **A home and info endpoint**


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python
- Docker

### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/coderacheal/Wine-Grader-Machine-Learning-API.git
```

Change into the cloned repository

```sh
  cd Wine-Grader-Machine-Learning-API
  
```

Create a virtual environment

```sh

python -m venv virtual_env

```

Activate the virtual environment

```sh
    virtual_env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


### Usage

To run the project, execute the following command:


```sh
  uvicorn main:app --reload 

  OR 

  uvicorn main:app 
```

- Click on the `http://127.0.0.1:8000` that show up in the terminal
- In the browser add a `/docs` to see the Swagger UI for Fastapi
- Finally test a prediction by clicking on the     `Try it out` button that shows up when you click on the prediction function or endpoint

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Racheal Appiah-kubi**

- GitHub: [GitHub Profile](https://github.com/coderacheal)
- Twitter: [Twitter Handle](https://twitter.com/racheal_kubi)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/racheal-appiah-kubi/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>


- **Add a front end application for users**
  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank all the free available resource made available online

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


