Summary:	PLD Linux release file
Summary(cs):	Soubor s èíslem verze systému PLD Linux
Summary(da):	PLD Linux release fil
Summary(de):	PLD Linux Release-Datei
Summary(es):	El fichero con la versión de PLD Linux
Summary(fr):	Fichier de version de PLD Linux
Summary(id):	File rilis PLD Linux
Summary(is):	Útgáfuskráin fyrir PLD Linux
Summary(it):	File della release di PLD Linux
Summary(ja):	PLD Linux ¥ê¥ê¡¼¥¹¥Õ¥¡¥¤¥ë
Summary(ko):	PLD Linux ¹èÆ÷ ÆÄÀÏ
Summary(no):	PLD Linux release fil
Summary(pl):	Wersja Linuksa PLD
Summary(pt):	O ficheiro de versão final do PLD Linux
Summary(ru):	æÁÊÌ ÒÅÌÉÚÁ PLD Linux
Summary(sk):	Súbor oznaèujúci verziu PLD Linux
Summary(sl):	Datoteka s podatki o izdaji PLD Linuxa
Summary(sv):	PLD Linux versionsfil
Summary(tr):	PLD Linux sürüm dosyasý
Summary(zh_CN):	PLD Linux °æ±¾ÎÄ¼þ¡£
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

%description -l cs
Soubor s èíslem verze systému PLD Linux.

%description -l da
PLD Linux release fil.

%description -l de
PLD Linux Release-Datei.

%description -l es
El fichero con la versión de PLD Linux.

%description -l fr
Fichier de version de PLD Linux.

%description -l id
File rilis PLD Linux.

%description -l is
Útgáfuskráin fyrir PLD Linux.

%description -l it
File della release di PLD Linux.

%description -l ja
PLD Linux ¥ê¥ê¡¼¥¹¥Õ¥¡¥¤¥ë

%description -l ko
PLD Linux ¹èÆ÷ ÆÄÀÏ.

%description -l no
PLD Linux release fil.

%description -l pl
Wersja Linuksa PLD.

%description -l pt
O ficheiro de versão final do PLD Linux.

%description -l ru
æÁÊÌ ÒÅÌÉÚÁ PLD Linux.

%description -l sk
Súbor oznaèujúci verziu PLD Linux.

%description -l sl
Datoteka s podatki o izdaji PLD Linuxa.

%description -l sv
PLD Linux versionsfil.

%description -l tr
PLD Linux sürüm dosyasý.

%description -l zh_CN
PLD Linux °æ±¾ÎÄ¼þ¡£

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
