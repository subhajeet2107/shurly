<p align="center"><img src="https://github.com/subhajeet2107/shurly/blob/master/frontend/public/img/icons/shurly_main.png" /></p>

Shurly
======

Fastest 🚀 Feature Rich URL Shortener with built in Analytics 🐢

[![Build Status](https://travis-ci.com/subhajeet2107/shurly.svg?branch=master)](https://travis-ci.org/subhajeet2107/shurly)
[![Coverage Status](https://coveralls.io/repos/github/subhajeet2107/shurly/badge.svg?branch=master)](https://coveralls.io/github/subhajeet2107/shurly?branch=master)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>


## Development
+ run `docker-compose up --build`

## Usage

Creating short urls in Shurly is very easy, just paste the long url in shorten box provided on homepage

![How to use](https://github.com/subhajeet2107/shurly/blob/master/frontend/public/img/shurly_usage.gif)

## Features
Shurly is an open source , highly customisable and simplest possible but powerful URL shortening service build with modern technologies and scalablilty in mind, it should be very easy and simple to host shurly on any server, follow the instructions on how to deploy and setup. Shurly uses Vue JS for the frontend and Django as the backend keeping a very loosly coupled architecture, the project provides:
- A frontend to easily shorten urls
- Uses custom hasher to quickly generate short URL safe and twitter ready short urls
- A build in RESTful API provided by Django rest framework to be used
- An extensible backend created with Django which includes adding custom integrations
- Every time a url is opened we captured redirects for every user, to check stats just replace `/r/short_code` to `/s/short_code`

## Architecture

- Python 3, supports python 2.7 till 3.7
- Django Rest API backend
- Shurly backend is created in Django
- Postgres DB ( Can be used with MySQL or any other database which is supported by Django)
- Vue JS
- Axios
- Nginx with Production and Development Configurations
- Docker
- Docker Compose

## Installation/Setup

- Open terminal and git clone this repository: https://github.com/subhajeet2107/shurly
- Then run  `docker-compose up --build` to setup the entire project, make sure you have docker installed
- This project follows 12 factor princples and you can change dynamic values using Environment settings
- DB Setup: Change database settings with the following variables

`POSTGRES_HOST=postgres
POSTGRES_DB=shurly
POSTGRES_PASSWORD=mysecretpass
POSTGRES_USER=postgresuser
`

## Using Shurly API

### User Registration:


`
curl -XPOST http://127.0.0.1:8000/api/user/ -H 'Content-Type: application/json' -d '{
"email": "admin123@gmail.com",
"name": "Admin"
"password": "admin@123"
}'
`

### List all URLs:


`
curl -XGET http://127.0.0.1:8000/api/director/
`

### Shorten a URL:

`
curl -XPOST http://127.0.0.1:8000/api/director/ -H 'Content-Type: application/json' -d '{
"original_url": "https://www.some-very-long-url.com/"
}'
`
This will return a JSON response with short_url which you can use, this will be relative to the website where Shurly is hosted

### Get a short URL by id:


`
curl -XGET http://127.0.0.1:8000/api/director/2/
`


## Contributions

Contributions are welcome, just open a pull request to add a new feature, make sure to generate coverage report and travis is happy


## License

MIT License

Copyright (c) 2019 Subhajeet Dey (https://twitter.com/_subhajeet_)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

