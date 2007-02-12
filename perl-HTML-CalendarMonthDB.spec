#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	CalendarMonthDB
Summary:	HTML::CalendarMonthDB - generating HTML calendar with persistant data
Summary(pl.UTF-8):   HTML::CalendarMonthDB - generowanie kalendarza w HTML z trwałymi danymi
Name:		perl-HTML-CalendarMonthDB
Version:	1.01
Release:	1
License:	free (see README)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b9297144606d7ba3ba6eea93eda3c9ec
%if %{with tests}
BuildRequires:	perl-DBI
BuildRequires:	perl-Date-Calc
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::CalendarMonthDB is a Perl module for generating, manipulating,
and printing a HTML calendar grid for a specified month. It is
intended as a faster and easier-to-use alternative to
HTML::CalendarMonth. It is based on HTML::CalendarMonthSimple, but can
store persistant data into a database, as well as adding features like
per-event links, descriptions, and times.

%description -l pl.UTF-8
HTML::CalendarMonthDB to moduł Perla do generowania, obrabiania i
drukowania tabelek HTML z kalendarzem dla określonego miesiąca. Ma być
szybszą i łatwiejszą w użyciu alternatywą dla HTML::CalendarMonth.
Jest oparty na HTML::CalendarMonthSimple, ale może przechowywać trwałe
dane w bazie, a także dodawać do zdarzeń rzeczy takie jak odnośniki,
opisy i czasy do zdarzeń.

%prep
%setup -q -n %{pdir}-%{pnam}-1.0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install cgi/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc IMPORTANT-README INSTALL README
%{perl_vendorlib}/HTML/CalendarMonthDB.pm
%attr(755,root,root) %{perl_vendorlib}/HTML/setup_calendar.pl
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.tmpl
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.cgi
