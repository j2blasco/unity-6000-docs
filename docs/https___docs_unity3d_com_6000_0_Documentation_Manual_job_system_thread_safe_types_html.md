* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-thread-safe-types.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Code optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-optimization.html)
  * [Write multithreaded code with the job system](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system.html)
  * Thread safe types


[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-parallel-for-jobs.html)
Parallel jobs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-native-container.html)
Introduction to NativeContainer
# Thread safe types
The job system works best when you use it with the [Burst compiler](https://docs.unity3d.com/Packages/com.unity.burst@latest/). Because Burst doesn’t support managed objects, you need to use unmanaged types to access the data in jobs. You can do this with [blittable types](https://learn.microsoft.com/en-us/dotnet/framework/interop/blittable-and-non-blittable-types), or use Unity’s built-in [`NativeContainer`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.LowLevel.Unsafe.NativeContainerAttribute.html) objects.
**Topic** | **Description**  
---|---  
[Introduction to NativeContainer](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-native-container.html) | Understand Unity’s custom thread-safe type, `NativeContainer`.  
[Implement a custom NativeContainer](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-custom-nativecontainer.html) | Implement custom native containers.  
[Copying NativeContainer structures](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-copy-nativecontainer.html) | Copy and reference multiple native containers.  
[Custom NativeContainer example](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-custom-nativecontainer-example.html) | Use a real world custom NativeContainer example.  
## Additional resources
  * [Burst compiler](https://docs.unity3d.com/Packages/com.unity.burst@latest/)
  * [Collections](https://docs.unity3d.com/Packages/com.unity.collections@latest)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-parallel-for-jobs.html)
Parallel jobs
[](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-native-container.html)
Introduction to NativeContainer
