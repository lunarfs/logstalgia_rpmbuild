Name:           logstalgia
Version:        1.0.7
Release:        0%{?dist}
Summary:        Logstalgia is a visualization tool that replays or streams web server access logs as a retro arcade game simulation.
Group:          Applications/Multimedia
License:        GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
URL:            https://github.com/acaudwell/Logstalgia
Vendor:         Andrew Caudwell
Source:         https://github.com/acaudwell/Logstalgia/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Prefix:         %{_prefix}
Packager: 	Frank Vissing
BuildRoot:      %{_tmppath}/%{name}-root


%description

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir}

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README THANKS COPYING
%{_mandir}/*
%{_bindir}/logstalgia
%{_prefix}/share/logstalgia/*

