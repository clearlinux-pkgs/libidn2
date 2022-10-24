#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x51722B08FE4745A2 (simon@josefsson.org)
#
Name     : libidn2
Version  : 2.3.4
Release  : 12
URL      : https://mirrors.kernel.org/gnu/libidn/libidn2-2.3.4.tar.gz
Source0  : https://mirrors.kernel.org/gnu/libidn/libidn2-2.3.4.tar.gz
Source1  : https://mirrors.kernel.org/gnu/libidn/libidn2-2.3.4.tar.gz.sig
Summary  : Library implementing IDNA2008 and TR46
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0 Unicode-TOU
Requires: libidn2-bin = %{version}-%{release}
Requires: libidn2-info = %{version}-%{release}
Requires: libidn2-lib = %{version}-%{release}
Requires: libidn2-license = %{version}-%{release}
Requires: libidn2-locales = %{version}-%{release}
Requires: libidn2-man = %{version}-%{release}
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libunistring-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : valgrind

%description
Libidn2 is a free software implementation of IDNA2008, Punycode and
Unicode TR46.  Its purpose is to encode and decode internationalized
domain names.

%package bin
Summary: bin components for the libidn2 package.
Group: Binaries
Requires: libidn2-license = %{version}-%{release}

%description bin
bin components for the libidn2 package.


%package dev
Summary: dev components for the libidn2 package.
Group: Development
Requires: libidn2-lib = %{version}-%{release}
Requires: libidn2-bin = %{version}-%{release}
Provides: libidn2-devel = %{version}-%{release}
Requires: libidn2 = %{version}-%{release}

%description dev
dev components for the libidn2 package.


%package dev32
Summary: dev32 components for the libidn2 package.
Group: Default
Requires: libidn2-lib32 = %{version}-%{release}
Requires: libidn2-bin = %{version}-%{release}
Requires: libidn2-dev = %{version}-%{release}

%description dev32
dev32 components for the libidn2 package.


%package doc
Summary: doc components for the libidn2 package.
Group: Documentation
Requires: libidn2-man = %{version}-%{release}
Requires: libidn2-info = %{version}-%{release}

%description doc
doc components for the libidn2 package.


%package info
Summary: info components for the libidn2 package.
Group: Default

%description info
info components for the libidn2 package.


%package lib
Summary: lib components for the libidn2 package.
Group: Libraries
Requires: libidn2-license = %{version}-%{release}

%description lib
lib components for the libidn2 package.


%package lib32
Summary: lib32 components for the libidn2 package.
Group: Default
Requires: libidn2-license = %{version}-%{release}

%description lib32
lib32 components for the libidn2 package.


%package license
Summary: license components for the libidn2 package.
Group: Default

%description license
license components for the libidn2 package.


%package locales
Summary: locales components for the libidn2 package.
Group: Default

%description locales
locales components for the libidn2 package.


%package man
Summary: man components for the libidn2 package.
Group: Default

%description man
man components for the libidn2 package.


%prep
%setup -q -n libidn2-2.3.4
cd %{_builddir}/libidn2-2.3.4
pushd ..
cp -a libidn2-2.3.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666648583
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1666648583
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libidn2
cp %{_builddir}/libidn2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libidn2/f134eeebdc065e961a7935729cd6fd8fee3a50f2
cp %{_builddir}/libidn2-%{version}/COPYING.LESSERv3 %{buildroot}/usr/share/package-licenses/libidn2/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/libidn2-%{version}/COPYING.unicode %{buildroot}/usr/share/package-licenses/libidn2/33ad3570b2dc646e18e97171233bfceda6f7f088
cp %{_builddir}/libidn2-%{version}/COPYINGv2 %{buildroot}/usr/share/package-licenses/libidn2/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang libidn2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/idn2

%files dev
%defattr(-,root,root,-)
/usr/include/idn2.h
/usr/lib64/libidn2.so
/usr/lib64/pkgconfig/libidn2.pc
/usr/share/man/man3/idn2_check_version.3
/usr/share/man/man3/idn2_free.3
/usr/share/man/man3/idn2_lookup_u8.3
/usr/share/man/man3/idn2_lookup_ul.3
/usr/share/man/man3/idn2_register_u8.3
/usr/share/man/man3/idn2_register_ul.3
/usr/share/man/man3/idn2_strerror.3
/usr/share/man/man3/idn2_strerror_name.3
/usr/share/man/man3/idn2_to_ascii_4i.3
/usr/share/man/man3/idn2_to_ascii_4i2.3
/usr/share/man/man3/idn2_to_ascii_4z.3
/usr/share/man/man3/idn2_to_ascii_8z.3
/usr/share/man/man3/idn2_to_ascii_lz.3
/usr/share/man/man3/idn2_to_unicode_44i.3
/usr/share/man/man3/idn2_to_unicode_4z4z.3
/usr/share/man/man3/idn2_to_unicode_8z4z.3
/usr/share/man/man3/idn2_to_unicode_8z8z.3
/usr/share/man/man3/idn2_to_unicode_8zlz.3
/usr/share/man/man3/idn2_to_unicode_lzlz.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libidn2.so
/usr/lib32/pkgconfig/32libidn2.pc
/usr/lib32/pkgconfig/libidn2.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libidn2/api-index-0.1.html
/usr/share/gtk-doc/html/libidn2/api-index-2.0.0.html
/usr/share/gtk-doc/html/libidn2/api-index-2.1.1.html
/usr/share/gtk-doc/html/libidn2/api-index-deprecated.html
/usr/share/gtk-doc/html/libidn2/api-index-full.html
/usr/share/gtk-doc/html/libidn2/home.png
/usr/share/gtk-doc/html/libidn2/index.html
/usr/share/gtk-doc/html/libidn2/left-insensitive.png
/usr/share/gtk-doc/html/libidn2/left.png
/usr/share/gtk-doc/html/libidn2/libidn2-idn2.h.html
/usr/share/gtk-doc/html/libidn2/libidn2.devhelp2
/usr/share/gtk-doc/html/libidn2/libidn2.html
/usr/share/gtk-doc/html/libidn2/right-insensitive.png
/usr/share/gtk-doc/html/libidn2/right.png
/usr/share/gtk-doc/html/libidn2/style.css
/usr/share/gtk-doc/html/libidn2/up-insensitive.png
/usr/share/gtk-doc/html/libidn2/up.png

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libidn2.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libidn2.so.0
/usr/lib64/libidn2.so.0.3.8

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libidn2.so.0
/usr/lib32/libidn2.so.0.3.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libidn2/33ad3570b2dc646e18e97171233bfceda6f7f088
/usr/share/package-licenses/libidn2/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libidn2/f134eeebdc065e961a7935729cd6fd8fee3a50f2
/usr/share/package-licenses/libidn2/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/idn2.1

%files locales -f libidn2.lang
%defattr(-,root,root,-)

