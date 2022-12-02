%global octpkg symbolic

Summary:	Symbolic toolbox for Octave
Name:		octave-%{octpkg}
Version:	3.0.1
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.2.0
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(mpmath)
BuildRequires:	python3dist(sympy)

Requires:	octave(api) = %{octave_api}
Requires:	python3dist(sympy)

Requires(post): octave
Requires(postun): octave

%description
The Octave-Forge Symbolic package adds symbolic calculation
features to GNU Octave.  These include common Computer Algebra System tools
such as algebraic operations, calculus, equation solving, Fourier and Laplace
transforms, variable precision arithmetic and other features.  Internally,
the package uses [SymPy](www.sympy.org), but no knowledge of Python is
required.  Compatibility with other symbolic toolboxes is intended.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

