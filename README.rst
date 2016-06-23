nose-parallel
=============

A plugin to help split up your tests runs across multiple machines.

In an ideal world, test suites should be fast enough that they can
be run locally on a single machine without extra engineering. This
plugin is there to help when you can't make that to happen.

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

.. code:: bash

   pip install nose-parallel


Usage
-----

On each machine:

#. Export environment variables ``NODE_TOTAL`` (the number of machines on which the suite will be run) and and ``NODE_INDEX`` (the 0-based index of the current machine)
#. Run nosetests with the ``--with-parallel`` flag
#. Do something to join the results from all the machines back together

For example, this is how we'd run nosetests on the second machine in a
four-machine testing cluster:

.. code:: bash

   NODE_TOTAL=4 NODE_INDEX=1 nosetests --with-parallel


If you don't set those variables, ``nose-parallel`` will do the right thing and run all your tests.
The CircleCI versions of the environment variables (``CIRCLE_NODE_TOTAL`` and ``CIRCLE_NODE_INDEX``,
respectively) are also natively supported.

If you want to further randomize the distribution of tests, so
that the same test cases don't always run together on the same node, you may
use the ``--parallel-salt`` option to specify a salt value (e.g. a build
number, the day of the month). The salt must be the same on each node
during a parallel build, otherwise some test cases might be missed.

Alternatively you can set environment variable ``NOSE_PARALLEL_SALT``. And, as
an added convenience, you can change this environment variable to something
your build environment already configures for each build with the option
``--parallel-salt-env``. E.g. on CircleCI you could do:

.. code:: bash

    nosetests --with-parallel --parallel-salt-env CIRCLE_BUILD_NUM


License
-------

``nose-parallel`` is released under the MIT license.


Contribute
----------

- Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
- Fork the repository on GitHub to start making your changes to the master branch (or branch off of it).
- Send a pull request and bug the maintainer until it gets merged and published.
- Add yourself to the authors list in ``setup.py``


Thanks To
---------

- `@mahmoudimus <https://github.com/mahmoudimus>`_, whose `nose-timer <https://github.com/mahmoudimus/nose-timer>`_ plugin this is based off of
