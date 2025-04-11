%global octpkg symbolic

Summary:	Symbolic toolbox for Octave
Name:		octave-symbolic
Version:	3.2.1
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/symbolic/
Url:		https://github.com/cbm755/octsympy/
Source0:	https://github.com/cbm755/octsympy/releases/download/v%{version}/symbolic-%{version}.tar.gz

BuildRequires:  octave-devel >= 5.1.0
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(mpmath)
BuildRequires:	python%{pyver}dist(sympy)

Requires:	octave(api) = %{octave_api}
Requires:	python%{pyver}dist(sympy)

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Symbolic calculation features, including common Computer Algebra 
System tools such as algebraic operations, calculus, equation 
solving, Fourier and Laplace transforms, variable precision 
arithmetic and other features.

Internally, the package uses SymPy, but no knowledge of Python is
required.

Compatibility with other symbolic toolboxes is intended.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

