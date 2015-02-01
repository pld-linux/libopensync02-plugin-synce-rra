Summary:	OpenSync 0.2x plugin for syncing pre-2005 Windows Mobile devices
Summary(pl.UTF-8):	Wtyczka OpenSync 0.2x do synchronizacji urządzeń Windows Mobile sprzed 2005
Name:		libopensync02-plugin-synce-rra
Version:	0.22.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/synce/libopensync-plugin-synce-rra-%{version}.tar.gz
# Source0-md5:	415b63a93262fff48ce293440c2040be
Patch0:		%{name}-update.patch
URL:		http://www.synce.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libopensync02-devel >= 1:0.22
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	synce-core-lib-devel >= 0.16
BuildRequires:	synce-rra-devel >= 0.16
Requires:	synce-core >= 0.16
Requires:	libopensync02 >= 1:0.22
Obsoletes:	libopensync-plugin-synce-rra < 0.30
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSync 0.2x plugin for syncing pre-2005 Windows Mobile devices.

%description -l pl.UTF-8
Wtyczka OpenSync 0.2x do synchronizacji urządzeń Windows Mobile sprzed
wersji 2005.

%prep
%setup -q -n libopensync-plugin-synce-rra-%{version}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/synce_plugin.so
%{_datadir}/opensync/defaults/synce-plugin
