Name:           ros-melodic-dynamixel-sdk
Version:        3.7.0
Release:        0%{?dist}
Summary:        ROS dynamixel_sdk package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/dynamixel_sdk
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rospy

%description
This package is wrapping version of ROBOTIS Dynamxel SDK for ROS. The ROBOTIS
Dynamixel SDK, or SDK, is a software development library that provides Dynamixel
control functions for packet communication. The API is designed for Dynamixel
actuators and Dynamixel-based platforms.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Jan 04 2019 Pyo <pyo@robotis.com> - 3.7.0-0
- Autogenerated by Bloom

* Tue Jul 17 2018 Pyo <pyo@robotis.com> - 3.6.2-0
- Autogenerated by Bloom

