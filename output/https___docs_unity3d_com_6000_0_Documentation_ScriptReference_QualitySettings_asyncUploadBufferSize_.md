* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadBufferSize.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).asyncUploadBufferSize
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
asyncUploadBufferSize; 
### Description
Sets the ring buffer size used for asynchronous texture and mesh data uploads.
The `asyncUploadBufferSize` property determines the size of the ring buffer used for asynchronous texture and mesh uploads in Unity. The minimum value for this property is 2 MB, and the maximum value is 2047 MB.  
  
This property helps optimize the loading of scenes with large assets or many small assets. If the buffer is too small to accommodate the largest asset currently loading, Unity automatically resizes the buffer to fit. However, resizing the buffer can consume additional system resources and introduce memory overhead.  
  
To prevent buffer resizing, set the value to match the size of the largest texture or mesh in the Scene. If you encounter excessive memory usage or performance issues, consider lowering this value to conserve resources. Alternatively, you can disable [asyncUploadPersistentBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadPersistentBuffer.html), although this might lead to memory fragmentation and further complications. Be cautious when disabling persistent buffers, as fragmented memory can make future memory allocations unpredictable and less efficient.
```
using UnityEngine;  
  
public class StartupExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Set ring buffer size to 16 MB.
        QualitySettings.asyncUploadBufferSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-asyncUploadBufferSize.html) = 16;
    }
}

```

The asynchronous upload pipeline allows Unity to perform time-sliced asynchronous texture and mesh data uploads on the render thread. This pipeline provides fine-grained control over memory usage and the time-slicing mechanism, ensuring that asset uploads don't block the main thread and are managed efficiently during runtime. To minimize memory allocations, the pipeline re-uses a ring buffer to process texture and mesh data. You can adjust the size of this ring buffer using the asyncUploadBufferSize property.  
  
This functionality is useful for optimizing scenes with frequent dynamic asset loading or high-memory environments, such as open-world games or applications with large textures and meshes. By allowing asynchronous data uploads, Unity ensures smooth performance and avoids sudden spikes in memory usage or frame times during intensive loading operations.  
  
The asynchronous upload pipeline minimizes allocations, except for the unavoidable allocations performed by the graphics driver itself. It's designed to reuse existing memory efficiently, reducing fragmentation and overhead.  
  
Additional resources: [Loading texture and mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/LoadingTextureandMeshData.html).
* * *
