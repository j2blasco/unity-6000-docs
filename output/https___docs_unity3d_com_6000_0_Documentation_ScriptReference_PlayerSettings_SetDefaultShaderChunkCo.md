* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetDefaultShaderChunkCount.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetDefaultShaderChunkCount
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
## Declaration
public static void SetDefaultShaderChunkCount(int chunkCount); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The build target to set the shader chunk count for.  
chunkCount | The maximum number of chunks to keep in memory for each shader.  
### Description
Sets the default limit on the number of shader variant chunks Unity loads and keeps in memory.
To limit the amount of memory Unity uses to [load shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html), you can use `SetDefaultShaderChunkCount` to set the maximum number of compressed shader variant chunks you want Unity to load and decompress into CPU memory at one time.  
  
The default value is `0`, which means Unity loads and decompresses all the chunks into memory.  
  
When Unity reaches the limit but needs to load another chunk, Unity removes the least recently used decompressed chunk from memory to make room.  
  
You can use [PlayerSettings.SetDefaultShaderChunkSizeInMB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetDefaultShaderChunkSizeInMB.html) to limit the size of compressed chunks.  
  
Use the following to override the default shader chunk count: 
  * [PlayerSettings.SetShaderChunkCountForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetShaderChunkCountForPlatform.html) to override for a build target.
  * [Shader.maximumChunksOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader-maximumChunksOverride.html) to override at runtime.


Additional resources: [PlayerSettings.GetDefaultShaderChunkCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetDefaultShaderChunkCount.html).
* * *
