* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyBuffer.html

#  [Graphics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.html).CopyBuffer
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
## Declaration
public static void CopyBuffer([GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) source, [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) dest); 
### Parameters
Parameter | Description  
---|---  
source | The source buffer.  
dest | The destination buffer.  
### Description
Copies the contents of one [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html) into another.
The GPU copies the buffer contents efficiently.  
  
Total buffer sizes (i.e. [count](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-count.html) multiplied by [stride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer-stride.html)) must match between source and destination buffers. The source buffer must have a [GraphicsBuffer.Target.CopySource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.CopySource.html) target flag, and the destination buffer must have a [GraphicsBuffer.Target.CopyDestination](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.CopyDestination.html) target flag.
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // create a source index buffer and set data for it
        var src = new GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html)(
            GraphicsBuffer.Target.Index[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html) | GraphicsBuffer.Target.CopySource[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.CopySource.html),
            3, 2);
        src.SetData(new ushort[]{1, 10, 100});
        // create a destination index buffer and copy source into it
        var dst = new GraphicsBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html)(
            GraphicsBuffer.Target.Index[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.Index.html) | GraphicsBuffer.Target.CopyDestination[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.Target.CopyDestination.html),
            3, 2);
        Graphics.CopyBuffer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyBuffer.html)(src, dst);  
  
        // check the copied data
        var got = new ushort[3];
        dst.GetData(got);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"copied data: {got[0]}, {got[1]}, {got[2]}");  
  
        // release the buffers
        src.Release();
        dst.Release();
    }
}

```

Additional resources: [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html), [CommandBuffer.CopyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyBuffer.html), [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html).
* * *
