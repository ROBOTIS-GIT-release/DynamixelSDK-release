%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-dynamixel-sdk
Version:        3.7.51
Release:        2%{?dist}%{?release_suffix}
Summary:        ROS dynamixel_sdk package

License:        Apache 2.0
URL:            http://wiki.ros.org/dynamixel_sdk
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospy
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rospy
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This package is wrapping version of ROBOTIS Dynamixel SDK for ROS. The ROBOTIS
Dynamixel SDK, or SDK, is a software development library that provides Dynamixel
control functions for packet communication. The API is designed for Dynamixel
actuators and Dynamixel-based platforms.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Apr 15 2021 Will Son <willson@robotis.com> - 3.7.51-2
- Autogenerated by Bloom

* Thu Apr 15 2021 Will Son <willson@robotis.com> - 3.7.51-1
- Autogenerated by Bloom

* Tue Jul 21 2020 Will Son <willson@robotis.com> - 3.7.31-1
- Autogenerated by Bloom

