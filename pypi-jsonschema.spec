#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jsonschema
Version  : 4.6.0
Release  : 83
URL      : https://files.pythonhosted.org/packages/b5/a0/dd13abb5f371f980037d271fd09461df18c85188216008a1e3a9c3f8bd0c/jsonschema-4.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/a0/dd13abb5f371f980037d271fd09461df18c85188216008a1e3a9c3f8bd0c/jsonschema-4.6.0.tar.gz
Summary  : An implementation of JSON Schema validation for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-jsonschema-bin = %{version}-%{release}
Requires: pypi-jsonschema-license = %{version}-%{release}
Requires: pypi-jsonschema-python = %{version}-%{release}
Requires: pypi-jsonschema-python3 = %{version}-%{release}
Requires: pypi(pyrsistent)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi-pytest

%description
==========
jsonschema
==========
|PyPI| |Pythons| |CI| |ReadTheDocs| |Precommit| |Zenodo|

%package bin
Summary: bin components for the pypi-jsonschema package.
Group: Binaries
Requires: pypi-jsonschema-license = %{version}-%{release}

%description bin
bin components for the pypi-jsonschema package.


%package license
Summary: license components for the pypi-jsonschema package.
Group: Default

%description license
license components for the pypi-jsonschema package.


%package python
Summary: python components for the pypi-jsonschema package.
Group: Default
Requires: pypi-jsonschema-python3 = %{version}-%{release}

%description python
python components for the pypi-jsonschema package.


%package python3
Summary: python3 components for the pypi-jsonschema package.
Group: Default
Requires: python3-core
Provides: pypi(jsonschema)
Requires: pypi(attrs)
Requires: pypi(pyrsistent)

%description python3
python3 components for the pypi-jsonschema package.


%prep
%setup -q -n jsonschema-4.6.0
cd %{_builddir}/jsonschema-4.6.0
pushd ..
cp -a jsonschema-4.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656397163
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jsonschema
cp %{_builddir}/jsonschema-4.6.0/COPYING %{buildroot}/usr/share/package-licenses/pypi-jsonschema/2de1a0a3674903238a664ace5d3acc66a7d546c7
cp %{_builddir}/jsonschema-4.6.0/json/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jsonschema/6808b97edf6d2c189571af702b95916168ff7db8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonschema

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jsonschema/2de1a0a3674903238a664ace5d3acc66a7d546c7
/usr/share/package-licenses/pypi-jsonschema/6808b97edf6d2c189571af702b95916168ff7db8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
