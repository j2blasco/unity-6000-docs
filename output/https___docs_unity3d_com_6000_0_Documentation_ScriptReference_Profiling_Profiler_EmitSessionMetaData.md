* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitSessionMetaData.html

#  [Profiler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.html).EmitSessionMetaData
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
public static void EmitSessionMetaData(Guid id, int tag, Array data); 
## Declaration
public static void EmitSessionMetaData(Guid id, int tag, List<T> data); 
## Declaration
public static void EmitSessionMetaData(Guid id, int tag, NativeArray<T> data); 
### Parameters
Parameter | Description  
---|---  
id | Unique identifier associated with the data.  
tag | Data stream index.  
data | Binary data.  
### Description
Write metadata associated with the whole Profiler session capture.
Use _EmitSessionMetaData_ to write arbitrary binary data that should be available for all frames of this session. Data must contain only blittable types.  
  
If the information you want to store in the Profiler meta data might change from frame to frame, consider using [EmitFrameMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitFrameMetaData.html) instead.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Diagnostics;
using Unity.Collections;
using UnityEngine;
using UnityEngine.Profiling;  
  
public class Example
{
    public struct TextureInfo
    {
        public int format;
        public int w;
        public int h;
    }  
  
    public static readonly Guid MyProjectId = new Guid("7E1DEA84-51F1-477A-82B5-B5C57AC1EBF7");
    public static readonly int TextureInfoTag = 0;
    public static readonly int TextureDataTag = 1;  
  
    [Conditional("ENABLE_PROFILER")]
    public void EmitTextureToProfilerStream(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) t)
    {
        if (!Profiler.enabled[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html))
            return;
        TextureInfo textureInfo = new TextureInfo() { format = (int)t.format, w = t.width, h = t.height };
        NativeArray<byte> textureData = t.GetRawTextureData<byte>();
        Profiler.EmitSessionMetaData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitSessionMetaData.html)(MyProjectId, TextureInfoTag, new[] { textureInfo });
        Profiler.EmitSessionMetaData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitSessionMetaData.html)(MyProjectId, TextureDataTag, textureData);
    }
}

```

**Note:**   
Writing large chunks of data might increase the Profiler's overhead and memory usage. Always check if Profiler is [enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler-enabled.html) before generating data. When possible, write data in small chunks to reduce memory usage.  
  
Additional resources: [FrameDataView.GetSessionMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetSessionMetaData.html).
* * *
