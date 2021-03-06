%global spirv_llvm_translator_commit 4d43f68a30a510b4e7607351caab3df8e7426a6b

Name:           spirv-llvm-translator
Version:        10.0.12
Release:        1%{?dist}

Summary:        LLVM/SPIR-V Bi-Directional Translator
License:        NCSA
Source0:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_translator_commit}/spirv-llvm-translator.tar.gz
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  llvm-devel
Requires:       llvm-libs

%description
This package contains the LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation between LLVM IR and SPIR-V.

%package        devel
Summary:        Development files for spirv-llvm-translator
Requires:       %{name} = %{version}-%{release}

%description    devel
Development package for spirv-llvm-translator

%prep
%autosetup -n SPIRV-LLVM-Translator-%{spirv_llvm_translator_commit}

%build
mkdir build
cd build
%cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DCMAKE_BUILD_TYPE=Release
%make_build

%install
cd build
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libLLVMSPIRVLib.so.10

%files devel
%{_includedir}/LLVMSPIRVLib
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
* Wed Jun 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.12-1
- Update to 10.0.12-1

* Mon Jun 01 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.8-1
- Update to 10.0.8-1

* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.6-1
- Update to 10.0.6-1

* Mon Mar 02 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.4-1
- Update to 10.0.4-1

* Mon Feb 17 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.3-1
- Package version 10.0.3-1 on llvm 10
