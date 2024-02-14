Name:       override-hostname
Version:    0.0.1
Release:    1%{?dist}
Summary:    Override gethostname() using LD_PRELOAD

License:    0BSD

URL:        https://github.com/im-0/fedora-rpm.override-hostname

Source0:    Makefile
Source1:    lib.c

BuildRequires:  gcc
BuildRequires:  make


%description
Override gethostname() using LD_PRELOAD.


%prep
cp %{SOURCE0} ./
cp %{SOURCE1} ./


%build
%make_build


%install
mkdir -p %{buildroot}/%{_libdir}/%{name}
cp liboverride-hostname.so %{buildroot}/%{_libdir}/%{name}/


%files
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/liboverride-hostname.so


%changelog
* Wed Feb 14 2024 Ivan Mironov <mironov.ivan@gmail.com> - 0.0.1-1
- Initial packaging
