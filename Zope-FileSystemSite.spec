%define		zope_subname	FileSystemSite
Summary:	Repackaging of the CMF's FileSystem Directory Views
Summary(pl):	Produkt zmieniaj±cy organizacje wy¶wietlania katalogów w CMF
Name:		Zope-%{zope_subname}
Version:	1.4.1
Release:	3
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://www.infrae.com/download/%{zope_subname}/%{version}/%{zope_subname}-%{version}.tgz
# Source0-md5:	5c3bf90234187f0d37ab3dcf2c4c4129
URL:		http://zope.org/Members/philikon/FileSystemSite/
%pyrequires_eq	python-modules
Requires:	Zope >= 2.7
Requires:	Zope-CMF >= 1:1.4.1

Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FileSystemSite repackaging of the CMF's FileSystem Directory Views

%description -l pl
FileSystemSite jest produktem Zope zmieniaj±cym sposób
wy¶wietlania katalogów w CMF

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {EditorUtils,ExampleSite,Extensions,dtml,images,templates,tests,*.py,version.txt,refresh.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc README.txt HISTORY.txt
%{_datadir}/%{name}
