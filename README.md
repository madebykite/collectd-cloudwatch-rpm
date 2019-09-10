CollectD CloudWatch RPM
=======================

Packages the [collectd-cloudwatch][1] CollectD plugin as an RPM.

Configuration
-------------

Configuration files are located in `/opt/collectd-plugins/cloudwatch/config`. Documentation on configuring the plugin can be found on the [collectd-cloudwatch Github project][2].

Development
-----------

### Dependencies

* [`docker`](https://docs.docker.com/install/)
* [`docker-compose`](https://docs.docker.com/compose/install/)

You can package and install by running the following:

    docker-compose up
    
You can inspect the installation by invoking a shell:

    docker-compose run collectd-cloudwatch bash -l

[1]: https://github.com/awslabs/collectd-cloudwatch
[2]: https://github.com/awslabs/collectd-cloudwatch#configuration
