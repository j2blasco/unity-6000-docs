* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.html

# CompressionType
enumeration
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
Compression Method for Asset Bundles.
When building or recompressing Asset Bundles, these are the available compression methods. Some of these are only available for building and cannot be used for recompression.  
  
Additional resources: [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html), [AssetBundle.RecompressAssetBundleAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.RecompressAssetBundleAsync.html), [ArchiveHandle.Compression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.Compression.html). 
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.None.html) | Uncompressed Asset Bundles are larger than compressed Asset Bundles, but they are the fastest to access once downloaded.  
[Lzma](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.Lzma.html) | LZMA compression results in smaller compressed Asset Bundles but they must be entirely decompressed before use.  
[Lz4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.Lz4.html) | LZ4 compression results in larger compressed files than LZMA, but does not require the entire bundle to be decompressed before use.  
[Lz4HC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.Lz4HC.html) | LZ4HC is a high compression variant of LZ4. LZ4HC compression results in larger compressed files than LZMA, but does not require the entire bundle to be decompressed before use.  
* * *
