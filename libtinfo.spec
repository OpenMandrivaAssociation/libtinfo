%define dont_symlinks_libs 1

%define major 6
%define libname %mklibname tinfo %{major}

Summary:	Virtual package for libtinfo library
Name:		libtinfo
Version:	6
Release:	1
License:	MIT
Group:		System/Libraries
Url:		http://www.gnu.org/software/ncurses/ncurses.html

%description
Virtual package for libtinfo library.

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Virtual package for libtinfo library
Group:		System/Libraries
Requires:	%{_lib}ncurses%{major}
%ifarch x86_64
Provides:	libtinfo.so.%{major}()(64bit) = %{EVRD}
%else
Provides:	libtinfo.so.%{major} = %{EVRD}
%endif

%description -n	%{libname}
Virtual package for libtinfo library.

%files -n %{libname}
%{_libdir}/libtinfo.so.%{major}

#----------------------------------------------------------------------------

%prep

%build

%install
mkdir -p %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s /%{_lib}/libncurses.so.%{major} libtinfo.so.%{major}
popd
