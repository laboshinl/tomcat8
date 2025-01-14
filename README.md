# Tomcat 8

Tomcat 8 RPM for CentOS 7, built from upstream binaries: https://tomcat.apache.org

The service is installed under `/opt/tomcat8`, requires OpenJDK 1.8 and runs under the `tomcat` user.
The `examples` directory is not bundled with this package.

To start the service there are 2 different systemd services:

- `tomcat8.service`: control a standard Tomcat instance, webapps should be placed under `/opt/tomcat8/webapps/`
- `tomcat8@.service`: control multiple instances of the service, you must define `CATALINA_BASE` inside `/etc/sysconfig/tomcat8@<instance` file
  This service can be used to start applications previously installed under Tomcat 7 and hosted inside `/var/lib/tomcats` directory.
- `tomcat8-nojsvc@.service`: same as `tomcat8@.service`, but this service don't use `jsvc` for launch the application, instead use `java` directly.
  This approach make possible to use standard Java debug tools, but the application can't perform some privileged operations (e.g. bind to a port < 1024).


