
%define	distname	Ac
%define	distversion	2.00
%define	distrelease	"%{distversion} PLD Linux (%{distname})"

Summary:	PLD Linux release file
Summary(cs.UTF-8):	Soubor s číslem verze systému PLD Linux
Summary(da.UTF-8):	PLD Linux release fil
Summary(de.UTF-8):	PLD Linux Release-Datei
Summary(es.UTF-8):	El fichero con la versión de PLD Linux
Summary(fr.UTF-8):	Fichier de version de PLD Linux
Summary(id.UTF-8):	File rilis PLD Linux
Summary(is.UTF-8):	Útgáfuskráin fyrir PLD Linux
Summary(it.UTF-8):	File della release di PLD Linux
Summary(ja.UTF-8):	PLD Linux リリースファイル
Summary(ko.UTF-8):	PLD Linux 배포 파일
Summary(nb.UTF-8):	PLD Linux release fil
Summary(pl.UTF-8):	Wersja Linuksa PLD
Summary(pt.UTF-8):	O ficheiro de versão final do PLD Linux
Summary(ru.UTF-8):	Файл релиза PLD Linux
Summary(sk.UTF-8):	Súbor označujúci verziu PLD Linux
Summary(sl.UTF-8):	Datoteka s podatki o izdaji PLD Linuxa
Summary(sv.UTF-8):	PLD Linux versionsfil
Summary(tr.UTF-8):	PLD Linux sürüm dosyası
Summary(zh_CN.UTF-8):	PLD Linux 版本文件。
Name:		issue-pure
Version:	%{distversion}
Release:	3
License:	GPL
Group:		Base
Provides:	issue
Obsoletes:	issue
Obsoletes:	issue-alpha
Obsoletes:	issue-fancy
Obsoletes:	issue-logo
Obsoletes:	issue-nice
Obsoletes:	mandrake-release
Obsoletes:	redhat-release
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file.

%description -l cs.UTF-8
Soubor s číslem verze systému PLD Linux.

%description -l da.UTF-8
PLD Linux release fil.

%description -l de.UTF-8
PLD Linux Release-Datei.

%description -l es.UTF-8
El fichero con la versión de PLD Linux.

%description -l fr.UTF-8
Fichier de version de PLD Linux.

%description -l id.UTF-8
File rilis PLD Linux.

%description -l is.UTF-8
Útgáfuskráin fyrir PLD Linux.

%description -l it.UTF-8
File della release di PLD Linux.

%description -l ja.UTF-8
PLD Linux リリースファイル

%description -l ko.UTF-8
PLD Linux 배포 파일.

%description -l nb.UTF-8
PLD Linux release fil.

%description -l pl.UTF-8
Wersja Linuksa PLD.

%description -l pt.UTF-8
O ficheiro de versão final do PLD Linux.

%description -l ru.UTF-8
Файл релиза PLD Linux.

%description -l sk.UTF-8
Súbor označujúci verziu PLD Linux.

%description -l sl.UTF-8
Datoteka s podatki o izdaji PLD Linuxa.

%description -l sv.UTF-8
PLD Linux versionsfil.

%description -l tr.UTF-8
PLD Linux sürüm dosyası.

%description -l zh_CN.UTF-8
PLD Linux 版本文件。

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
PLD Linux %{distversion} (%{distname}) \m, \r
Welcome to \n
\u user(s)

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
PLD Linux %{distversion} (%{distname}) %m, %r
Welcome to %h

EOF
echo %{distrelease} > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
