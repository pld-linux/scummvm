%define snap	20020116
Summary:	SCUMM graphic adventure game interpreter
Summary(pl):	Interpreter przygodówek opartych na SCUMM
Name:		scummvm
Version:	0.1.0
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications/Games
#Source0:	http://scummvm.sourceforge.net/daily/%{name}-%{snap}.tar.bz2
Source0:	%{name}-%{snap}.tar.bz2
Patch0:		%{name}-timidity.patch
BuildRequires:	SDL-devel >= 1.2.2
Requires:	SDL >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ScummVM is an interpreter that will play graphic adventure games
written for LucasArts' SCUMM virtual machine. It uses the SDL library
for outputting graphics.

%description -l pl
ScummVM jest interpreterem, który pozwala graæ w przygodówki napisane
dla wirtualnej maszyny SCUMM stworzonej przez LucasArts. U¿ywa SDL do
wy¶wietlania grafiki.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6}
install scummvm $RPM_BUILD_ROOT%{_bindir}
install scummvm.6 $RPM_BUILD_ROOT%{_mandir}/man6

gzip -9nf readme.txt whatsnew.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%doc *.gz
