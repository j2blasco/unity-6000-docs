* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-reference.html

  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/analysis.html)
  * [Memory in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-memory.html)
  * [Native memory](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory.html)
  * Native memory allocators reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html)
Customizing native memory allocators
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-examples.html)
Native memory allocator examples
# Native memory allocators reference
You can control how native memory is allocated through using command line arguments, or using the settings in the Unity Editor (**Edit > Project Settings > Memory Settings**). For information on how to customize native memory allocators, refer to [Customizing native memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html).
![Project Settings > Memory Settings, showing a selection of Player memory settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/memory-native-settings.png) Project Settings > Memory Settings, showing a selection of Player memory settings
The following table contains information about each allocator setting, plus their [command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html), and their default values:
## Main Allocators
These allocators are the ones that Unity uses for most allocations.
### Main Allocator
The primary allocator Unity uses for most allocations. It has the following settings:
**Setting** | **Description** | **Command line argument** | **Default value**  
---|---|---|---  
**Main Thread Block Size** | Block size of dedicated main thread allocator. | `memorysetup-main-allocator-block-size` |  `16777216` bytes  
**Shared Thread Block Size** | Block size of shared thread allocator. | `memorysetup-thread-allocator-block-size` |  `16777216` bytes  
### Gfx Allocator
The allocator Unity uses for CPU allocations related to the Gfx system. It has the following settings:
**Setting** | **Description** | **Command line argument** | **Default value**  
---|---|---|---  
**Main Thread Block Size** | Block size of the dedicated main thread Gfx allocator. | `memorysetup-gfx-main-allocator-block-size` |  `16777216` bytes  
**Shared Thread Block Size** | Block size of the shared thread Gfx allocator. | `memorysetup-gfx-thread-allocator-block-size` |  `16777216` bytes  
### Other Allocators
Allocations used for type trees and the file cache. It has the following settings:
**Setting** | **Description** | **Command line argument** | **Default value**  
---|---|---|---  
**File Cache Block Size** | The file cache has its own allocator to avoid fragmentation. This is its block size. | `memorysetup-cache-allocator-block-size` |  `4194304` bytes  
**Type Tree Block Size** | The type trees have their own allocator to avoid fragmentation due to many small allocations. This is its block size. | `memorysetup-typetree-allocator-block-size` |  `2097152` bytes  
### Shared Bucket Allocator
The bucket allocator shared between the main allocators. It has the following settings:
**Setting** | **Description** | **Command line argument** | **Default value**  
---|---|---|---  
**Bucket Allocator Granularity** | Step size for buckets in the shared allocator. | `memorysetup-bucket-allocator-granularity` |  `16` bytes  
**Bucket Allocator BucketCount** | Number of bucket sizes. | `memorysetup-bucket-allocator-bucket-count` | `8`  
**Bucket Allocator Block Size** | Size of memory blocks used for buckets. | `memorysetup-bucket-allocator-block-size` | Editor: `8388608` bytes  
Player: `4194304` bytes  
**Bucket Allocator Block Count** | Maximum number of blocks to be allocated. | `memorysetup-bucket-allocator-block-count` | Editor: `8`  
Player: `1`  
## Fast Per Thread Temporary Allocators
The [Thread Local Storage (TLS) allocator](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html#tls) that handles very short-lived allocations.
**Allocator** | **Description** | **Command line argument** |  **Default value** (in bytes)  
---|---|---|---  
**Main Thread Block Size** | The initial size for the main thread stack. | `memorysetup-temp-allocator-size-main` | Editor: `16777216`  
Player: `4194304`  
**Job Worker Block Size** | Size of each job worker in the Unity job system. | `memorysetup-temp-allocator-size-job-worker` | `E262144`  
**Background Job Worker Block Size** | Size for each background worker. | `memorysetup-temp-allocator-size-background-worker` | `32768`  
**Preload Block Size** | The preload manager stack size. | `memorysetup-temp-allocator-size-preload-manager` | Editor: `33554432`  
Player: `262144`  
Audio Worker Block Size | Each audio worker thread’s stack size. | `memorysetup-temp-allocator-size-audio-worker` | `65536`  
**Cloud Worker Block Size** | Cloud worker threads stack size. | `memorysetup-temp-allocator-size-cloud-worker` | `32768`  
**Gfx Thread Blocksize** | The main render threads stack size. | `memorysetup-temp-allocator-size-gfx` | `262144`  
**GI Baking Blocksize** | Each GI worker thread’s stack size. | `memorysetup-temp-allocator-size-gi-baking-worker` | `262144`  
****NavMesh** A mesh that Unity generates to approximate the walkable areas and obstacles in your environment for path finding and AI-controlled navigation. [More info](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavInnerWorkings.html%23walkable-areas)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#NavMesh) Worker Block Size** | Nav **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) worker threads stack size. | `memorysetup-temp-allocator-size-nav-mesh-worker` | `65536`  
## Fast Thread Shared Temporary Allocators
[Fast linear allocator](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html) for short lived allocations shared between threads.
**Allocator** | **Description** | **Command line argument** |  **Default value** (in bytes)  
---|---|---|---  
**Job Allocator Block Size** | The round robin linear thread allocator Unity mainly uses for the job worker threads. | `memorysetup-job-temp-allocator-block-size` | `2097152`  
**Background Job Allocator Block Size** | The linear allocator for the background workers that allows longer lived allocations. | `memorysetup-job-temp-allocator-block-size-background` | `21048576`  
**Job Allocator Block Size on low memory platforms** | Platforms with less than 2 GB memory use this size for both the job workers and the background jobs. | `memorysetup-job-temp-allocator-reduction-small-platforms` | `262144`  
## Profiler Allocators
Allocators that Unity uses exclusively for [the Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html) so that they don’t interfere with the application’s allocation patterns. They have the following settings:
**Setting** | **Description** | **Command line argument** | **Default value**  
---|---|---|---  
****Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) Block Size** | The block size for the main part of the Profiler. | `memorysetup-profiler-allocator-block-size` | `16777216`  
**Editor Profiler Block Size** | Block size for the Editor part of the Profiler. This isn’t present in players. | `memorysetup-profiler-editor-allocator-block-size` |  `1048576` bytes  
### Shared Profiler Bucket Allocator
Shared bucket allocator for the Profiler and Editor Profiler allocators. Not present on low memory platforms. It has the following settings:
**Setting** | **Description** | **Command line argument** | **Default value**  
---|---|---|---  
**Bucket Allocator Granularity** | Step size for buckets in the shared allocator. | `memorysetup-profiler-bucket-allocator-granularity` |  `16` bytes  
**Bucket Allocator BucketCount** | Number of bucket sizes. For example, if the value is 4, the sizes are 16 bytes, 32 bytes, 48 bytes, and 64 bytes. | `memorysetup-profiler-bucket-allocator-bucket-count` | `8`  
**Bucket Allocator Block Size** | Size of memory blocks used for buckets. | `memorysetup-profiler-bucket-allocator-block-size` | Editor: `33554432` bytes  
Player: `4194304` bytes  
**Bucket Allocator Block Count** | Maximum number of blocks to be allocated. | `memorysetup-profiler-bucket-allocator-block-count` | Editor: `8`  
Player: `1`  
## Additional resources
  * [Native memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-allocators.html)
  * [Customizing native memory allocators](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html)
  * [Native memory allocator examples](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-examples.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/memory-allocator-customization.html)
Customizing native memory allocators
[](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-native-memory-allocator-examples.html)
Native memory allocator examples
