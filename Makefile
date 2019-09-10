name     := collectd-cloudwatch
version  := $(shell grep -i ^Version: SPECS/$(name).spec | cut -d' ' -f2)
release  ?= 1
rpmfile  := RPMS/noarch/$(name)-$(version)-$(release).noarch.rpm
topdir   := $(shell pwd)

clean:
	rm -rf BUILD SRPMS RPMS BUILDROOT

prepare: clean
	mkdir -p BUILD RPMS SRPMS

rpmbuild: prepare
	rpmbuild --define "_topdir $(topdir)" --define="Release $(release)" --undefine=_disable_source_fetch -ba SPECS/$(name).spec
