#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-certbot
Version  : 1.26.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/9c/78/90a464a4a10c6ac506243273db9bae4186b36e7c02e47ee613403e7d95cb/certbot-1.26.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9c/78/90a464a4a10c6ac506243273db9bae4186b36e7c02e47ee613403e7d95cb/certbot-1.26.0.tar.gz
Summary  : ACME client
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-certbot-bin = %{version}-%{release}
Requires: pypi-certbot-license = %{version}-%{release}
Requires: pypi-certbot-python = %{version}-%{release}
Requires: pypi-certbot-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(acme)
BuildRequires : pypi(configargparse)
BuildRequires : pypi(configobj)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(distro)
BuildRequires : pypi(josepy)
BuildRequires : pypi(parsedatetime)
BuildRequires : pypi(pyrfc3339)
BuildRequires : pypi(pytz)
BuildRequires : pypi(pywin32)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(zope.component)
BuildRequires : pypi(zope.interface)

%description
Certbot is part of EFF’s effort to encrypt the entire Internet. Secure communication over the Web relies on HTTPS, which requires the use of a digital certificate that lets browsers verify the identity of web servers (e.g., is that really google.com?). Web servers obtain their certificates from trusted third parties called certificate authorities (CAs). Certbot is an easy-to-use client that fetches a certificate from Let’s Encrypt—an open certificate authority launched by the EFF, Mozilla, and others—and deploys it to a web server.

%package bin
Summary: bin components for the pypi-certbot package.
Group: Binaries
Requires: pypi-certbot-license = %{version}-%{release}

%description bin
bin components for the pypi-certbot package.


%package license
Summary: license components for the pypi-certbot package.
Group: Default

%description license
license components for the pypi-certbot package.


%package python
Summary: python components for the pypi-certbot package.
Group: Default
Requires: pypi-certbot-python3 = %{version}-%{release}

%description python
python components for the pypi-certbot package.


%package python3
Summary: python3 components for the pypi-certbot package.
Group: Default
Requires: python3-core
Provides: pypi(certbot)
Requires: pypi(acme)
Requires: pypi(configargparse)
Requires: pypi(configobj)
Requires: pypi(cryptography)
Requires: pypi(distro)
Requires: pypi(josepy)
Requires: pypi(parsedatetime)
Requires: pypi(pyrfc3339)
Requires: pypi(pytz)
Requires: pypi(pywin32)
Requires: pypi(setuptools)
Requires: pypi(zope.component)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-certbot package.


%prep
%setup -q -n certbot-1.26.0
cd %{_builddir}/certbot-1.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649725080
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-certbot
cp %{_builddir}/certbot-1.26.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/certbot

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
