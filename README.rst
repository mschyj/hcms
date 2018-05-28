========================================================================
   HWCC-HPC Cluster Deployment Tool 
========================================================================

.. This file follows reStructuredText markup syntax; see
   http://docutils.sf.net/rst.html for more information

HWCC aims to provide a user-friendly command line tool to
create, manage and setup computing clusters hosted on OpenStack_ cloud
infrastructures. Its main goal is to get your own private cluster up and running with just a few
commands.

The HWCC project is licensed under the `GNU General Public License version 3`_.

Features
========

HWCC is in active development, and offers the following
features at the moment:

* INI-style configuration file to define cluster templates
* Can start and manage multiple independent clusters at the same time
* Automated setup of:
 * HPC clusters using SLURM_;
 * ...or anything that you can install with an Ansible_ playbook!
* Growing and shrinking a running cluster.

HWCC is currently in active development: please use the
GitHub issue tracker to file enhancement requests and ideas.

We appreciate pull requests for new features and enhancements. Please
use the *master* branch as starting point.


Quickstart
==========

Please use QuickStart.txt to start your travel with this tool.

After HWCC is installed, run this command to initialize the environment

  sh Inithwcc.sh

The configuration file is located in `.hwcc/config`.

Getting help
============

For anything concerning HWCC, including trouble running the
installation script, please send an email to mschyj@sina.com


.. References

   References should be sorted by link name (case-insensitively), to
   make it easy to spot a missing or duplicate reference.

.. _`Ansible`: https://ansible.com/
.. _`CentOS`: http://www.centos.org/
.. _`Ceph`: http://ceph.com/
.. _`Debian GNU/Linux`: http://www.debian.org
.. _`github`: https://github.com/
.. _`GNU General Public License version 3`: http://www.gnu.org/licenses/gpl.html
.. _`OpenStack`: http://www.openstack.org/
.. _`pip`: https://pypi.python.org/pypi/pip
.. _`python virtualenv`: https://pypi.python.org/pypi/virtualenv
.. _`Python`: http://www.python.org
.. _`SLURM`: https://slurm.schedmd.com/
.. _`Ubuntu`: http://www.ubuntu.com

.. (for Emacs only)
..
  Local variables:
  mode: rst
  End:
