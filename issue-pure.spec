Summary:	PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(pl):	Wersja Linuksa PLD
Name:		issue-pure
Version:	2.0
Release:	2
License:	free
Group:		Base
Group(de):	Gründsätzlich
Group(es):	Base
Group(pl):	Podstawowe
Group(pt_BR):	Base
BuildArch:	noarch
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue
Obsoletes:	issue-logo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file.

%description -l de
PLD Linux Release-Datei.

%description -l pl
Wersja Linuksa PLD.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
c
PLD Linux 1.0 (Ra) \m, \r
Welcome to \n
\u user(s)

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
PLD Linux 1.0 (Ra) %m, %r
Welcome to %h
 
EOF
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
