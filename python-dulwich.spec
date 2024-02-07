# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-dulwich
Epoch: 100
Version: 0.22.4
Release: 1%{?dist}
Summary: Pure-Python Git implementation
License: Apache-2.0
URL: https://github.com/jelmer/dulwich/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools-rust
BuildRequires: rust >= 1.64.0

%description
It aims to provide an interface to git repos (both local and remote)
that doesn't call out to git directly but instead uses pure Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-dulwich
Summary: Pure-Python Git implementation
Requires: python3
Requires: python3-urllib3 >= 1.25
Requires: python3-typing-extensions
Provides: python3-dulwich = %{epoch}:%{version}-%{release}
Provides: python3dist(dulwich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dulwich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dulwich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dulwich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dulwich) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-dulwich
It aims to provide an interface to git repos (both local and remote)
that doesn't call out to git directly but instead uses pure Python.

%files -n python%{python3_version_nodots}-dulwich
%license COPYING
%{_bindir}/*
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-dulwich
Summary: Pure-Python Git implementation
Requires: python3
Requires: python3-urllib3 >= 1.25
Requires: python3-typing-extensions
Provides: python3-dulwich = %{epoch}:%{version}-%{release}
Provides: python3dist(dulwich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dulwich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dulwich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dulwich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dulwich) = %{epoch}:%{version}-%{release}

%description -n python3-dulwich
It aims to provide an interface to git repos (both local and remote)
that doesn't call out to git directly but instead uses pure Python.

%files -n python3-dulwich
%license COPYING
%{_bindir}/*
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-dulwich
Summary: Pure-Python Git implementation
Requires: python3
Requires: python3-urllib3 >= 1.25
Requires: python3-typing-extensions
Provides: python3-dulwich = %{epoch}:%{version}-%{release}
Provides: python3dist(dulwich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dulwich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dulwich) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dulwich = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dulwich) = %{epoch}:%{version}-%{release}

%description -n python3-dulwich
It aims to provide an interface to git repos (both local and remote)
that doesn't call out to git directly but instead uses pure Python.

%files -n python3-dulwich
%license COPYING
%{_bindir}/*
%{python3_sitearch}/*
%endif

%changelog
