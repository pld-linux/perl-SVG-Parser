#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SVG
%define	pnam	Parser
Summary:	%{pdir}::%{pnam} - converts SVG XML documents into SVG objects
Summary(pl):	%{pdir}::%{pnam} - konwersja dokumentów SVG XML do obiektów SVG
Name:		perl-SVG-Parser
Version:	0.97
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48d7c76c30751d1c7487aba83c34d57f
BuildRequires:	perl-SVG >= 2.0
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-SVG >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVG::Parser is an XML parser that converts SVG XML documents into SVG
objects that may then be manipulated by the SVG module before being
regenerated into XML. It will work using any installed Expat or SAX
parser, and may be given preferred list of parsers to try; the first
to load successfully will be used.

%description -l pl
SVG::Parser to analizator XML konwertuj±cy dokumenty SVG XML na
obiekty SVG, którymi mo¿na manipulowaæ przy u¿yciu modu³u SVG przed
ponownym przekszta³ceniem na XML. Modu³ dzia³a z dowolnym
zainstalowanym analizatorem Expat lub SAX, mo¿na podaæ listê
preferowanych analizatorów - zostanie u¿yty pierwszy, który uda siê
za³adowaæ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/SVG/Parser.pm
%{perl_vendorlib}/SVG/Parser
%{_mandir}/man3/*
