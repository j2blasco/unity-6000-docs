* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-performance.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Web development](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-develop.html)
  * Web performance considerations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-enable.html)
Enable WebAssembly 2023
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-debugging.html)
Debug and troubleshoot Web builds
# Web performance considerations
In general, Web performance is close to native apps on the GPU, because the **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) graphics API uses your GPU for hardware-accelerated rendering. The only exception is the slight overhead for translating WebGL API calls and **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to your OS graphics API (typically DirectX on Windows, OpenGL on Mac, and Linux).
On the CPU, Emscripten translates your code into WebAssembly, the performance of which depends on the web browser you’re using.
Be aware of the following considerations:
  * Unity provides multithreading for C/C++ code, but not yet for C# code due to limitations of WebAssembly.
  * When using WebGL API for rendering, the CPU side dispatch of WebGL operations is slower than in native OpenGL. As a result, for best performance, the recommended best practice is to avoid large numbers of draw calls per frame, so make sure that both instancing and batching techniques are used in your shaders.
  * SIMD on the web is supported as part of WebAssembly 2023 **feature set** A feature set is a collection of related packages that you can use to achieve specific results in the Unity Editor. You can manage feature sets directly in Unity’s Package Manager. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/FeatureSets.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Featureset). Make sure to enable WebAssembly 2023 for best performance on newer browsers.


**Tip:** To learn how Unity distributes work to different threads on non-Web platforms, refer to the new timeline [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) in Unity.
## Web-specific settings which affect performance
To improve performance, set **Exception support** to **None** in the Player settings for Web by expanding **Other Settings > Stack Trace**.
## Collect performance data with the Profiler 
You can use the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-introduction.html) in the Web platform, but you can’t attach to a running player built with Web through the Unity Editor. This is because the WebGL API uses WebSockets for communication, which doesn’t allow for incoming connections on the browser side. To connect your application to the Profiler, refer to [Collect performance data on a target platform](https://docs.unity3d.com/6000.0/Documentation/Manual/profiling-target-device.html).
**Note** : Unity can’t profile draw calls for Web applications.
## Web content in background tabs
Your content continues to run when the canvas or browser window loses focus if one of the following options is enabled:
  * **Run in background** in the [Player settings for the Web platform](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html)
  * [Application.runInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-runInBackground.html)


However, some browsers can throttle content running in background tabs. If the tab with your content isn’t visible, your content only updates once per second in most browsers. Note that this causes [Time.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) to progress slower than usual with the default settings, as the default value of [Time.maximumDeltaTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-maximumDeltaTime.html) is lower than one second.
## Throttling Web performance
You might want to run your Web content at a lower frame rate in some situations to reduce CPU usage. For example, on other platforms, you can use the [Application.targetFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-targetFrameRate.html) API to do so.
When you don’t want to throttle performance, set this API to the default value of –1. This allows the browser to adjust the frame rate for the smoothest animation in the browser’s render loop, and might produce better results than Unity trying to do its own main loop timing to match a target frame rate.
**Note** : For security reasons, Unity can’t query a browser for its frame rate. As a result, Unity assumes a display rate of 60 **fps** See first person shooter, frames per second.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#FPS) for all browsers and bases `Application.targetFrameRate` on that value. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/wasm-2023-enable.html)
Enable WebAssembly 2023
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-debugging.html)
Debug and troubleshoot Web builds
