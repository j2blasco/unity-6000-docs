* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-tls-stack-allocator.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Memory in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
  * [Native memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory.html)
  * [Native memory allocator examples](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-examples.html)
  * Thread Local Storage stack allocator example


[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-bucket-allocator.html)
Bucket allocator example
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-threadsafe-linear-allocator.html)
Thread-safe linear allocator example
# Thread Local Storage stack allocator example
## Prerequisites
The examples use the memory usage reports that Unity writes to the log when you close the Player or Unity Editor. To create these reports, use the `-log-memory-performance-stats` command line argument. To find your project’s log files, follow the instructions on [the log files page](https://docs.unity3d.com/6000.0/Documentation/Manual/log-files.html).
## TLS stack allocator usage reports
If a thread’s stack allocator is full, allocations fall back to the [threadsafe linear allocator](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-threadsafe-linear-allocator.html). A few overflow allocations are fine: 1 to 10 in a frame, or a few hundred during load. However, if the numbers grow every frame, you can increase the block sizes. 
![Main Thread Block Size custom value in the Fast Per Thread Temporary Allocators](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Per_Thread.png) Main Thread Block Size custom value in the Fast Per Thread Temporary Allocators
To increase the block size, set the value in the Editor, or use the command line arguments. For more information, refer to [Customizing native memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html).
The information in the usage report can help you select a block size that’s appropriate for your application. For example, in the following main thread usage report, the load peaks at 2.7 MB, but the remaining frames are under 64 KB. You can reduce the block size from 4 MB to 64 KB and allow the loading frame to spill over the allocations:
```
[ALLOC_TEMP_TLS] TLS Allocator
  StackAllocators :
    [ALLOC_TEMP_MAIN]
      Peak usage frame count: [16.0 KB-32.0 KB]: 802 frames, [32.0 KB-64.0 KB]: 424 frames, [2.0 MB-4.0 MB]: 1 frames
      Initial Block Size 4.0 MB
      Current Block Size 4.0 MB
      Peak Allocated Bytes 2.7 MB
      Overflow Count 0
    [ALLOC_TEMP_Job.Worker 18]

```

In the following example, the worker thread isn’t used for large temporary allocations. To save memory, you can reduce the worker’s block size to 32 KB. This is useful on a multi-core machine, where each worker thread has its own stack:
```
[ALLOC_TEMP_Job.Worker 14]
      Initial Block Size 256.0 KB
      Current Block Size 256.0 KB
      Peak Allocated Bytes 18.6 KB
      Overflow Count 0

```

## Additional resources
  * [Native memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
  * [Native memory allocator examples](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-bucket-allocator.html)
Bucket allocator example
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-threadsafe-linear-allocator.html)
Thread-safe linear allocator example
