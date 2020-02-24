%global igc_commit b25b5ebe8b4dd0a36a776250dff7bd9a21b613c6
%global patch_version 3445

Name: intel-igc
Version: 1.0.3445
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/%{igc_commit}/igc-%{version}.tar.gz

BuildRequires: cmake clang gcc-c++ make procps flex bison python3 llvm-devel clang-devel pkg-config
BuildRequires: intel-opencl-clang-devel

%description
Intel(R) Graphics Compiler for OpenCL(TM).

%package       core
Summary:       Intel(R) Graphics Compiler Core

%description   core

%package       opencl
Summary:       Intel(R) Graphics Compiler Frontend
Requires:      %{name}-core = %{version}-%{release}
Requires:      intel-opencl-clang >= 9.0.13

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
cd build
%make_install
rm -fv $RPM_BUILD_ROOT/usr/bin/GenX_IR

%files core
%defattr(-,root,root)
/usr/lib64/libiga64.so.*
/usr/lib64/libigc.so.*
/usr/bin/iga64

%files opencl
%defattr(-,root,root)
/usr/lib64/libigdfcl.so.*

%files opencl-devel
%defattr(-,root,root)
/usr/include/igc/*
/usr/include/iga/*
/usr/include/visa/*
/usr/lib64/libiga64.so
/usr/lib64/libigc.so
/usr/lib64/libigdfcl.so
/usr/lib64/pkgconfig/*

%doc

%changelog
* Mon Feb 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3445-1
- Update to 1.0.3445

* Tue Feb 18 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3390-1
- Update to 1.0.3390

* Wed Feb 12 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3342-1
- Update to 1.0.3342

* Tue Feb 04 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3289-1
- Update to 1.0.3289

* Wed Jan 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-1
- Update to 1.0.3151

* Tue Dec 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-2
- Fix IGC commit

* Tue Dec 10 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-1
- Update to 1.0.3041

* Mon Dec 02 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2990-1
- Update to 1.0.2990

* Tue Nov 26 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2972-1
- Update to 1.0.2972

* Tue Nov 26 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2934-1
- Update to 1.0.2934

* Thu Nov 21 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2916-1
- Update to 1.0.2916

* Wed Nov 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2878-1
- Update to 1.0.2878

* Thu Nov 14 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2805-1
- Update to 1.0.2805

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2714.1-1
- Update to 1.0.2714.1

