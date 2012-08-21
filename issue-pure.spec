%define		distname	Ratman
%define		distversion	1.2
%define		distrelease	"%{distversion} Freddix (%{distname})"

Summary:	Freddix release file
Name:		issue-pure
Version:	%{distversion}
Release:	13
License:	GPL
Group:		Base
Provides:	issue
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freddix release file.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue <<EOF
Freddix %{distversion} (%{distname}) \m, \r
Welcome to \n
\u user(s)

EOF
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
Freddix %{distversion} (%{distname}) %m, %r
Welcome to %h

EOF
echo %{distrelease} > $RPM_BUILD_ROOT%{_sysconfdir}/freddix-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/freddix-release
%config(noreplace) %{_sysconfdir}/issue*

