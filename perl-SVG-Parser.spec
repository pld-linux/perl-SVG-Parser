#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SVG
%define	pnam	Parser
Summary:	%{pdir}::%{pnam} - converts SVG XML documents into SVG objects
Summary(pl):	%{pdir}::%{pnam} - konwertuje dokumenty SVG XML do obiektów SVG
Name:		perl-SVG-Parser
Version:	0.97
Release:	1
License:	GPLv1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48d7c76c30751d1c7487aba83c34d57f
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVG::Parser is an XML parser that converts SVG XML documents into SVG
objects that may then be manipulated by the SVG module before being
regenerated into XML. It will work using any installed Expat or SAX
parser, and may be given preferred list of parsers to try; the first
to load successfully will be used.

%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
# if module isn't noarch, use:
# %{__make} OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorlib}/*
%{_mandir}/man3/*
