* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-introduction.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Memory in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
  * [Native memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory.html)
  * Native memory introduction


[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory.html)
Native memory
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
Native memory allocators
# Native memory introduction
The Unity engine’s internal C/C++ core has its own memory management system, called native memory. In most situations, you can’t directly access or modify this memory type.
Native memory isn’t automatically managed or subject to [garbage collection](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html). This means it’s difficult to profile and handle in a way that doesn’t cause memory leaks.
Unity uses different memory allocator types, which all use different algorithms to organize memory. Unity’s memory manager uses these allocator types in different areas to organize the memory in your application effectively. 
To get greater control over how Unity allocates native memory, you can adjust the size of each allocation for each area. You can adjust the size of allocations either through the [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) window in the Unity Editor, or through the command line. For more information, refer to [Customizing allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html).
## Additional resources
  * [Memory in Unity introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html)
  * [Native allocators introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
  * [Customizing allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory.html)
Native memory
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
Native memory allocators
