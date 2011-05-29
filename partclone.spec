Summary:	Utility to clone and restore partitions
Name:		partclone
Version:	0.2.24
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/partclone/%{name}-%{version}.tar.gz
# Source0-md5:	d2856820ed3f92e064fcbda3cd20f94e
URL:		http://partclone.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel
BuildRequires:	ntfsprogs-devel
BuildRequires:	pkgconfig >= 0.9.0
#BuildRequires:	progsreiserfs-devel
#BuildRequires:	reiser4progs-devel
#BuildRequires:	xfsprogs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Partclone is a project like the well-known backup utility "Partition
Image" a.k.a partimage.

Partclone provides utilities to back up used blocks and design for
higher compatibility of the file system using supported library like
e2fslibs.

%prep
%setup -q
sed -e 's|gcc -static|gcc|' -i configure.ac
#sed -e 's|libxfs.h|xfs.h|' -i configure.ac -i src/xfsclone.[ch]
sed -e 's|ncurses.h|ncurses/ncurses.h|' -i configure.ac -i src/{partclone,progress}.c

mv po/fr_FR.gmo po/fr.gmo
mv po/fr_FR.po po/fr.po
sed -i 's/fr_FR/fr/' po/LINGUAS

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
export LIBS=-ltinfo
%configure \
	--enable-extfs \
	--enable-hfsp \
	--enable-fat \
	--enable-ntfs \
	--enable-btrfs \
	--enable-ncursesw
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO src/gauge
%attr(755,root,root) %{_sbindir}/%{name}.*
%{_mandir}/man8/%{name}.*.8*
