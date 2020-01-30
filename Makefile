PKGNAME=nagios-plugins-seadatacloud-check_cas
SPECFILE=${PKGNAME}.spec
FILES=Makefile ${SPECFILE} check_cas.pl

PKGVERSION=$(shell grep -s '^Version:' $(SPECFILE) | sed -e 's/Version:\s*//')


dist:
	rm -rf dist
	mkdir -p dist/${PKGNAME}-${PKGVERSION}
	cp -pr ${FILES} dist/${PKGNAME}-${PKGVERSION}/.
	cd dist ; tar cfz ../${PKGNAME}-${PKGVERSION}.tar.gz ${PKGNAME}-${PKGVERSION}
	rm -rf dist

sources: dist

clean:
	rm -rf ${PKGNAME}-${PKGVERSION}.tar.gz
	rm -rf dist
