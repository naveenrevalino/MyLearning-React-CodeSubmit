# [Toubib](https://en.wiktionary.org/wiki/toubib) API - Fullstack Code Challenge

First week at Dialogue!

The team you've joined has already delivered a initial part of Toubib®, an Electronic
Medical Record application.

Toubib® currently has an api that allows creating and reading patient records.
It also allows to create, read and delete doctors.

The next iteration is to be able to list and delete patients from the web app.

After refining, the team believes that it should take at most 4 hours.

# What to deliver?

You have to complete these 4 tasks:

1. Connect the app to the API : Done
2. Create a responsive grid card layout for the patients : Done
3. Add a pagination for the patient list : Done
4. Deliver the delete patient endpoint : Done

## 1. Connect the app to the API : Completed

Connect the app to the API to display the list of patients.
The app should automatically fetch patients when it starts.
Add tests.

## 2. Create a responsive grid card layout for the patients : Completed

Try to replicate the styling (it doesn't need to be pixel perfect) of the patient cards, and the responsiveness of the grid layout as built here:

https://user-images.githubusercontent.com/6495392/155193291-fc99a407-6ba9-4e7c-bd4a-6b060bd35302.mov

## 3. Add a pagination for the patient list : Completed

The results should display 10 patients per page, with a way of navigating directly to the first and last page.
The pagination should be responsive.

## 4. Complete the delete patient feature : Completed

Add the endpoint with the relevant tests.
Hook the app to use the newly created endpoint to be able to delete patients by clicking on a trash icon.

# App Quickstart

The app is using [React](https://reactjs.org/) and is bootstrapped with [Vite](https://vitejs.dev/).

Inside the `toubib-webapp`folder, use

```
npm install
```

and

```
npm run dev
```

to launch the app.

# API Quickstart

The API is a [FastAPI](https://fastapi.tiangolo.com/) app running against an sqlite DB.

We advise you to use docker.

But feel free to use a local python 3.12 and [poetry](https://python-poetry.org/) if you feel more comfortable doing so.

A `Makefile` with all usefull commands is provided.


## Run the API

```sh
make docker-run-app
```

It launches the api locally on the port 8000.

Check the api doc on http://localhost:8000/docs


## Run tests

```sh
make docker-test
```

# Evaluation

Your submission will be evaluated against:

1. **Functionality.** Are the requirements fulfilled?
2. **Tests**. Is it tested?
