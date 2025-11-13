# Damiao Setup

## Here the setup to follow

```
cd /home/unitree/H1_reply/library/Damiao_c/
mkdir build
cd build
cmake ..
make
cp dm.cxxxxxxxxxx.so /home/unitree/H1_reply/reply/src
```

## 1st issue

### Details

```
-- The C compiler identification is GNU 11.4.0
-- The CXX compiler identification is unknown
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
CMake Error at CMakeLists.txt:14 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.
```

### Solution
This error means that CMake cannot find a C++ compiler (like g++). Your C compiler (GCC) is found (gcc 11.4.0), but no C++ compiler is detected.

```
sudo apt update
sudo apt install build-essential
g++ --version
```

## 2nd Issue

### Details
```
-- The CXX compiler identification is GNU 11.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at CMakeLists.txt:19 (find_package):
  By not providing "Findpybind11.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "pybind11",
  but CMake did not find one.

  Could not find a package configuration file provided by "pybind11" with any
  of the following names:

    pybind11Config.cmake
    pybind11-config.cmake

  Add the installation prefix of "pybind11" to CMAKE_PREFIX_PATH or set
  "pybind11_DIR" to a directory containing one of the above files.  If
  "pybind11" provides a separate development package or SDK, be sure it has
  been installed.


-- Configuring incomplete, errors occurred!
```

### Solution
You're getting this error because your CMake project is trying to use pybind11, but CMake cannot locate its configuration files (pybind11Config.cmake or pybind11-config.cmake).

```
sudo apt update
sudo apt install pybind11-dev
```

## 3rd Issue

### Details
```
In file included from /usr/include/pybind11/pytypes.h:12, from /usr/include/pybind11/cast.h:13, from /usr/include/pybind11/attr.h:13, from /usr/include/pybind11/pybind11.h:13, from /home/gmaccagni/Workspace/area42-rdi-h1-ros2-controller/library/Damiao_c/python_bindings.cpp:1: /usr/include/pybind11/detail/common.h:215:10: fatal error: Python.h: No such file or directory 215 | #include <Python.h> | ^~~~~~~~~~ compilation terminated. make[2]: *** [CMakeFiles/dm.dir/build.make:76: CMakeFiles/dm.dir/python_bindings.cpp.o] Error 1 make[1]: *** [CMakeFiles/Makefile2:83: CMakeFiles/dm.dir/all] Error 2 make: *** [Makefile:91: all] Error 2
```

### Solution
You're very close — the issue now is that the compiler can't find Python.h, which means the Python development headers are missing.

sudo apt install python3-dev

## 4th Issue
- Copy the build dm.xxxx.so file into the same folder of the damiao.py script
- Rename the dm.xxxx.so file into dm.so
- run the script

## 5th Issue
### Details
```
CMake Error at /opt/ros/foxy/share/cmake/pybind11/pybind11Tools.cmake:8 (cmake_minimum_required):
  Compatibility with CMake < 3.5 has been removed from CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.

  Or, add -DCMAKE_POLICY_VERSION_MINIMUM=3.5 to try configuring anyway.
Call Stack (most recent call first):
  /opt/ros/foxy/share/cmake/pybind11/pybind11Config.cmake:100 (include)
  CMakeLists.txt:19 (find_package)
```

### Solution
```
cmake .. -DCMAKE_POLICY_VERSION_MINIMUM=3.5
```
