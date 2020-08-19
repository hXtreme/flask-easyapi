.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/hXtreme/flask_easyapi/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.
* Expected and Actual behaviour of your code.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Other Issues
^^^^^^^^^^^^

Look through Github issuses for open issues. Things tagged "help wanted" are open to anyone; for others confirm with project team to pick up the issue.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Flask-EasyAPI could always use more documentation, whether as part of the
official Flask-EasyAPI docs, in docstrings, as additional examples, or even on the web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/hXtreme/flask_easyapi/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `flask_easyapi` for local development.

1. Fork the `flask_easyapi` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/flask_easyapi.git

3. Install your local copy into a virtualenv. This is how you set up your fork for local development::

    $ cd flask_easyapi/
    $ virtualenv env && . ./env/bin/activate
    $ pip installl -r requirements_dev.txt
    $ pip install --editable .

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, make sure to follows black's style guide 
   and check that your changes pass flake8, 
   the tests, including testing other Python versions with tox::

    $ black flask_easyapi tests
    $ flake8 flask_easyapi tests
    $ pytest
    $ tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.com/hXtreme/flask_easyapi/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests.test_flask_easyapi


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

Github workflow will then deploy to PyPI if tests pass.
