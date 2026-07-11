%global tl_name flexipage
%global tl_revision 66614

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	Flexible page geometry with marginalia
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flexipage
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flexipage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flexipage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flexipage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows easy page layout if marginalia is required. Mid
document changes are possible such as: new marginal width, full width
text, and landscape text without marginal. Partners well with the
package sidenotesplus. The package also aids the layout for book
printing, allowing for binding corrections and adding page bleed, if
required.

