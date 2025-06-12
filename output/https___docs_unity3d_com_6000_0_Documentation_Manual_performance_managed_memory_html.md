* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Memory in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
  * Managed memory


[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html)
Memory in Unity introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory-introduction.html)
Managed memory introduction
# Managed memory
Unity’s managed memory system is a C# scripting environment based on the Mono or **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) Virtual Machines (VMs). The benefit of the managed memory system is that it manages the release of memory, so you don’t need to manually request the release of memory through your code. It makes use of a garbage collector to automatically free memory allocations.
**Topic** | **Description**  
---|---  
**[Managed memory introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory-introduction.html)** | Automatically manage the release and allocation of memory in your application.  
**[Garbage collector introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html)** | Reclaim unused memory in your application.  
**[Garbage collection modes](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-incremental-garbage-collection.html)** | Overview of the different ways that the garbage collector runs.  
**[Configuring garbage collection](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-disabling-garbage-collection.html)** | Set up the garbage collector in your project.  
**[Tracking garbage collection allocations](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-track-garbage-collection.html)** | Monitor when your application performed garbage collection.  
## Additional resources
  * [Memory in Unity introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html)
  * [Memory performance data](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-memory.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory-overview.html)
Memory in Unity introduction
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory-introduction.html)
Managed memory introduction
