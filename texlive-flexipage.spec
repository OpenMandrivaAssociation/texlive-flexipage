Name:		texlive-flexipage
Version:	66614
Release:	1
Summary:	Flexible page geometry with marginalia
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flexipage
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flexipage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flexipage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flexipage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package flexipage allows easy page layout if marginalia is
required. Mid document changes are possible such as: new
marginal width, full width text, and landscape text without
marginal. Partners well with the package sidenotesplus. The
package also aids the layout for book printing, allowing for
binding corrections and adding page bleed, if required.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/flexipage
%{_texmfdistdir}/tex/latex/flexipage
%doc %{_texmfdistdir}/doc/latex/flexipage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
