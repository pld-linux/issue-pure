Summary:	PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(pl):	Wersja Linuksa PLD
Name:		issue-pure
Version:	2.0
Release:	7
License:	GPL
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	redhat-release
Obsoletes:	mandrake-release
Obsoletes:	issue
Obsoletes:	issue-alpha
Obsoletes:	issue-fancy
Obsoletes:	issue-logo
Obsoletes:	redhat-release
Obsoletes:	mandrake-release

%description
PLD Linux release file.

%description -l de
PLD Linux Release-Datei.

%description -l pl
Wersja Linuksa PLD.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
PLD Linux 1.99 (Ac) \m, \r
Welcome to \n
\u user(s)

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
PLD Linux 1.99 (Ac) %m, %r
Welcome to %h

EOF
echo "1.99 PLD Linux (Ac)" > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
