nose-parallel
==========

A plugin to help split up your tests runs across multiple machines.

In an ideal world, test suites should be fast enough that they can 
be run locally without extra engineering. This plugin is there to help 
when you can't get that to happen.

Install
-------

.. code::

   pip install nose-parallel


Usage
-----

Run nosetests with the ``--with-timer`` flag, and you will see a list of the
tests and the time spent by each one (in seconds):

.. code:: bash

   myapp.tests.ABigTestCase.test_the_world_is_running: 56.0010s
   myapp.tests.ABigTestCase.test_the_rest_of_the_galaxy_is_running: 2356.0010s


How do I show only the ``n`` slowest tests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For example, to show only the **10** slowest tests, run nosetests with
``--timer-top-n`` flag.

.. code:: bash

   nosetests --with-timer --timer-top-n 10


How do I color the output and have pretty colors?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can highlight slower tests using ``--timer-ok`` and ``--timer-warning`` flags.

- Tests which takes less time than ``--timer-ok`` will be highlighted green.
- Tests which takes less time than ``--timer-warning`` will be highlighted yellow.
- All other tests will be highlighted red.


How do I increase timer verbosity?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default nose-timer outputs test times at the end of all tests.
You can output test times after each test with ``--timer-verbose`` flag.
Note that ``--vv`` should be enabled as well to view info logs.

.. code:: bash

    nosetests --with-timer --timer-verbose -vv .


License
-------

``nose-parallel`` is released under the MIT license.


Contribute
----------

- Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
- Fork the repository on GitHub to start making your changes to the master branch (or branch off of it).
- Send a pull request and bug the maintainer until it gets merged and published.
- Make sure to add yourself to the authors list in ``setup.py``


Thanks To
---------

- `@mahmoudimus <https://github.com/mahmoudimus>`_, whose `nose-timer <https://github.com/mahmoudimus/nose-timer>`_ plugin this is based off of
