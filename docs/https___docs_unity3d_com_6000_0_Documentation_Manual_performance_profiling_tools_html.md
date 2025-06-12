* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-profiling-tools.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * Profiling tools


[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-counters-reference.html)
Profiler counters reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
Platform development 
# Profiling tools
[Profiling](https://en.wikipedia.org/wiki/Profiling_\(computer_programming\)) your application is the best way to measure its performance. You can use a variety of profiling tools to understand where there might be any issues with elements of your application including memory usage, CPU performance, GPU performance, and your custom **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
## Unity’s profiling tools
Unity has several profiling tools that you can use to measure the performance of your application:
  * [Unity Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html): Measure the performance of the Unity Editor, your application in Play mode, or connect to a device running your application in development mode.
  * [Profiling Core package](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest): Provides APIs that you can use to add contextual information to Unity **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) captures
  * [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest): A tool that provides in-depth memory performance analysis
  * [Profile Analyzer](https://docs.unity3d.com/Packages/com.unity.performance.profile-analyzer@latest): Compare two profiling datasets together to analyze how your changes affect your application’s performance.
  * [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html): A tool that provides a way to measure the graphical performance of your application.


### Third party profiling tools
Alongside the Unity Profiler, use platform-specific profilers to ensure that your application runs as expected. The following list provides some examples of available profiling tools. You can also use Unity’s [low level native plug-in Profiler API](https://docs.unity3d.com/6000.0/Documentation/Manual/LowLevelNativePluginProfiler.html) to export profiling data to third-party profiling tools.
  * **Android:**
    * General Android GPU profiling: Google’s [Android GPU Inspector](https://developer.android.com/agi), if you have a device that supports it.
    * Arm CPU: [Streamline](https://developer.arm.com/tools-and-software/embedded/arm-development-studio/components/streamline-performance-analyzer) from Arm Mobile Studio.
    * Arm Mali GPU: Use the tools from [Arm Mobile Studio](https://developer.arm.com/solutions/hpc/hpc-software/categories/profiling-tools) for GPU and system profiling.
    * Imagination PowerVR GPU: [PVRTune](https://developer.imaginationtech.com/pvrtune/) for GPU profiling.
    * Qualcomm chips: [Snapdragon Profiler](https://developer.qualcomm.com/software/snapdragon-profiler) for GPU and system profiling.
  * **macOS and iOS** : 
    * [Xcode](https://developer.apple.com/xcode/)
    * [Xcode GPU Frame Capture](https://developer.apple.com/documentation/metal/frame_capture_debugging_tools/)
  * **PC:**
    * [AMD uProf](https://developer.amd.com/amd-uprof/)
    * [Intel GPA](https://www.intel.com/content/www/us/en/developer/tools/graphics-performance-analyzers/overview.html)
    * [NVIDIA Nsight Graphics](https://developer.nvidia.com/nsight-graphics)
    * [PIX on Windows](https://devblogs.microsoft.com/pix/download/)
    * [Superluminal](https://superluminal.eu/)
    * [VTune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html)
    * [Windows Performance Analysis Toolkit](https://docs.microsoft.com/en-us/windows-hardware/test/wpt/)
    * [Visual Studio graphics debugger](http://msdn.microsoft.com/en-us/library/hh315751.aspx)
    * [RenderDoc](https://github.com/baldurk/renderdoc)
    * [Radeon Developer Tool Suite](https://gpuopen.com/introducing-radeon-developer-tool-suite/)
    * [GPU Driver Instruments](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Instrument-GPUDriver.html)


These tools have the most utility on platforms that can use [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) to produce a C++ version of the project. These native-code versions provide transparent call stacks and high-resolution method timings that are unavailable when running under Mono.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-counters-reference.html)
Profiler counters reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
Platform development 
