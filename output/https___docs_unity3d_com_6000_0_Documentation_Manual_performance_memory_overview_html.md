* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Memory in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
  * Memory in Unity introduction


[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
Memory in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html)
Managed memory
# Memory in Unity introduction
To ensure your application runs with no performance issues, it’s important to understand how Unity uses and allocates memory.
Unity uses the following memory management layers to handle memory in your application: 
  * **[Managed memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html#managed-memory)** : A controlled memory layer that uses a managed heap and a [garbage collector](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html) to automatically allocate and assign memory.
  * **[C# unmanaged memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html#unmanaged-memory)** : A layer of memory management that you can use with the `Unity.Collections` namespace, the [Collections package](https://docs.unity3d.com/Packages/com.unity.collections@latest), and via [`UnsafeUtility.Malloc`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html) and [`UnsafeUtility.Free`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html). This memory type is called unmanaged because it doesn’t use a garbage collector to track and manage when memory stops being used, but requires your code to explicitly manage and release the memory itself, by calling `Dispose` on the collection or `Free` on memory allocated with `UnsafeUtility.Malloc`.
  * **[Native memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html#native-memory)** : C++ memory that Unity uses to run the engine. It contains memory related to areas such as memory used for the assets in your project, and managers for Unity’s different native subsystems like the rendering or animation systems. In most situations, you can’t access this memory via your C# code, but because it’s usually the biggest chunk of your application’s memory footprint, it’s useful to be aware of it if you want to optimize your application’s memory usage.


## Managed memory
[Mono and IL2CPP’s](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html) scripting virtual machines (VM) implement the managed memory system, which is sometimes referred to as the scripting memory system. The VM offer a controlled memory environment divided into the following different types:
  * **The managed heap** : A section of memory that the VM automatically controls with a [garbage collector](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html).
  * **The scripting stack:** This is built up and unwound as your application steps into and out of any code scopes.
  * **Native VM memory:** Contains memory related to Unity’s scripting layer.


Using managed memory in Unity is the easiest way to manage the memory in your application, but it has some disadvantages. The garbage collector is convenient to use, but it’s also unpredictable in how it releases and allocates memory, which might lead to performance issues such as stuttering, which happens when the garbage collector has to stop to release and allocate memory. To work around this unpredictability, you can use the [C# unmanaged memory layer](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html#unmanaged-memory).
For more information on how managed memory works, refer to the section on [Managed memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html).
## C# unmanaged memory
The **C# unmanaged memory layer** allows you to access the native memory layer to fine-tune memory allocations, with the convenience of writing C# code.
You can use the `Unity.Collections` namespace (including [`NativeArray`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html)) in the Unity core API, the data structures in the [Unity Collections package](https://docs.unity3d.com/Packages/com.unity.collections@latest), and [`UnsafeUtility.Malloc`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Malloc.html) and [`UnsafeUtility.Free`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.UnsafeUtility.Free.html) to access C# unmanaged memory. 
If you use Unity’s [job system](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system.html), or [Burst](http://docs.unity3d.com/Packages/com.unity.burst@latest), you must use C# unmanaged memory. Additionally, to be able to use Burst you can only use the containers in the `Unity.Collections` namespace or types that fulfill the C# [unmanaged constraint](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/unmanaged-types).
Unity’s native code, and sometimes its native allocators, allocate the memory that’s accessible to C# via these APIs. Because of this, tools like the [Memory Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest) group C/# unmanaged memory in with the native memory.
## Native memory
The Unity engine’s internal C/C++ core has its own memory management system, called native memory. In most situations, you can’t directly access or modify this memory type.
Unity stores the **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in your project, assets, graphics APIs, graphics drivers, subsystems, **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) buffers, and allocations inside native memory. This means that you can indirectly access the native memory via Unity’s C# API and manipulate your application’s data in a safe way, and get the benefits of the native and efficient code that’s in the internal C/C++ core.
Most of the time, you won’t need to interact with Unity’s native memory, but you can check how it affects the performance of your application whenever you use the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler), through [Profiler markers](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker). You can also adjust the performance of your application by changing the settings on your assets and via configurable settings for Unity’s native memory allocators. For more information, refer to [Native memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html).
## Additional resources
  * [Managed memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html)
  * [Native memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory.html)
  * [C# unnmanaged memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-unmanaged-memory.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
Memory in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html)
Managed memory
