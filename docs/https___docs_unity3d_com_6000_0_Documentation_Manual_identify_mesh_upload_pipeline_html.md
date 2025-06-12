* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/identify-mesh-upload-pipeline.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Loading texture and mesh data asynchronously](https://docs.unity3d.com/6000.0/Documentation/Manual/loading-texture-mesh-data-asynchronously.html)
  * Check whether a mesh uses the asynchronous upload pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData.html)
Texture and mesh loading
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-asynchronous-upload-pipeline.html)
Configure the asynchronous upload pipeline
# Check whether a mesh uses the asynchronous upload pipeline
To identify which upload pipeline Unity is using for a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), you can use the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) or another profiling tool and observe thread activity and **profiler markers** Placed in code to describe a CPU or GPU event that is then displayed in the Unity Profiler window. Added to Unity code by default, or you can use [ProfilerMarker API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-guide.html) to add your own custom markers. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-markers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profilermarker).
The following indicate that Unity is using the asynchronous upload pipeline to upload textures or meshes:
  * The `AsyncUploadManager.ScheduleAsyncRead`, `AsyncReadManager.ReadFile`, and `Async.DirectTextureLoadBegin` profiler markers.
  * Activity on the `AsyncRead` thread.


If you do not see this activity, then Unity is not using the asynchronous upload pipeline.
Note that the following profiler markers do not indicate that Unity is using the asynchronous upload pipeline; Unity calls them to check whether any asynchronous upload work needs to occur:
  * `Initialization.AsyncUploadTimeSlicedUpdate`
  * `AsyncUploadManager.AsyncResourceUpload`
  * `AsyncUploadManager.ScheduleAsyncCommands`


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData.html)
Texture and mesh loading
[](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-asynchronous-upload-pipeline.html)
Configure the asynchronous upload pipeline
