Summary:	Cute little penguins that walk along the tops of your windows
Name:		xpenguins
Version:	2.1
Release:	1
License:	GPL
Group:		X11/Amusements
Group(de):	X11/Unterhaltung
Group(pl):	X11/Rozrywka
Source0:	http://xpenguins.seul.org/%{name}-%{version}.tar.gz
URL:		http://xpenguins.seul.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program animates a friendly family of penguins in your root
window. They drop in from the top of the screen, walk along the tops
of your windows, up the side of your windows, up the side of the
screen, and sometimes even levitate with their genetically-modified
go-go-gadget 'copter ability.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xpenguins
%{_datadir}/xpenguins
%{_mandir}/man1/*
