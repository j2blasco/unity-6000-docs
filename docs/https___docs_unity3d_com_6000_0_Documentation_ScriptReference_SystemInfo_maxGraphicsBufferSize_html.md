* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxGraphicsBufferSize.html

#  [SystemInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.html).maxGraphicsBufferSize
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
maxGraphicsBufferSize; 
### Description
The maximum size of a graphics buffer ([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html), [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html), vertex/index buffer, etc.) in bytes (Read Only).
Any GPU buffer ([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html), [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or a vertex/index buffer used by a [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html)) can not be larger than this amount of bytes.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // prints maximum graphics buffer size, in megabytes
        var maxSizeMb = SystemInfo.maxGraphicsBufferSize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-maxGraphicsBufferSize.html) / 1024 / 1024;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Maximum graphics buffer size is {maxSizeMb} MB");
    }
}

```

* * *
