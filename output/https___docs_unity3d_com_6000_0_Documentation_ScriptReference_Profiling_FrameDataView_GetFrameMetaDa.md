* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.GetFrameMetaData.html

#  [FrameDataView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.html).GetFrameMetaData
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
public NativeArray<T> GetFrameMetaData(Guid id, int tag); 
## Declaration
public NativeArray<T> GetFrameMetaData(Guid id, int tag, int index); 
### Parameters
Parameter | Description  
---|---  
id | Project or package identifier.  
tag | Data stream index.  
index | Chunk index.  
### Returns
**NativeArray <T>** Returns the frame metadata as a NativeArray. 
### Description
Retrieves metadata associated with the frame.
Use _GetFrameMetaData_ to retrieve the data that the [Profiler.EmitFrameMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitFrameMetaData.html) method wrote to the Profiler stream.  
  
Use _id_ to identify the metadata from your Project or package.  
Use _tag_ to distinguish between different data streams.  
Use _index_ to retrieve separate data chunks for each [Profiler.EmitFrameMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitFrameMetaData.html) called in a frame.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using Unity.Collections;
using UnityEditor.Profiling;
using UnityEditorInternal;
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
  
    public void EmitTextureToProfilerStream(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) t)
    {
        TextureInfo textureInfo = new TextureInfo() { format = (int)t.format, w = t.width, h = t.height };
        NativeArray<byte> textureData = t.GetRawTextureData<byte>();
        Profiler.EmitFrameMetaData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitFrameMetaData.html)(MyProjectId, TextureInfoTag, new[] { textureInfo });
        Profiler.EmitFrameMetaData[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitFrameMetaData.html)(MyProjectId, TextureDataTag, textureData);
    }  
  
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetTextureFromProfilerStream(int frame)
    {
        using (var frameData = ProfilerDriver.GetHierarchyFrameDataView(frame, 0, HierarchyFrameDataView.ViewModes.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView.ViewModes.Default.html), HierarchyFrameDataView.columnDontSort[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.HierarchyFrameDataView-columnDontSort.html), false))
        {
            NativeArray<TextureInfo> textureInfos = frameData.GetFrameMetaData<TextureInfo>(MyProjectId, TextureInfoTag);
            if (textureInfos.Length == 0)
                return null;  
  
            NativeArray<byte> textureData = frameData.GetFrameMetaData<byte>(MyProjectId, TextureDataTag);
            if (textureData.Length == 0)
                return null;  
  
            TextureInfo textureInfo = textureInfos[0];
            Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(textureInfo.w, textureInfo.h, (TextureFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html))textureInfo.format, false);
            texture.LoadRawTextureData(textureData);  
  
            return texture;
        }
    }
}

```

**Note:**   
The _FrameDataView_ instance defines the lifetime of the returned ''NativeArray'. As such, if _FrameDataView_ is disposed, all returned metadata becomes invalid and cannot be used. Copy data to a new _NativeArray_ if you need it for longer duration.  
  
Additional resources: [Profiler.EmitFrameMetaData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.Profiler.EmitFrameMetaData.html).
* * *
