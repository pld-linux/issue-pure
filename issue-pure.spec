Summary:	    PLD Linux release file
Summary(de):	PLD Linux Release-Datei
Summary(pl):	Wersja Linuxa PLD
Name:		      issue-pure
Version:	    2.0
Release:	    1
Copyright:	  free
Group:		    Base
Group(pl):	  Podstawowe
Buildarch:	  noarch
Obsoletes:	  redhat-release
Obsoletes:	  mandrake-release
BuildRoot:	  %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file.

%description -l de
PLD Linux Release-Datei.

%description
Wersja Linuxa PLD.


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
c
PLD GNU/Linux 1.0 (Ra) \m, \r
Welcome to \n
\u user(s)

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
PLD GNU/Linux 1.0 (Ra) %m, %r
Welcome to %h
 
EOF
echo "1.0 PLD Linux (Ra)" > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
