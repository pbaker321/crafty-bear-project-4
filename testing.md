## ***Testing***

### ***User Stories Testing***

![user-stories-test](README_FILES/user-story-test.jpg)

* After i started the project i decided to not do package sizes

* I did add a customer review section, that i had previously decided on.


:biohazard: Bugs
======

### Emails
* Trouble with the confirmation and verification emails stopped being sent once the project was deployed to heroku.
* Updated to the variable names on both settings.py and config settongs on heroku. Problem fixed, although there was no typo

### Stripe Webhooks. Are sending but timing out at the source end.
* I removed all but the payment webhooks

### Dependencies disapearing
* Throughout I had to reload all dependcies. I discovered this was due to a gitpod update. 

### ***HTML Validation***
[![W3C](https://img.shields.io/static/v1?style=for-the-badge&message=W3C&color=005A9C&logo=W3C&logoColor=FFFFFF&label=)](https://validator.w3.org/)

![html-check](README_FILES/html-checker.jpg)

### ***CSS Validation***
[![W3C](https://img.shields.io/static/v1?style=for-the-badge&message=W3C&color=005A9C&logo=W3C&logoColor=FFFFFF&label=)](https://jigsaw.w3.org/css-validator/)

#### **Checkout CSS file**

![checkout-css](README_FILES/css-checkout.jpg)

#### **Base CSS File**

![base-css](README_FILES/css-base.jpg)

### ***JavaScript Validation***
[JShint](https://jshint.com/)

#### **Static JS checkout file**

![checkout-js](README_FILES/jshint-checkout.jpg)

#### **Static JS profiles file**

![profiles-js](README_FILES/jshint-profiles.jpg)

### ***Python Validation***
[PEP8online](http://pep8online.com/)

#### **Checkout Views**
![views-checkout](README_FILES/views-checkoutpep8.jpg)

#### **Profile Views**
![views-profile](README_FILES/views-profilespep8.jpg)

#### **Webhook Handler**
![wh-handler](README_FILES/wh-handlerpep8.jpg)


## ***Performance Testing***

### **Lighthouse**

#### Desktop
![desktop-Lighthouse](README_FILES/lighthouse-desktop.jpg)

#### Mobile
![Mobile-Lighthouse](README_FILES/lighthouse-mobile.jpg)