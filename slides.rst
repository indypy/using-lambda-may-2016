.. -*- coding: utf-8 -*-

...  Copyright 2016 Six Feet Up, Inc.

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.

:title: Using Python with AWS Lambda
:event: IndyPy May 2016
:author: Calvin Hendryx-Parker
:pygments: tango
:css: custom.css

.. |space| unicode:: 0xA0 .. non-breaking space
.. |br| raw:: html

    <br />

----

Using Python with AWS Lambda
============================

----

Your Presenter
==============

Calvin Hendryx-Parker, CTO
++++++++++++++++++++++++++

Six Feet Up, Inc.
-----------------

.. note::

    Introduce yourself, why are you the person they should be listening to for
    the next 45 minutes

----

What is AWS Lambda?
===================

* Server-less computing
* Event-driven
* Continuous Scaling

----

What runs on Lambda?
====================

* Python
* Java
* Node.js

----

What kinds of things do people do with Lambda?
==============================================

* S3
* Kinesis
* DynamoDB
* SNS
* API Gateway
* Mobile Backend
* Scheduled Events
* AWS IoT
* Alexa Events

.. note::
    Async calls use the Event invocation type and the return is discarded.

    Kinesis can work sync or async and can read in batches of records coming from a stream

    Lambda can subscribe to SNS topics even across accounts

    More event sources are being added such as Cognito Sync Triggers

----

What does Lambda Cost?
======================

Per Request
+++++++++++

* First 1 million requests per month are free
* $0.20 per 1 million requests thereafter

Per Compute time
++++++++++++++++

* First 400,000 GB-seconds of compute time per month are free
* Lambda instances can vary based on RAM used
* For 128MB instance, you get 3.2M seconds free
* Allows up to 1.5GB instances (266,667 seconds free)
* Billing is metered in increments of 100 milliseconds

.. note::
    All calls made to AWS Lambda must complete execution within 300 seconds

----

Let's do Python with Lambda
===========================

* Python 2.7
* Include Standard Library
* Includes the AWS SDK library, Boto 3
* You can bundle anything else you like

----

Hello Lambda
============

* Simple
* TTW
* No dependencies
* API Endpoint

----

Fetch Lambda, Good Dog
======================

* S3 Events
* Fetch Files
* Use Pillow to Convert Images
* Put the Converted Files Back

Some Pre-packaged Binaries for Lambda
+++++++++++++++++++++++++++++++++++++

https://github.com/Miserlou/lambda-packages


.. note::

    Each Lambda function receives 500MB of non-persistent disk space in its own /tmp directory

    Binary compiles can be made and just need to run on Amazon Linux

----

Lambda Telephone Game
=====================

* API Gateway
* Webhook Target for ZenDesk
* Use Requests to call another Webhook in Pingdom

----

Questions?
==========

