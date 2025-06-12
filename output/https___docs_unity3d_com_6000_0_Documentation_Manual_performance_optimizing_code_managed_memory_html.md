* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-optimizing-code-managed-memory.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Code optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-optimization.html)
  * Optimizing your code for managed memory


[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-custom-nativecontainer-example.html)
Custom NativeContainer example
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reference-types.html)
Reference type management
# Optimizing your code for managed memory
C#’s automatic memory management reduces the risk of memory leaks and other programming errors, in comparison to other programming languages like C++, where you must manually track and free all the memory you allocate.
Automatic memory management allows you to write code quickly and with few errors. However, this convenience might have performance implications. To optimize your code for performance, you must avoid situations where your application triggers the [garbage collector](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html) a lot. This section outlines some common issues and workflows that affect when your application triggers the garbage collector.
**Topic** | **Description**  
---|---  
**[Reference type management](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reference-types.html)** | Optimize how you use reference types in your code.  
**[Creating reusable code](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reusable-code.html)** | Reuse code to optimize the performance of your application.  
**[Optimizing arrays](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-optimizing-arrays.html)** | Optimize when and how you use arrays in your code.  
## Additional resources
  * [Managed memory introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory-introduction.html)
  * [Garbage collector introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-garbage-collector.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-custom-nativecontainer-example.html)
Custom NativeContainer example
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-reference-types.html)
Reference type management
