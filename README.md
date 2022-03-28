# TO DO API
![PYTHON-3.9.6](https://img.shields.io/badge/PYTHON-3.9.6-blue)
![FastAPI-0.75.0](https://img.shields.io/badge/FastAPI-0.75.0-brightgreen)
![MongoDB](https://img.shields.io/badge/MongoDB-orange)
![REST API](https://img.shields.io/badge/RESTful-API-yellow)


### RUN IT MANUALLY
before you run the api, be sure to install all the required modules via your terminal

```jsx
$ pip install -r requirements.txt
```

then change the directory

```jsx
$ cd app
```

once we are here, we should note that uvicorn is already installed when you executed the first command.
now, to run the server type the following in your terminal. this should be done inside the app directory

```jsx
uvicorn main:app --reload
```
### HOW IT WORKS?

once the server starts running, open your browser and load up the port and go to docs. By default the port is

```jsx
http://127.0.0.1:8000/docs
```
once you load up this page, you shall see something like this.

![OPENING](https://lh3.googleusercontent.com/uQ77nriPIWOIS84B3bjqSbH1rcHwhzMO12QPyRICw1o8Olf0TahN_vQfaNUdeS6x_DxDQHPTabXy2BjEE046UHBQY8XpSLaccCCwKpNTV5YOVZURCCRVL1cFAalNsLoN7UHzCvGrGQ=w2400)

on the top right corner under the header(Todo API) you shall see a green button named "Authorize". click it to authorizr the api and get the header token.

The authorize box looks like this, enter the username and password to authorize yourself.
![auth](https://lh3.googleusercontent.com/dUL1X73LIFzU7Orl4rF68C5Sl8CuUyns4ydr5KshYZ9eDPrjQC2KI87lx1CvjIsLNCDWnl4ke_7VQDs7CHL6BVlpPBsj-XBDSeo066hIk8k0va9Fe-fLjCDlhZQYZfLLeQFS1i6dCQ=w2400)

close the box after that
![auth1](https://lh3.googleusercontent.com/TgsYmvpEQXmUcTr7OV-_CiZpfn-SvSIcqJDAczd0LUjwnRLiH9askP7ESbwabNKe-M97I4GF2pPcl4YecvP5UQrxAnWbm5crhyQ6q8UQwukJQUWWVp-n0cA-1uBbek2qsK6a7KxYDA=w2400)
