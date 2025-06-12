* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Profile rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/profile-rendering.html)
  * [Frame Timing Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-landing.html)
  * Introduction to the Frame Timing Manager


[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-landing.html)
Frame Timing Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-enable.html)
Enable the FrameTimingManager
# Introduction to the Frame Timing Manager
The FrameTimingManager is an API that captures detailed timing data about performance during individual frames in an application. You can use this data to assess those frames to understand why your application doesn’t meet performance targets.
Use the FrameTimingManager if:
  * You need to debug at a frame-by-frame level.
  * You want to use the [Dynamic Resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution) feature.
  * You want to use the [Adaptive Performance](https://docs.unity.cn/Packages/com.unity.mobile.adaptiveperformance@0.1/manual/index.html) package.


Frame timings don’t replace data from the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler); after you profile your application at a high level, use the FrameTimingManager to investigate specific details. The FrameTimingManager decreases performance when it records data, so it can’t produce an accurate measurement of how your application performs.
## Platform support
**Property** | **Description** | **Supported** | **Comment**  
---|---|---|---  
**Windows** | DirectX 11 | Yes |   
| DirectX 12 | Yes |   
| OpenGL | Yes |   
| Vulkan | Yes |   
**macOS** | Metal | Yes | Might report a larger GPU time measurement than the total frame time due to the behavior of tile-based deferred rendering GPUs.  
**Linux** | OpenGL | Partial | Doesn’t support the GPU time measurement.  
| Vulkan | Yes |   
**Android** | OpenGL ES | Yes |   
| Vulkan | Yes |   
**iOS** | Metal | Yes | Might report a larger GPU time measurement than the total frame time due to the behavior of tile-based deferred rendering GPUs.  
**tvOS** | Metal | Yes | Might report a larger GPU time measurement than the total frame time due to the behavior of tile-based deferred rendering GPUs.  
****WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL)** | WebGL | Partial | Doesn’t support the GPU time measurement.  
## How the FrameTimingManager works
The FrameTimingManager provides results with a set delay of four frames. This is because timing results aren’t immediately available at the end of each frame, so the FrameTimingManager waits to get CPU and GPU data for the frame.
The delay doesn’t guarantee accurate timing results, because the GPU may not have any available resources to return the results, or might fail to return them correctly.
The FrameTimingManger changes how it produces a FrameTimeComplete timestamp under some circumstances:
  * If the GPU supports GPU timestamps, the GPU provides a FrameTimeComplete timestamp.
  * If the GPU doesn’t support GPU timestamps and returns GPU Time, the FrameTimingManager calculates a value for gpuFrameTime. The value is the sum of the reported GPU Time and the FirstSubmitTimestamp values.
  * If the GPU doesn’t support GPU timestamps and doesn’t return GPU Time,the FrameTimingManager sets the value of PresentTimestamp as the value of FrameTimeComplete.


## Additional resources
  * [Dynamic resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)
  * [FrameTiming API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTiming.html)
  * [FrameTimingManager API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FrameTimingManager.html)
  * [Profiler overview](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-landing.html)
Frame Timing Manager
[](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager-enable.html)
Enable the FrameTimingManager
