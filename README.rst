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
It also supports natively the default environment variables from:

- CircleCI
- Buildkite
- GitLab CI

We welcome PRs that add native support for other CI alternatives.

If you want to further randomize the distribution of tests, so
that the same test cases don't always run together on the same node, you may
use the ``--parallel-salt`` option or ``NOSE_PARALLEL_SALT`` environment variable 
to specify a salt value for the randomization (e.g. a build number, the day of the month). 
The salt must be the same on each node during a parallel build, otherwise some test cases might be missed. 

For example, on CircleCI you could do:

.. code:: bash

    nosetests --with-parallel --parallel-salt-env CIRCLE_BUILD_NUM

By default ``nose-parallel`` will split tests based on method and function names. You can customize this strategy by setting the ``--parallel-strategy`` option. Supported strategies are: 'CLASS', 'DIRECTORY', 'FILE', 'METHOD', 'FUNCTION' and 'MODULE'.

For example, to split tests based on the file names:

.. code:: bash

    nosetests --with-parallel --parallel-strategy=FILE

License
-------

``nose-parallel`` is released under the MIT license.


Contribute
----------

- Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
- Fork the repository on GitHub to start making your changes to the master branch (or branch off of it).
- Send a pull request and bug the maintainer until it gets merged and published.


Thanks To
---------

- `@mahmoudimus <https://github.com/mahmoudimus>`_, whose `nose-timer <https://github.com/mahmoudimus/nose-timer>`_ plugin this is based off of
