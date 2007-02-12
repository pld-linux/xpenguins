Summary:	Cute little penguins that walk along the tops of your windows
Summary(pl.UTF-8):	Małe pingwiny chodzące po okienkach
Summary(pt_BR.UTF-8):	Pinguins que andam sobre as bordas de suas janelas
Name:		xpenguins
Version:	2.2
Release:	7
License:	GPL
Group:		X11/Amusements
Source0:	http://xpenguins.seul.org/%{name}-%{version}.tar.gz
# Source0-md5:	2ccf555d55f9b0377017322b3b3d27a4
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://xpenguins.seul.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program animates a friendly family of penguins in your root
window. They drop in from the top of the screen, walk along the tops
of your windows, up the side of your windows, up the side of the
screen, and sometimes even levitate with their genetically-modified
go-go-gadget 'copter ability.

%description -l pl.UTF-8
Ten program wyświetla animację przyjaznej rodziny pingwinów w głównym
oknie. Pingwiny spadają z góry ekranu, chodzą po górnych krawędziach
okienek, czasem nawet lewitują korzystając z wszczepionego koptera.

%description -l pt_BR.UTF-8
Este programa mostra uma família de pinguins em sua janela principal.
Eles aparecem pelo topo da tela, caminham até o topo de suas janelas e
por outras áreas.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/xpenguins
%{_datadir}/xpenguins
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
