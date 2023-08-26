Name:           alsa-ucm-conf
Version:        1.2.9
Release:        0
Summary:        ALSA UCM Profiles
License:        BSD-3-Clause
URL:            https://www.alsa-project.org
Source:         alsa-ucm-conf-%{version}.tar.bz2
BuildArch:      noarch
Requires:       alsa-lib >= 1.2.8

%description
This package contains the profiles files for ALSA UCM (Use Case Manager).

%prep
%autosetup -p1
find . -name ".gitignore" -delete

%build

%install
mkdir -p %{buildroot}%{_datadir}/alsa
cp -a alsa-ucm-conf/ucm %{buildroot}%{_datadir}/alsa/
cp -a alsa-ucm-conf/ucm2 %{buildroot}%{_datadir}/alsa/

%files
%{_datadir}/alsa

%changelog
