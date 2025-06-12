* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-optional-features.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx.html)
  * [Develop for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-develop.html)
  * Enable optional features for QNX


[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-touch-input.html)
Support touch input for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-troubleshooting.html)
Troubleshooting the QNX Player
# Enable optional features for QNX
You can launch the Unity QNX Player from the command line and pass arguments to change how the Player executes.
**Note** : All command line arguments have precedence over the settings configured in the Unity Editor.
Command | Details  
---|---  
`-platform-hmi-force-srgb-blit` | Configure the path to the `graphics.conf` to override [auto detection](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-autodetect-plugins.html).  
`-platform-hmi-quit-after-frame` | Enable logging. Refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html) > **Configuration** > **Logging**.  
`-platform-hmi-log-startup-times` | Enable logging. Refer to [**Player Settings**](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html) > **Configuration** > **Logging**.  
`-platform-hmi-force-vsync-count [C]` | The number of vertical syncs that are allowed to pass between each frame. Where, setting 0 disables **vsync** Vertical synchronization (VSync) is a display setting that caps a game’s frame rate to match the refresh rate of a monitor, to prevent image tearing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VSync) completely, –1 will use the value set in `QualitySettings`.  
## Startup time logging
Startup time logging is the length of time that it takes an application to start up. It’s often used as a critical metric for system safety and regulatory requirements.
Startup time logging in QNX devices include the duration or total time from the time the application launches. There are two types of Startup time logging:
  * **Real:** This is the actual wall or clock time, similar to a stopwatch used for calculating the time.
  * **User:** This is the time an application or one of its threads has spent on a CPU core. This can be higher than the Real time if multiple threads are busy when an application is starting up.


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
## Webcam
**Note:** Unity’s support for Webcam in QNX is currently experimental.
#### Prerequisites
  * QNX 7.1
  * `libcamapi` and its dependencies installed on the system (will be loaded dynamically)
  * **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) supporting `NV12` format


[Webcam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) usage is optional in QNX and it’s only supported on QNX 7.1. For more information, refer to the [Webcam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebCamTexture.html) documentation.
## Additional resources
  * [Autodetect plug-ins for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-autodetect-plugins.html)
  * [Support touch input for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-touch-input.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-touch-input.html)
Support touch input for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-troubleshooting.html)
Troubleshooting the QNX Player
