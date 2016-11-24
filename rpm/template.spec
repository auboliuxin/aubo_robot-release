Name:           ros-jade-aubo-gazebo
Version:        0.3.11
Release:        0%{?dist}
Summary:        ROS aubo_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/aubo_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-aubo-description
Requires:       ros-jade-effort-controllers
Requires:       ros-jade-gazebo-ros
Requires:       ros-jade-gazebo-ros-control
Requires:       ros-jade-gazebo-ros-pkgs
Requires:       ros-jade-joint-state-controller
Requires:       ros-jade-joint-trajectory-controller
Requires:       ros-jade-robot-state-publisher
Requires:       ros-jade-ros-controllers
BuildRequires:  ros-jade-catkin

%description
Gazebo wrapper for the Aubo robot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Nov 24 2016 Liuxin <liuxin@our-robotics.com> - 0.3.11-0
- Autogenerated by Bloom

* Thu Nov 24 2016 Liuxin <liuxin@our-robotics.com> - 0.3.10-1
- Autogenerated by Bloom

* Thu Nov 24 2016 Liuxin <liuxin@our-robotics.com> - 0.3.10-0
- Autogenerated by Bloom

