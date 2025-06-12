* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-optional-features.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [Embedded Linux](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux.html)
  * [Develop for Embedded Linux](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-develop.html)
  * Enable optional features for Embedded Linux


[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-autodetect-plugins.html)
Autodetect plug-ins for Embedded Linux
[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-troubleshooting.html)
Troubleshooting the Embedded Linux Unity Editor
# Enable optional features for Embedded Linux
You can enable the following optional features to improve the performance of your applications.
## Loading screen
When you start the Embedded Linux player, a separate loading screen appears (typically, within 200 ms on our reference systems) containing the 2D image configured in the [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) window. The initial **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) content is still available except that it loads behind the loading screen.
## Shader cache persistence for GLES3
Embedded Linux supports binary **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) caching on the device where the Unity Player is installed for better startup timings. The cache is created at runtime after you load a shader. As this cache is written to the temporary folder:`[TEMP]/[COMPANY_NAME]/[PROJECT_NAME]/UnityShaderCache/`, it can be wiped when you restart the system.
To use shader caching when your system restarts, copy the cache into the Player data by following these steps:
  1. Deploy the Unity Player to the target system.
  2. Run the application and make sure all shaders are touched.
  3. Copy all the files from `[TEMP]/[COMPANY_NAME]/[PROJECT_NAME]/UnityShaderCache/` to `[PATH_TO_PLAYER]/Data/UnityShaderCache/`.


**Note:**
  * You must refresh the cache every time the player is updated.
  * As the cache is device-specific, you must only share it between devices with the exact same hardware and software configuration.


## Pipeline cache persistence for Vulkan
Embedded Linux supports binary Vulkan pipeline caching on the device where the Unity Player is installed for better startup timings. The binary Vulkan pipeline cache is created at runtime when you use Vulkan pipelines. As this cache is written to the temporary `[TEMP]/[COMPANY_NAME]/[PROJECT_NAME]/vulkan_pso_cache.bin` file, you can wipe it when you restart the system.
To use pipeline caching when your system restarts, copy the cache into the Player data by following these steps:
  1. Deploy the Unity Player to the target system.
  2. Run the application and make sure all pipelines are being used.
  3. Copy `[TEMP]/[COMPANY_NAME]/[PROJECT_NAME]/vulkan_pso_cache.bin` file to `[PATH_TO_PLAYER]/Data`.


**Note:**
  * You must refresh the cache every time the player is updated.
  * As the cache is device specific, you must only share it between devices with the exact same hardware and software configuration.


## Startup time logging
Startup time logging is the length of time that it takes an application to start up. It’s often used as a critical metric for system safety and regulatory requirements.
Startup time logging in Embedded Linux include the duration or total time (in milliseconds) since the application is launched. There are two types of Startup time logging:
  * **Real:** This is the actual wall or clock time, similar to a stopwatch used for calculating the time.
  * **User:** This is the time an application or one of its threads has spent on a CPU core. This can be higher than the Real time if multiple threads are busy when an application is starting up.


To add a startup timing log from C#, use:
`HmiPlatform.LogStartupTiming("log tag");`
The results appear in the following `Player.log` line:
`[TIMING::STARTUP] log tag: Real: xxx ms | User: yyy ms`
It contains the **log tag** , **wall time (xxx)** , and **cpu time (yyy)** in milliseconds since the player’s start time.
You can guard the code using `#if UNITY_EMBEDDED_LINUX_API ... #endif`.
**Note:** Use the same terminology as the **Time** command to refer to wall vs. CPU time. For more information, refer to the main [Linux](https://man7.org/linux/man-pages/man7/time.7.html) manual.
### Example output
```
[TIMING::STARTUP] Initial probing done: Real: 19 ms | User: 11 ms
[TIMING::STARTUP] SDL Initialized: Real: 64 ms | User: 54 ms
[TIMING::STARTUP] Scripting runtime loaded: Real: 97 ms | User: 86 ms
[TIMING::STARTUP] Plugins loaded: Real: 97 ms | User: 87 ms
[TIMING::STARTUP] Engine initialized (nogfx): Real: 104 ms | User: 94 ms
[TIMING::STARTUP] Player Prefs loaded: Real: 104 ms | User: 94 ms
[TIMING::STARTUP] Screen initialized: Real: 139 ms | User: 112 ms
[TIMING::STARTUP] Engine initialized (gfx): Real: 187 ms | User: 161 ms
[TIMING::STARTUP] Gfx initialized: Real: 190 ms | User: 163 ms
[TIMING::STARTUP] Input initialized: Real: 190 ms | User: 163 ms
[TIMING::STARTUP] SPLASH - Begin: Real: 190 ms | User: 164 ms
[TIMING::STARTUP] SPLASH - Primary scene assets loaded (async): Real: 2197 ms | User: 1670 ms
[TIMING::STARTUP] SPLASH - All engine initial states established: Real: 2197 ms | User: 1670 ms

```

Output from a custom event using the Script API
`[TIMING::STARTUP] HELLO!!: Real: 2198 ms | User: 1671 ms`
When you specify `platform-hmi-quit-after-frame` command line argument, the log contains the following information up to frame number `X`, where `X` is the number of frames after which the application quits.
`[TIMING::STARTUP] Frame 1 rendered: Real: 2209 ms | User: 1687 ms`
`[TIMING::STARTUP] Frame 2 rendered: Real: 2210 ms | User: 1692 ms`
## EVDEV input handling with Wayland
To enable the `EVDEV SDL2` input driver while running in Wayland, start the player with the `-platform-embedded-linux-wayland-enable-evdev-input` argument. 
## Force to use Wayland
In a system where both X11 and Wayland windowing systems are available, you can force the Unity Player to use Wayland by setting the environment variable to `SDL_VIDEODRIVER=wayland`.
## Command line arguments
You can launch the Unity Embedded Linux Player from the command line and pass arguments to change how the Player executes.
**Note:** All command line arguments have precedence over the settings configured in the Unity Editor.
CLI argument | Description  
---|---  
`-platform-hmi-force-srgb-blit` | Change the forced `srgb-blit` setting. For more information, refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html) > **Rendering** > **Color Space**.  
`-platform-hmi-quit-after-frame` | Enable logging. Refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html) > **Configuration** > **Logging**.  
`-platform-hmi-log-startup-times` | Enable logging. Refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html) > **Configuration** > **Logging**.  
`-platform-hmi-single-gl-context` | Disable context sharing for GLES. **Note:** The arguments disable multi-display support.  
`-platform-hmi-cpu-configuration <configuration>` | Specify a CPU configuration for the player. This argument expects a string containing a combination of the letters H (high performance core), L (low performance core) and/or D (disable core). For example, `DHLL` for disabling the usage of the first core, tagging the second as High and the third and forth as Low performance on 4+ core CPU. Refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html) > **Configuration** > **CPU configuration**.  
`-platform-hmi-player-data-path` | Enter the directory path on the system where you want to save the `.config` and log files. Refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html) > **Configuration** > **Player Data path**.  
`-platform-hmi-force-vsync-count [C]` | The number of vertical syncs that are allowed to pass between each frame. Where, setting 0 disables **vsync** Vertical synchronization (VSync) is a display setting that caps a game’s frame rate to match the refresh rate of a monitor, to prevent image tearing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VSync) completely, –1 will use the value set in `QualitySettings`.  
`-platform-embedded-linux-enable-gamepadinput` | Change the game controller setting. Refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html) > **Configuration** > **Enable Game Controllers**.  
`-platform-embedded-linux-offscreen-video` | Configure player to use offscreen rendering driver from SDL2. This is helpful for simulations and creating a render server. All rendering is offscreen but will still be GPU-accelerated. **Note:** When using this feature, you can cap CPU/GPU usage by setting `Application.targetFrameRate`.  
`-platform-embedded-linux-wayland-enable-evdev-input` | Enable the EVDEV SDL2 input driver while running in Wayland. For more information, refer to [EVDEV input handling with Wayland](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-optional-features.html#EVDEV).  
## Additional resources
  * [Embedded Linux Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-player-settings.html)
  * [Linux manual pages](https://man7.org/linux/man-pages/man7/time.7.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-autodetect-plugins.html)
Autodetect plug-ins for Embedded Linux
[](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-troubleshooting.html)
Troubleshooting the Embedded Linux Unity Editor
