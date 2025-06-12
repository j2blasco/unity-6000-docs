* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-deploy.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx.html)
  * [Build and deliver for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-and-deliver.html)
  * Deploy a QNX project


[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-command-line.html)
Build for QNX from the command line
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
iOS
# Deploy a QNX project
Unity uses EGL handled by SDL2, which requires SDL to dynamically load `libEGL` and `libGLESv2` from the `graphics.conf file`. Unity does not parse the `conf` file but instead uses environment variables to locate these libraries.
## Setup
Use the following instructions to deploy QNX.
  1. Use one of the methods to locate the `graphics.conf` file that your screen loads:
     * Start `screen` with the `-c [path/to/graphics.conf]` option.
     * Let your `screen` automatically find the `graphics.conf` file in the folder inside `GRAPHICS_ROOT`.
  2. Make sure the folder that contains `graphics.conf` is part of `LD_LIBRARY_PATH`.
  3. Locate `begin egl display 1` in `graphics.conf`:
     * The line starting with `egl-dlls`should contain `libEGL[-_tag].so`, which is the required `libEGL` (for example, `libEGL_viv.so`).
     * The line starting with `glesv2-dlls` should contain `libGLESv2[-_tag]`, which is the `libGLESv2` (for example, `libGLESv2_viv.so`).
     * Both libraries should be in the same folder as `graphics.conf`.
     * Both library file names must be set up as environment variables.
  4. If you are using `ksh`, set the following environment variables.
```
SDL_VIDEO_EGL_DRIVER=[name_of_libEGL_in_graphics_conf].so (e.g., run export SDL_VIDEO_EGL_DRIVER=libEGL_viv.so)
SDL_VIDEO_GL_DRIVER=[name_of_libGLESv2_in_graphics_conf].so (e.g., run export SDL_VIDEO_GL_DRIVER=libGLESv2_viv.so)

```

  5. If you are on `sh`, you need to set the environment with the unity player start. For example, `run SDL_VIDEO_EGL_DRIVER=libEGL_viv.so SDL_VIDEO_GL_DRIVER=libGLESv2_viv.so ./qnxplayer`.
  6. Start the Unity Player.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-command-line.html)
Build for QNX from the command line
[](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html)
iOS
