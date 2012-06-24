Summary:	A collection of programs to faciliate TCP programming in shell-scripts
Summary(pl):	Zestaw program�w u�atawiaj�cych programowanie TCP w skryptach pow�oki
Name:		tcputils
Version:	0.6.2
Release:	1
License:	Public Domain
Group:		Applications/Networking
Source0:	ftp://ftp.lysator.liu.se/pub/unix/tcputils/%{name}-%{version}.tar.gz
# Source0-md5:	daf5844e3b3f09b0171c426ac4c0419c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tcputils is a collection of programs to facilitate TCP programming in
shell-scripts. There is also a small library which makes it somewhat
easier to create TCP/IP sockets.

The programs included in this release are:
- mini-inetd - small TCP/IP connection dispatcher
- tcpbug - TCP/IP connection bugging device
- tcpconnect - general TCP/IP client
- tcplisten - general TCP/IP server
- getpeername - get name of connected TCP/IP peer

%description -l pl
tcputils to zestaw program�w u�atwiaj�cych programowanie TCP w
skryptach pow�oki. Dodatkowo do��czona jest ma�a biblioteka nieco
u�atwiaj�ca tworzenie gniazd TCP/IP.

Programy za��czone w tej wersji to:
- mini-inetd - ma�y program do przekazywania po��cze� TCP/IP
- tcpbug - narz�dzie do �ledzenia po��cze� TCP/IP
- tcpconnect - og�lny klient TCP/IP
- tcplisten - og�lny serwer TCP/IP
- getpeername - uzyskiwanie nazwy drugiej strony po��czenia TCP/IP

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	COPT="%{rpmcflags}" \
	NETLIBS=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
