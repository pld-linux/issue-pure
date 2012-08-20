
%bcond_with	snap	# include shapshot information in version,
			# should be used only in official Th spanhots

%define snapshot	2012

# CPE_NAME = cpe:/ {part} : {vendor} : {product} : {version} : {update} : {edition} : {language}
# http://cpe.mitre.org/specification/
# http://csrc.nist.gov/publications/nistir/ir7695/NISTIR-7695-CPE-Naming.pdf

%if %{with snap}
%define	distname	Th/%{snapshot}
%define cpename		cpe:/o:pld-linux:pld:%{distversion}:%{snapshot}
%else
%define	distname	Th
%define cpename		cpe:/o:pld-linux:pld:%{distversion}
%endif
%define	distversion	3.0
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
Release:	1%{?with_snap:.%{snapshot}}
License:	GPL
Group:		Base
Provides:	issue
Provides:	issue-package
Obsoletes:	issue-package
Conflicts:	issue-alpha < 3.0
Conflicts:	issue-fancy < 3.0
Conflicts:	issue-logo < 3.0
Conflicts:	issue-nice < 3.0
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

# CPE_NAME = cpe:/ {part} : {vendor} : {product} : {version} : {update} : {edition} : {language}
# http://cpe.mitre.org/specification/
cat >$RPM_BUILD_ROOT%{_sysconfdir}/os-release <<EOF
NAME="PLD Linux"
VERSION="%{distversion} (%{distname})"
ID="pld"
VERSION_ID="%{distversion}"
PRETTY_NAME="PLD Linux %{distversion} (%{distname})"
ANSI_COLOR="0;32"
CPE_NAME="%{cpename}"
HOME_URL="http://www.pld-linux.org/"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/os-release
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
