* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Memory in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
  * [Native memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory.html)
  * Customizing native memory allocators


[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
Native memory allocators
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-reference.html)
Native memory allocators reference
# Customizing native memory allocators
To customize allocator settings you can either edit the configurable values through the [Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html#use-the-editor) or supply them as [command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html#use-command-line-arguments).
## Using the Editor
  1. Open the **Project Settings** window (**Edit** > **Project Settings**).
  2. Select the **Memory Settings** panel.
  3. Select the lock icon next to the value you want to edit.

![Project Settings > Memory Settings, showing a selection of Player memory settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/memory-native-settings.png) Project Settings > Memory Settings, showing a selection of Player memory settings
For more information on how the values affect each allocator, refer to [Native memory allocator examples](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-examples.html).
## Using command line arguments
You can use [command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html) to set the size of each allocator. To find the name of the allocator parameters you want to change, check the list of allocator settings the Editor and players print when they start up.
For example, to change the block size of the main heap allocators, use the following: 
`-memorysetup-main-allocator-block-size=<new_value>`
For a full list of command line arguments, refer to [Native memory allocators reference](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-reference.html).
## Measuring the performance of changes
To ensure your settings improve performance, [profile your application](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-collect-data.html) before and after making changes. For more information, refer to the [Profiler overview page](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html).
You can also use the [Profiler Analyzer](https://docs.unity3d.com/Packages/com.unity.performance.profile-analyzer@latest) package to measure changes. The **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) Analyzer enables you to compare multiple frames, and two different Profiler captures to each other. Comparing two captures is useful for highlighting differences in allocator performance between two different runs with different settings. 
You can also check the memory usage reports, which are available in the log when you close the Player or Editor. To find your log files, follow the instructions on the [log files page](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html).
## Storing and reading the settings
Unity stores allocator settings in `MemorySettings.asset` and these settings are applied during the build process. This means new settings take effect at every build.
In the Editor, these settings are stored in the `ProjectSettings` folder and are updated every time Unity imports or changes `MemorySettings.asset`. New values for the Editor only take effect on the next Editor startup.
## Additional resources
  * [Native memory allocator examples](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-examples.html)
  * [Native memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
  * [Native memory allocators reference](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-reference.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
Native memory allocators
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-reference.html)
Native memory allocators reference
