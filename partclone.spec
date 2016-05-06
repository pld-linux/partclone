Summary:	Utility to clone and restore partitions
Name:		partclone
Version:	0.2.88
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/partclone/%{name}-%{version}.tar.gz
# Source0-md5:	fdf2b91ae0470c4a4463edd97b39357a
URL:		http://partclone.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext-tools
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel
BuildRequires:	ntfs-3g-devel
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
%doc AUTHORS ChangeLog README.md TODO
%attr(755,root,root) %{_sbindir}/partclone.btrfs
%attr(755,root,root) %{_sbindir}/partclone.chkimg
%attr(755,root,root) %{_sbindir}/partclone.dd
%attr(755,root,root) %{_sbindir}/partclone.ext2
%attr(755,root,root) %{_sbindir}/partclone.ext3
%attr(755,root,root) %{_sbindir}/partclone.ext4
%attr(755,root,root) %{_sbindir}/partclone.ext4dev
%attr(755,root,root) %{_sbindir}/partclone.extfs
%attr(755,root,root) %{_sbindir}/partclone.fat
%attr(755,root,root) %{_sbindir}/partclone.fat12
%attr(755,root,root) %{_sbindir}/partclone.fat16
%attr(755,root,root) %{_sbindir}/partclone.fat32
%attr(755,root,root) %{_sbindir}/partclone.hfs+
%attr(755,root,root) %{_sbindir}/partclone.hfsp
%attr(755,root,root) %{_sbindir}/partclone.hfsplus
%attr(755,root,root) %{_sbindir}/partclone.imager
%attr(755,root,root) %{_sbindir}/partclone.info
%attr(755,root,root) %{_sbindir}/partclone.ntfs
%attr(755,root,root) %{_sbindir}/partclone.ntfsfixboot
%attr(755,root,root) %{_sbindir}/partclone.ntfsreloc
%attr(755,root,root) %{_sbindir}/partclone.restore
%attr(755,root,root) %{_sbindir}/partclone.vfat
%{_mandir}/man8/partclone.btrfs.8*
%{_mandir}/man8/partclone.chkimg.8*
%{_mandir}/man8/partclone.dd.8*
%{_mandir}/man8/partclone.ext2.8*
%{_mandir}/man8/partclone.ext3.8*
%{_mandir}/man8/partclone.ext4.8*
%{_mandir}/man8/partclone.ext4dev.8*
%{_mandir}/man8/partclone.extfs.8*
%{_mandir}/man8/partclone.fat12.8*
%{_mandir}/man8/partclone.fat16.8*
%{_mandir}/man8/partclone.fat32.8*
%{_mandir}/man8/partclone.hfs+.8*
%{_mandir}/man8/partclone.hfsplus.8*
%{_mandir}/man8/partclone.imager.8*
%{_mandir}/man8/partclone.info.8*
%{_mandir}/man8/partclone.ntfs.8*
%{_mandir}/man8/partclone.restore.8*
%{_mandir}/man8/partclone.vfat.8*
%{_mandir}/man8/partclone.8.*
%{_mandir}/man8/partclone.fat.8*
%{_mandir}/man8/partclone.hfsp.8*
%{_mandir}/man8/partclone.ntfsfixboot.8*
%{_mandir}/man8/partclone.ntfsreloc.8*
%{_datadir}/%{name}
