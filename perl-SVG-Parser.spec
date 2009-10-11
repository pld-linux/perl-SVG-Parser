#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SVG
%define		pnam	Parser
Summary:	SVG::Parser - converts SVG XML documents into SVG objects
Summary(pl.UTF-8):	SVG::Parser - konwersja dokumentów SVG XML do obiektów SVG
Name:		perl-SVG-Parser
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	58e1f95faede185edf0657abc443f668
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-SVG >= 2.0
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-SAX
%endif
Requires:	perl-SVG >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVG::Parser is an XML parser that converts SVG XML documents into SVG
objects that may then be manipulated by the SVG module before being
regenerated into XML. It will work using any installed Expat or SAX
parser, and may be given preferred list of parsers to try; the first
to load successfully will be used.

%description -l pl.UTF-8
SVG::Parser to analizator XML-a konwertujący dokumenty SVG XML na
obiekty SVG, którymi można manipulować przy użyciu modułu SVG przed
ponownym przekształceniem na XML. Moduł działa z dowolnym
zainstalowanym analizatorem Expat lub SAX, można podać listę
preferowanych analizatorów - zostanie użyty pierwszy, który uda się
załadować.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/SVG/Parser.pm
%{perl_vendorlib}/SVG/Parser
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
