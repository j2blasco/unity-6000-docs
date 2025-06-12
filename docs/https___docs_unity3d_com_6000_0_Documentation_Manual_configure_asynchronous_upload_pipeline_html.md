* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/configure-asynchronous-upload-pipeline.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Working with GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/working-with-gameobjects.html)
  * [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)
  * [Loading texture and mesh data asynchronously](https://docs.unity3d.com/6000.0/Documentation/Manual/loading-texture-mesh-data-asynchronously.html)
  * Configure the asynchronous upload pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/identify-mesh-upload-pipeline.html)
Check whether a mesh uses the asynchronous upload pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/text-meshes.html)
Text meshes
# Configure the asynchronous upload pipeline
Unity provides optimization settings specific to the asynchronous upload pipeline. To access these settings, open the Project’s [Quality settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html). 
Note that you cannot configure settings for the synchronous upload pipeline.
![The Async Upload settings in the Quality settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AsyncUploadQualitySettings.png) The Async Upload settings in the Quality settings
### Configure the streaming buffer for mesh data
Unity re-uses a single ring buffer to stream texture and **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) data to the GPU. This reduces the number of memory allocations required.
The **Async Upload Buffer** determines the size of this ring buffer. It has a minimum size of 2 megabytes, and a maximum size of 2047 megabytes.
Unity automatically resizes the buffer to fit the largest texture or mesh that is currently loading. This can be a slow operation, especially if Unity has to perform it more than once; for example, if you are loading many textures that are larger than the default buffer size. To reduce the number of times that Unity must resize the buffer, set this value to fit the largest value that you expect to load. This is usually the largest texture in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). 
You can configure this value in the Quality settings window, or using the [QualitySettings.asyncUploadBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadBufferSize.html) API.
### Configure the CPU’s upload time
To control the amount of time the CPU spends uploading texture or mesh data to the GPU, use **Async Upload Time Slice**. The value is in milliseconds per frame.
A larger value means the data will be ready on the GPU sooner, but the CPU will spend more time on upload operations during those frames. Note that Unity only uses this time for uploading if there is data waiting in the buffer to be uploaded to the GPU; if there is no data waiting, Unity can use this time for other operations.
You can configure this value in the Quality settings window, or using the [QualitySettings.asyncUploadTimeSlice](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadTimeSlice.html) API. 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/identify-mesh-upload-pipeline.html)
Check whether a mesh uses the asynchronous upload pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/text-meshes.html)
Text meshes
