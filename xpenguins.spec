Summary:	Cute little penguins that walk along the tops of your windows.
Name:		xpenguins
Version:	1.1
Release:	2
License:	GPL
Group:		X11/Amusements
Group(pl):	X11/Rozrywka	
Source0:	http://www.met.rdg.ac.uk/~swrhgnrj/xpenguins/%{name}-%{version}-%{release}.tar.gz
URL:		http://www.met.rdg.ac.uk/~swrhgnrj/xpenguins/
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This program animates a friendly family of penguins in your root window.
They drop in from the top of the screen, walk along the tops of your
windows, up the side of your windows, up the side of the screen, and
sometimes even levitate with their genetically-modified go-go-gadget
'copter ability.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

install -s xpenguins $RPM_BUILD_ROOT%{_bindir}/xpenguins
install xpenguins.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README AUTHORS \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xpenguins
%{_mandir}/man1/*
