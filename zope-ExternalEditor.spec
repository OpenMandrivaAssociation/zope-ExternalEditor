%define Product ExternalEditor
%define product externaleditor
%define name    zope-%{Product}
%define version 0.9.3
%define release %mkrel 6

%define zope_minver     2.7
%define zope_home       %{_prefix}/lib/zope
%define software_home   %{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Zope External Editor
License:    GPL
Group:      System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}-src.tar.bz2
Source1:    ZopeEdit.ini
# give a system configuration file
Patch0:     zopeedit-etc.patch
Requires:   zope >= %{zope_minver}
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Do you like editing zope objects in text areas?

If not, this product is for you. The ExternalEditor is a Zope product and
configurable helper application that allows you to drop into your favorite
editor(s) directly from the ZMI to modify Zope objects. Its one of those 
"have your cake and eat it too" kind of things ;^).


%package -n zopeedit
Summary:        Zope ExternalEditor helper application
Group:          System/Servers
License:        GPL
Requires:       tkinter

%description -n zopeedit
Do you like editing zope objects in text areas?

If not, this product is for you. The ExternalEditor is a Zope product and
configurable helper application that allows you to drop into your favorite
editor(s) directly from the ZMI to modify Zope objects. Its one of those 
"have your cake and eat it too" kind of things ;^).


%prep
%setup -c -q
%patch0 -p0

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__mkdir_p} %{buildroot}/%{_bindir}
%{__mkdir_p} %{buildroot}%{_sysconfdir}

%{__cp} -a * %{buildroot}%{software_home}/Products/
mv %{buildroot}%{software_home}/Products/ExternalEditor/zopeedit.py %{buildroot}/%{_bindir}
cp %{SOURCE1} %{buildroot}%{_sysconfdir}


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
        service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*

%files -n zopeedit
%defattr(-,root,root)
%{_bindir}/zopeedit.py
%config(noreplace) %{_sysconfdir}/ZopeEdit.ini
