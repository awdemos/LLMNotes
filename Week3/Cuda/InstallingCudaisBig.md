```bash
└─> sudo apt install cuda-toolkit
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  alsa-topology-conf alsa-ucm-conf at-spi2-core ca-certificates-java cuda-cccl-12-6 cuda-command-line-tools-12-6 cuda-compiler-12-6 cuda-crt-12-6 cuda-cudart-12-6
  cuda-cudart-dev-12-6 cuda-cuobjdump-12-6 cuda-cupti-12-6 cuda-cupti-dev-12-6 cuda-cuxxfilt-12-6 cuda-documentation-12-6 cuda-driver-dev-12-6 cuda-gdb-12-6 cuda-libraries-12-6
  cuda-libraries-dev-12-6 cuda-nsight-12-6 cuda-nsight-compute-12-6 cuda-nsight-systems-12-6 cuda-nvcc-12-6 cuda-nvdisasm-12-6 cuda-nvml-dev-12-6 cuda-nvprof-12-6
  cuda-nvprune-12-6 cuda-nvrtc-12-6 cuda-nvrtc-dev-12-6 cuda-nvtx-12-6 cuda-nvvm-12-6 cuda-nvvp-12-6 cuda-opencl-12-6 cuda-opencl-dev-12-6 cuda-profiler-api-12-6
  cuda-sanitizer-12-6 cuda-toolkit-12-6 cuda-toolkit-12-6-config-common cuda-toolkit-12-config-common cuda-toolkit-config-common cuda-tools-12-6 cuda-visual-tools-12-6
  dbus-user-session dconf-gsettings-backend dconf-service default-jre default-jre-headless fonts-dejavu-extra gds-tools-12-6 gir1.2-glib-2.0 gsettings-desktop-schemas java-common
  libargon2-1 libasound2 libasound2-data libatk-bridge2.0-0 libatk-wrapper-java libatk-wrapper-java-jni libatspi2.0-0 libcryptsetup12 libcublas-12-6 libcublas-dev-12-6
  libcufft-12-6 libcufft-dev-12-6 libcufile-12-6 libcufile-dev-12-6 libcurand-12-6 libcurand-dev-12-6 libcusolver-12-6 libcusolver-dev-12-6 libcusparse-12-6 libcusparse-dev-12-6
  libdconf1 libfontenc1 libgif7 libgirepository-1.0-1 libice6 libkmod2 liblcms2-2 libnpp-12-6 libnpp-dev-12-6 libnspr4 libnss-systemd libnss3 libnuma1 libnvfatbin-12-6
  libnvfatbin-dev-12-6 libnvjitlink-12-6 libnvjitlink-dev-12-6 libnvjpeg-12-6 libnvjpeg-dev-12-6 libopengl0 libpam-systemd libpcsclite1 libsm6 libxaw7 libxcb-cursor0
  libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 libxcb-util1 libxcb-xinerama0 libxcb-xinput0 libxcb-xkb1 libxft2 libxkbcommon-x11-0 libxkbcommon0
  libxkbfile1 libxmu6 libxt6 libxtst6 libxv1 libxxf86dga1 networkd-dispatcher nsight-compute-2024.3.2 nsight-systems-2024.5.1 openjdk-11-jre openjdk-11-jre-headless python3-dbus
  python3-gi session-migration systemd systemd-sysv systemd-timesyncd x11-common x11-utils xkb-data
Suggested packages:
  libasound2-plugins alsa-utils liblcms2-utils pcscd iw | wireless-tools fonts-ipafont-gothic fonts-ipafont-mincho fonts-wqy-microhei | fonts-wqy-zenhei fonts-indic
  python-dbus-doc systemd-container libtss2-esys-3.0.2-0 libtss2-mu0 libtss2-rc0 policykit-1 mesa-utils
The following NEW packages will be installed:
  alsa-topology-conf alsa-ucm-conf at-spi2-core ca-certificates-java cuda-cccl-12-6 cuda-command-line-tools-12-6 cuda-compiler-12-6 cuda-crt-12-6 cuda-cudart-12-6
  cuda-cudart-dev-12-6 cuda-cuobjdump-12-6 cuda-cupti-12-6 cuda-cupti-dev-12-6 cuda-cuxxfilt-12-6 cuda-documentation-12-6 cuda-driver-dev-12-6 cuda-gdb-12-6 cuda-libraries-12-6
  cuda-libraries-dev-12-6 cuda-nsight-12-6 cuda-nsight-compute-12-6 cuda-nsight-systems-12-6 cuda-nvcc-12-6 cuda-nvdisasm-12-6 cuda-nvml-dev-12-6 cuda-nvprof-12-6
  cuda-nvprune-12-6 cuda-nvrtc-12-6 cuda-nvrtc-dev-12-6 cuda-nvtx-12-6 cuda-nvvm-12-6 cuda-nvvp-12-6 cuda-opencl-12-6 cuda-opencl-dev-12-6 cuda-profiler-api-12-6
  cuda-sanitizer-12-6 cuda-toolkit cuda-toolkit-12-6 cuda-toolkit-12-6-config-common cuda-toolkit-12-config-common cuda-toolkit-config-common cuda-tools-12-6
  cuda-visual-tools-12-6 dbus-user-session dconf-gsettings-backend dconf-service default-jre default-jre-headless fonts-dejavu-extra gds-tools-12-6 gir1.2-glib-2.0
  gsettings-desktop-schemas java-common libargon2-1 libasound2 libasound2-data libatk-bridge2.0-0 libatk-wrapper-java libatk-wrapper-java-jni libatspi2.0-0 libcryptsetup12
  libcublas-12-6 libcublas-dev-12-6 libcufft-12-6 libcufft-dev-12-6 libcufile-12-6 libcufile-dev-12-6 libcurand-12-6 libcurand-dev-12-6 libcusolver-12-6 libcusolver-dev-12-6
  libcusparse-12-6 libcusparse-dev-12-6 libdconf1 libfontenc1 libgif7 libgirepository-1.0-1 libice6 libkmod2 liblcms2-2 libnpp-12-6 libnpp-dev-12-6 libnspr4 libnss-systemd
  libnss3 libnuma1 libnvfatbin-12-6 libnvfatbin-dev-12-6 libnvjitlink-12-6 libnvjitlink-dev-12-6 libnvjpeg-12-6 libnvjpeg-dev-12-6 libopengl0 libpam-systemd libpcsclite1 libsm6
  libxaw7 libxcb-cursor0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 libxcb-util1 libxcb-xinerama0 libxcb-xinput0 libxcb-xkb1 libxft2
  libxkbcommon-x11-0 libxkbcommon0 libxkbfile1 libxmu6 libxt6 libxtst6 libxv1 libxxf86dga1 networkd-dispatcher nsight-compute-2024.3.2 nsight-systems-2024.5.1 openjdk-11-jre
  openjdk-11-jre-headless python3-dbus python3-gi session-migration systemd systemd-sysv systemd-timesyncd x11-common x11-utils xkb-data
0 upgraded, 130 newly installed, 0 to remove and 0 not upgraded.
Need to get 3,028 MB of archives.
After this operation, 6,798 MB of additional disk space will be used.
Do you want to continue? [Y/n] 

```
