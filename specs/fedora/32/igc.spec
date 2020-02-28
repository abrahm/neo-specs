%global igc_commit ee341708a3d95738e942b6d3c5cd25b1f4b430f1
%global patch_version 3151

Name: intel-igc
Version: 1.0.3151
Release: 2%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: https://github.com/intel/intel-graphics-compiler/archive/%{igc_commit}/igc-%{version}.tar.gz
Patch0:  %{url}/commit/d9b4d395b4813e2c76c47e20446d03c3a68f99ff.patch

BuildRequires: cmake gcc-c++ make flex bison python3 llvm-devel clang-devel
BuildRequires: intel-opencl-clang-devel

%description
Intel(R) Graphics Compiler for OpenCL(TM).

%package       core
Summary:       Intel(R) Graphics Compiler Core

%description   core

%package       opencl
Summary:       Intel(R) Graphics Compiler Frontend
Requires:      %{name}-core = %{version}-%{release}
Requires:      intel-opencl-clang >= 9.0.9

%description   opencl

%package       opencl-devel
Summary:       Intel(R) Graphics Compiler development package
Requires:      %{name}-opencl = %{version}-%{release}

%description   opencl-devel

%prep
%autosetup -p1 -n intel-graphics-compiler-%{igc_commit}

%build
mkdir build
pushd build

cmake .. -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr  \
 -DIGC_PREFERRED_LLVM_VERSION=9.0.0 -DIGC_PACKAGE_RELEASE=%{patch_version}
%make_build
popd

%install
%make_install -C build
rm -fv %{buildroot}/usr/bin/GenX_IR

%files core
%{_libdir}/libiga64.so.1
%{_libdir}/libiga64.so.%{version}
%{_libdir}/libigc.so.1
%{_libdir}/libigc.so.%{version}
%{_bindir}/iga64

%files opencl
%{_libdir}/libigdfcl.so.1
%{_libdir}/libigdfcl.so.%{version}

%files opencl-devel
%{_includedir}/igc/*
%{_includedir}/iga/*
%{_includedir}/visa/*
%{_libdir}/libiga64.so
%{_libdir}/libigc.so
%{_libdir}/libigdfcl.so
%{_libdir}/pkgconfig/*

%doc

%changelog
* Tue Jan 28 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-2
- fix compilation under Fedora 32

* Fri Jan 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-1
- Update to 1.0.3151

* Fri Dec 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-1
- Update to 1.0.3041

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3032-1
- Update to 1.0.3032

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2990-2
- Correct commit ID for IGC 1.0.2990

* Fri Dec 06 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2990-1
- Update to 1.0.2990

* Fri Nov 29 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2934-1
- Update to 1.0.2934

* Wed Nov 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2878-1
- Update to 1.0.2878

* Thu Nov 14 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2805-1
- Update to 1.0.2805

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2714.1-1
- Update to 1.0.2714.1
