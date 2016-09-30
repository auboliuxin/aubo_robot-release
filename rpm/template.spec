Name:           ros-indigo-aubo-kinematics
Version:        0.1.5
Release:        1%{?dist}
Summary:        ROS aubo_kinematics package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/aubo_kinematics
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-ros-planning
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf-conversions
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-ros-planning
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf-conversions

%description
Provides forward and inverse kinematics for Aubo Robots designs.

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

