Summary:	Cute little penguins that walk along the tops of your windows
Summary(pl):	Ma³e pingwiny chodz±ce po okienkach
Name:		xpenguins
Version:	2.2
Release:	3
License:	GPL
Group:		X11/Amusements
Source0:	http://xpenguins.seul.org/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
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

%description -l pl
Ten program wy¶wietla animacjê przyjaznej rodziny pingwinów w g³ównym
oknie. Pingwiny spadaj± z góry ekranu, chodz± po górnych krawêdziach
okienek, czasem nawet lewituj± korzystaj±c z wszczepionego koptera.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README AUTHORS ChangeLog

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Amusements}
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Amusements

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xpenguins
%{_datadir}/xpenguins
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_applnkdir}/Amusements/*
