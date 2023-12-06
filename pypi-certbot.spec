#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v3
# autospec commit: c1050fe
#
Name     : pypi-certbot
Version  : 2.8.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/f7/e3/6e20eb27fca5fc4e95d43a53f96d5e8f72565983f9acd64b840c09c3777f/certbot-2.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f7/e3/6e20eb27fca5fc4e95d43a53f96d5e8f72565983f9acd64b840c09c3777f/certbot-2.8.0.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
|build-status|
.. |build-status| image:: https://img.shields.io/azure-devops/build/certbot/ba534f81-a483-4b9b-9b4e-a60bec8fee72/5/master
:target: https://dev.azure.com/certbot/certbot/_build?definitionId=5
:alt: Azure Pipelines CI status
.. image:: https://raw.githubusercontent.com/EFForg/design/master/logos/eff-certbot-lockup.png
:width: 200
:alt: EFF Certbot Logo

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

%description python3
python3 components for the pypi-certbot package.


%prep
%setup -q -n certbot-2.8.0
cd %{_builddir}/certbot-2.8.0
pushd ..
cp -a certbot-2.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701897973
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-certbot
cp %{_builddir}/certbot-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-certbot/4bdc361ecc9ed00f502ec709aabdf54cc856b5cb || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
