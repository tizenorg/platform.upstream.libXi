#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           libXi
Version:        1.6.1
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System Environment/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(inputproto) >= 2.1.99.6
BuildRequires:  pkgconfig(x11) >= 1.4.99.1
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

Requires:       libX11 >= 1.4.99.1

%description
X.Org X11 libXi runtime library

%package devel
Summary:        X
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(inputproto) >= 2.1.99.6
Requires:       pkgconfig(xorg-macros)
Requires:       pkgconfig(xproto)

%description devel
X.Org X11 libXi development package

%prep
%setup -q

%build
autoreconf -v --install || exit 1
%reconfigure --disable-specs \
	       --disable-static

make %{?_smp_mflags}

%install

%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXi.so.6
%{_libdir}/libXi.so.6.1.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XInput2.h
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
