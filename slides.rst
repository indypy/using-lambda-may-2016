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

* Serverless computing
* Event-driven
* Continous Scaling

----

What runs on Lambda?
====================

* Python
* Java
* Node.js

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


----


Each Lambda function receives 500MB of non-persistent disk space in its own /tmp directory

All calls made to AWS Lambda must complete execution within 300 seconds

Includes the AWS SDK library, Boto 3

Questions?
==========

