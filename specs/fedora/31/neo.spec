Name: intel-opencl
Version: 20.08.15750
Release: 1%{?dist}
Summary: Intel(R) Graphics Compute Runtime for OpenCL(TM)

License: MIT
URL: https://github.com/intel/compute-runtime
Source0: %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

BuildRequires: make libva-devel gcc-c++ cmake

BuildRequires: intel-gmmlib-devel = 19.4.1
BuildRequires: intel-igc-opencl-devel = 1.0.3390

Requires: intel-gmmlib = 19.4.1
Requires: intel-igc-opencl = 1.0.3390

%description
Intel(R) Graphics Compute Runtime for OpenCL(TM).

%prep
%autosetup -n compute-runtime-%{version}

%build
mkdir build
cd build
%cmake -DCMAKE_BUILD_TYPE=Release -DNEO_DRIVER_VERSION=%{version} -DSKIP_UNIT_TESTS=1 ..
%make_build

%install
%make_install -C build
chmod +x %{buildroot}/%{_libdir}/intel-opencl/libigdrcl.so

%files
%{_libdir}/intel-opencl/libigdrcl.so
%{_bindir}/ocloc

%config(noreplace)
%{_sysconfdir}/OpenCL/vendors/intel.icd

%doc

%changelog
* Fri Feb 28 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.08.15750-1
- Update to 20.08.15750

* Fri Feb 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.07.15711-1
- Update to 20.07.15711

* Fri Feb 14 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.06.15619-1
- Update to 20.06.15619

* Fri Feb 07 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.05.15524-1
- Update to 20.05.15524

* Fri Jan 31 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.04.15428-1
- Update to 20.04.15428

* Fri Jan 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.03.15346-1
- Update to 20.03.15346

* Fri Jan 17 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.02.15268-1
- Update to 20.02.15268

* Fri Jan 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.01.15264-1
- Update to 20.01.15264

* Fri Jan 03 2020 Jacek Danecki <jacek.danecki@intel.com> - 19.52.15209-1
- Update to 19.52.15209

* Fri Dec 27 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.51.15145-1
- Update to 19.51.15145

* Fri Dec 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.50.15079-1
- Update to 19.50.15079
- Updated IGC

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.49.15055-1
- Update to 19.49.15055
- Updated IGC

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.48.14977-2
- Rebuild with IGC 1.0.2990-2

* Fri Dec 06 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.48.14977-1
- Update to 19.48.14977
- Updated IGC

* Fri Nov 29 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.47.14903-1
- Update to 19.47.14903
- Updated IGC

* Fri Nov 22 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.46.14807-1
- Update to 19.46.14807
- Updated IGC

* Tue Nov 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.45.14764-1
- Update to 19.45.14764

* Wed Nov 13 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.44.14658-1
- Update to 19.44.14658

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.43.14583-1
- Update to 19.43.14583

* Thu Oct 24 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.41.14441-1
- Update to 19.41.14441
