* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html

# Profiler
class in UnityEngine.Profiling
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Controls the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html) from script.
You can add custom Profiler sections in your scripts with [Profiler.BeginSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginSample.html) and [Profiler.EndSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EndSample.html).  
  
On standalone platforms, you can save all profiling information to a file, which allows you to inspect it later. To do this, you must specify a [Profiler.logFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-logFile.html) and set both [Profiler.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) and [Profiler.enableBinaryLog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableBinaryLog.html) to `true`.  
  
Because use of the Profiler negatively affects the performance of your app, most of the Profiler API functionality is only available when you enable the `Development Build`. Therefore, you must enable `Developer Build` if you want to use profiler API methods in your built app. Disabling `Development Build` makes your app run faster, but prevents you from using most of the Profiler API methods.  
  
The exception to this are the Profiler API methods relating to memory usage. Because Unity manages most of its system memory at run-time, it can provide that information with no performance penalty; therefore these methods are available even if you don't enable `Development Build`. This applies to all memory-related Profiler API methods except [Profiler.GetAllocatedMemoryForGraphicsDriver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetAllocatedMemoryForGraphicsDriver.html) and [Profiler.GetRuntimeMemorySizeLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetRuntimeMemorySizeLong.html), since they require extra profiling data only available in development builds.
### Static Properties
Property | Description  
---|---  
[areaCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-areaCount.html) | The number of Profiler Areas that you can profile.  
[enableAllocationCallstacks](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableAllocationCallstacks.html) | Enables the recording of callstacks for managed allocations.  
[enableBinaryLog](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enableBinaryLog.html) | Enables the logging of profiling data to a file.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) | Enables the Profiler.  
[logFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-logFile.html) | Specifies the file to use when writing profiling data.  
[maxUsedMemory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-maxUsedMemory.html) | Sets the maximum amount of memory that Profiler uses for buffering data. This property is expressed in bytes.  
[usedHeapSizeLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-usedHeapSizeLong.html) | Returns the number of bytes that Unity has allocated. This does not include bytes allocated by external libraries or drivers.  
### Static Methods
Method | Description  
---|---  
[AddFramesFromFile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.AddFramesFromFile.html) | Displays the recorded profile data in the profiler.  
[BeginSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginSample.html) | Begin profiling a piece of code with a custom label.  
[BeginThreadProfiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.BeginThreadProfiling.html) | Enables profiling on the thread from which you call this method.  
[EmitFrameMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitFrameMetaData.html) | Write metadata associated with the current frame to the Profiler stream.  
[EmitSessionMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitSessionMetaData.html) | Write metadata associated with the whole Profiler session capture.  
[EndSample](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EndSample.html) | Ends the current profiling sample.  
[EndThreadProfiling](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EndThreadProfiling.html) | Frees the internal resources used by the Profiler for the thread.  
[GetAllCategories](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetAllCategories.html) | Returns all ProfilerCategory registered in Profiler.  
[GetAllocatedMemoryForGraphicsDriver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetAllocatedMemoryForGraphicsDriver.html) | Returns the amount of allocated memory for the graphics driver, in bytes.Only available in development players and editor.  
[GetAreaEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetAreaEnabled.html) | Returns whether or not a given ProfilerArea is currently enabled.  
[GetCategoriesCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetCategoriesCount.html) | Returns number of ProfilerCategory registered in Profiler.  
[GetMonoHeapSizeLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetMonoHeapSizeLong.html) | Returns the size of the reserved space for managed-memory.  
[GetMonoUsedSizeLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetMonoUsedSizeLong.html) | Gets the allocated managed memory for live objects and non-collected objects.  
[GetRuntimeMemorySizeLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetRuntimeMemorySizeLong.html) | Gathers the native-memory used by a Unity object.  
[GetTempAllocatorSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTempAllocatorSize.html) | Returns the size of the temp allocator.  
[GetTotalAllocatedMemoryLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalAllocatedMemoryLong.html) | The total memory allocated by the internal allocators in Unity. Unity reserves large pools of memory from the system; this includes double the required memory for textures because Unity keeps a copy of each texture on both the CPU and GPU. This function returns the amount of used memory in those pools.  
[GetTotalFragmentationInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalFragmentationInfo.html) | Returns heap memory fragmentation information.  
[GetTotalReservedMemoryLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalReservedMemoryLong.html) | The total memory Unity has reserved.  
[GetTotalUnusedReservedMemoryLong](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.GetTotalUnusedReservedMemoryLong.html) | Unity allocates memory in pools for usage when unity needs to allocate memory. This function returns the amount of unused memory in these pools.  
[IsCategoryEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.IsCategoryEnabled.html) | Returns whether or not a given ProfilerCategory is currently enabled.  
[SetAreaEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.SetAreaEnabled.html) | Enable or disable a given ProfilerArea.  
[SetCategoryEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.SetCategoryEnabled.html) | Enable or disable a given ProfilerCategory.  
[SetTempAllocatorRequestedSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.SetTempAllocatorRequestedSize.html) | Sets the size of the temp allocator.  
* * *
