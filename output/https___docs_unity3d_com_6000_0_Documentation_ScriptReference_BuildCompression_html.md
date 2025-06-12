* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html

# BuildCompression
struct in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Contains information about compression methods, compression levels and block sizes that are supported by Asset Bundle compression at build time and recompression at runtime.
The formats that are currently supported are exposed with static properties. There are three supported BuildCompression types for compressing AssetBundles during builds (LZ4, LZMA and Uncompressed) and two supported recompression methods for runtime (LZ4Runtime and UncompressedRuntime).  
  
Additional resources: [AssetBundle.RecompressAssetBundleAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.RecompressAssetBundleAsync.html), [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html), [BuildAssetBundleOptions.ChunkBasedCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ChunkBasedCompression.html), [BuildAssetBundleOptions.UncompressedAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.UncompressedAssetBundle.html), [BuildOptions.CompressWithLz4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CompressWithLz4.html), [CompressionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.html), [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html). 
### Static Properties
Property | Description  
---|---  
[LZ4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.LZ4.html) | LZ4HC "Chunk Based" Compression.  
[LZ4Runtime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.LZ4Runtime.html) | LZ4 Compression for runtime recompression.  
[LZMA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.LZMA.html) | LZMA Compression.  
[Uncompressed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.Uncompressed.html) | Uncompressed Asset Bundle.  
[UncompressedRuntime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.UncompressedRuntime.html) | Uncompressed Asset Bundle.  
* * *
