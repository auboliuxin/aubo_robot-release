Name:           ros-indigo-aubo-trajectory-filters
Version:        0.3.6
Release:        1%{?dist}
Summary:        ROS aubo_trajectory_filters package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/industrial_trajectory_filters
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-ros-planning
Requires:       ros-indigo-orocos-kdl
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-ros-planning
BuildRequires:  ros-indigo-orocos-kdl
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-trajectory-msgs

%description
ROS Industrial libraries/plugins for filtering trajectories. This package is
part of the ROS Industrial program and contains libraries and moveit plugins for
filtering robot trajectories.

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
* Mon Nov 21 2016 Shaun Edwards <sedwards@swri.org> - 0.3.6-1
- Autogenerated by Bloom

* Thu Nov 17 2016 Shaun Edwards <sedwards@swri.org> - 0.3.6-0
- Autogenerated by Bloom

* Wed Nov 16 2016 Shaun Edwards <sedwards@swri.org> - 0.3.4-0
- Autogenerated by Bloom

