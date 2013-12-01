nose-parallel
==========

A plugin to help split up your tests runs across multiple machines.

In an ideal world, test suites should be fast enough that they can 
be run locally without extra engineering. This plugin is there to help 
when you can't get that to happen.

This **won't** help you run tests in parallel on one machine in different 
threads; that's what the built-in `multiprocess 
<http://nose.readthedocs.org/en/latest/plugins/multiprocess.html>`_ plugin 
is for.

This **will** help you split up your test suites so that you can run the 
suites on multiple machines and not have the same test run twice - think 
Jenkins with the 
`multijob <https://wiki.jenkins-ci.org/display/JENKINS/Multijob+Plugin>`_ 
plugin, or CI services like `CircleCI <https://circleci.com/docs/parallel-manual-setup>`_.


Install
-------

.. code::

   pip install nose-parallel


Usage
-----

On each machine:

1 Export environment variables ``NODE_TOTAL`` (the number of machines on which
the suite will be run) and and ``NODE_INDEX``(the 0-based index of this machine)
2 Run nosetests with the ``--with-parallel` flag
3 Do something to join the results from all the machines back together

For example, this is how we'd run nosetests on the second machine in a 
four-machine testing cluster:

.. code:: bash

   NODE_TOTAL=4 NODE_INDEX=1 nosetests --with-parallel
   



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
