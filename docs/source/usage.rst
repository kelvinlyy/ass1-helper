Usage
=====

.. _create_users:

Create Users
------------


To use the REST API to create users, first you need to define
the attributes of the users in ``gen_user.py``.

Then, run ``gen_user.py`` to generate ``create_user.json``

Last, run ``setup_user.py`` to send the request

It basically calls the ``admin_agent.create_keycloak_user(create_request)``:


.. _create_jobs:

Create Jobs
-----------

To use the REST API to create jobs, first you need to define
the attributes of the jobs in ``gen_job.py``.

Then, run ``gen_job.py`` to generate ``create_job.json``

Last, run ``setup_job.py`` to send the request


.. code-block:: console

    Coding is fun!
