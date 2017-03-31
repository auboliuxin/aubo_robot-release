Name:           ros-indigo-aubo-trajectory
Version:        0.3.15
Release:        0%{?dist}
Summary:        ROS aubo_trajectory package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/aubo_trajectory
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-aubo-msgs
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-interactive-markers
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-fake-controller-manager
Requires:       ros-indigo-moveit-ros-perception
Requires:       ros-indigo-moveit-ros-planning-interface
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-aubo-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-interactive-markers
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-ros-perception
BuildRequires:  ros-indigo-moveit-ros-planning-interface
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs

%description
The aubo_trajectory package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 31 2017 liuxin <liuxin@our-robotics.com> - 0.3.15-0
- Autogenerated by Bloom

* Thu Nov 24 2016 liuxin <liuxin@our-robotics.com> - 0.3.12-1
- Autogenerated by Bloom

* Thu Nov 24 2016 liuxin <liuxin@our-robotics.com> - 0.3.12-0
- Autogenerated by Bloom

* Mon Nov 21 2016 liuxin <liuxin@our-robotics.com> - 0.3.7-0
- Autogenerated by Bloom

* Mon Nov 21 2016 liuxin <liuxin@our-robotics.com> - 0.3.6-1
- Autogenerated by Bloom

* Thu Nov 17 2016 liuxin <liuxin@our-robotics.com> - 0.3.6-0
- Autogenerated by Bloom

* Wed Nov 16 2016 liuxin <liuxin@our-robotics.com> - 0.3.4-0
- Autogenerated by Bloom

* Wed Nov 16 2016 liuxin <liuxin@our-robotics.com> - 0.3.2-0
- Autogenerated by Bloom

* Tue Nov 15 2016 liuxin <liuxin@our-robotics.com> - 0.2.3-0
- Autogenerated by Bloom

* Tue Oct 11 2016 liuxin <liuxin@our-robotics.com> - 0.2.1-0
- Autogenerated by Bloom

* Sun Oct 09 2016 liuxin <liuxin@our-robotics.com> - 0.1.6-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.5-2
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.5-1
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.5-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.4-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.3-0
- Autogenerated by Bloom

* Fri Sep 30 2016 liuxin <liuxin@our-robotics.com> - 0.1.2-0
- Autogenerated by Bloom

* Thu Sep 29 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-6
- Autogenerated by Bloom

* Thu Sep 29 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-5
- Autogenerated by Bloom

* Tue Sep 27 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-4
- Autogenerated by Bloom

* Fri Sep 23 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-3
- Autogenerated by Bloom

* Fri Sep 23 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-2
- Autogenerated by Bloom

* Fri Sep 23 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-1
- Autogenerated by Bloom

* Tue Sep 20 2016 liuxin <liuxin@our-robotics.com> - 0.1.1-0
- Autogenerated by Bloom

