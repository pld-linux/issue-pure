%define	distversion	%(. /etc/os-release 2>/dev/null ; echo $VERSION)

Summary:	PLD Linux prelogin message and identification file
Summary(de.UTF-8):	PLD Linux Systemidentifikationsdatei
Summary(es.UTF-8):	Mensaje pre-entrada y fichero de identificación del sistema de PLD Linux
Summary(fr.UTF-8):	Message d'identification du système avant la connexion de PLD Linux
Summary(it.UTF-8):	Messaggio di identificazione prima del login di PLD Linux
Summary(ja.UTF-8):	PLD Linux の ログイン前に表示されるメッセージとシステム情報のファイル
Summary(pl.UTF-8):	Plik identyfikujący system PLD Linux, wyświetlany przed zalogowaniem
Summary(pt.UTF-8):	Mensagem anteriores ao login e arquivo de identificaçăo do PLD Linux
Summary(ru.UTF-8):	Файл идентификации, содержащий сообщение, выдаваемым перед приглашением в систему PLD Linux
Name:		issue-pure
Version:	3.0
Release:	2
License:	GPL
Group:		Base
BuildRequires:	pld-release >= 3.0
%requires_eq	pld-release
Provides:	issue
Conflicts:	issue-alpha < 3.0-1
Conflicts:	issue-fancy < 3.0-1
Conflicts:	issue-logo < 3.0-1
Conflicts:	issue-nice < 3.0-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux prelogin message and identification file.

%description -l de.UTF-8
PLD Linux Systemidentifikationsdatei.

%description -l es.UTF-8
Mensaje pre-entrada y fichero de identificación del sistema de
PLD Linux.

%description -l fr.UTF-8
Message d'identification du système avant la connexion de PLD Linux.

%description -l it.UTF-8
Messaggio di identificazione prima del login di PLD Linux.

%description -l ja.UTF-8
PLD Linux の ログイン前に表示されるメッセージとシステム情報のファイル。

%description -l pl.UTF-8
Plik identyfikujący system PLD Linux, wyświetlany przed zalogowaniem.

%description -l pt.UTF-8
Mensagem anteriores ao login e arquivo de identificaçăo do PLD Linux.

%description -l ru.UTF-8
Файл идентификации, содержащий сообщение, выдаваемым перед
приглашением в систему PLD Linux.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
PLD Linux %{distversion} \m, \r
Welcome to \n
\u user(s)

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
PLD Linux %{distversion} %m, %r
Welcome to %h

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/issue*
