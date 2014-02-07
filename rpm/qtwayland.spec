Name:       qt5-qtwayland-wayland_egl
Summary:    Qt Wayland compositor, wayland_egl variant
Version:    5.2.0
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
Source100:	precheckin.sh
Patch0:     0001_qtcompositor_private_wayland_headers.patch
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PlatformSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Declarative)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5DBus)

BuildRequires:  pkgconfig(wayland-client)
%if "%{name}" == "qt5-qtwayland-wayland_egl"
BuildRequires:  pkgconfig(wayland-egl)
%endif

BuildRequires:  libxkbcommon-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libffi-devel
BuildRequires:  fdupes

Requires:       xkeyboard-config

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt wayland compositor for wayland_egl

%package devel
Summary:        Qt Wayland compositor - development files
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description devel
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt wayland compositor development files for wayland_egl

%package examples
Summary:        Qt Wayland compositor - examples
Group:          Qt/Qt
Requires:       %{name} = %{version}-%{release}

%description examples
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt wayland compositor examples for wayland_egl

%prep
%setup -q -n %{name}-%{version}/upstream
#%patch0 -p 1
if [ -f /usr/share/wayland/wayland.xml ]
then
    cp /usr/share/wayland/wayland.xml src/3rdparty/protocol/wayland.xml
fi


%build
export QTDIR=/usr/share/qt5
export QT_WAYLAND_GL_CONFIG=wayland_egl
touch .git
%qmake5 "QT_BUILD_PARTS += examples" "CONFIG += wayland-compositor" 

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake_install
(cd %{buildroot}; find .)
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-hardware-integration.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-hardware-integration.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-server-buffer-extension.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-server-buffer-extension.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-sub-surface-extension.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-sub-surface-extension.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-hardware-integration-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-hardware-integration-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-server-buffer-extension-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-server-buffer-extension-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-wayland.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-wayland.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-output-extension.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-output-extension.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-surface-extension.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-surface-extension.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-touch-extension.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-touch-extension.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-qtkey-extension.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-qtkey-extension.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-input-method.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-input-method.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-text.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-text.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-windowmanager.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/qwayland-server-windowmanager.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-input-method-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-input-method-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-output-extension-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-output-extension-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-qtkey-extension-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-qtkey-extension-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-sub-surface-extension-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-sub-surface-extension-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-surface-extension-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-surface-extension-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-text-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-text-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-touch-extension-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-touch-extension-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-wayland-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-wayland-server-protocol.h
install -D -p -m 0644 include/QtCompositor/5.2.1/QtCompositor/private/wayland-windowmanager-server-protocol.h %{buildroot}/%{_includedir}/qt5/QtCompositor/5.2.1/QtCompositor/private/wayland-windowmanager-server-protocol.h
mkdir -p %{buildroot}/%{_bindir}
ln -s qtchooser %{buildroot}/%{_bindir}/qtwaylandscanner

# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt


%fdupes %{buildroot}/%{_includedir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libQt5Compositor.so.5*
%{_libdir}/libQt5WaylandClient.so.5*

%{_libdir}/qt5/plugins/platforms/libqwayland-generic.so
%{_libdir}/qt5/plugins/wayland-graphics-integration/client/libdrm-egl-server.so
%{_libdir}/qt5/plugins/wayland-graphics-integration/server/libdrm-egl-server.so

%if "%{name}" == "qt5-qtwayland-wayland_egl"
%{_libdir}/qt5/plugins/platforms/libqwayland-egl.so
%{_libdir}/qt5/plugins/wayland-graphics-integration/client/libwayland-egl.so
%{_libdir}/qt5/plugins/wayland-graphics-integration/server/libwayland-egl.so
%endif

%if "%{name}" == "qt5-qtwayland-xcomposite_egl"
%{_libdir}/qt5/plugins/platforms/libqwayland-xcomposite-egl.so
%{_libdir}/qt5/plugins/waylandcompositors/libxcomposite-egl.so
%endif

%if "%{name}" == "qt5-qtwayland-nogl"
%{_libdir}/qt5/plugins/platforms/libqwayland-nogl.so
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/qt5/*
%{_bindir}/qtwaylandscanner
%{_libdir}/cmake/Qt5Compositor/*.cmake
%{_libdir}/cmake/Qt5WaylandClient/*.cmake
%{_libdir}/cmake/Qt5Gui/Qt5Gui_.cmake
%{_libdir}/libQt5Compositor.so
%{_libdir}/libQt5Compositor.la
%{_libdir}/libQt5Compositor.prl
%{_libdir}/libQt5WaylandClient.so
%{_libdir}/libQt5WaylandClient.la
%{_libdir}/libQt5WaylandClient.prl
%{_libdir}/pkgconfig/Qt5Compositor.pc
%{_libdir}/pkgconfig/Qt5WaylandClient.pc
%{_libdir}/qt5/bin/qtwaylandscanner
%{_datadir}/qt5/mkspecs/modules/qt_lib_compositor*.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_waylandclient*.pri

%files examples
%defattr(-,root,root,-)
%{_libdir}/qt5/examples/qtwayland/

