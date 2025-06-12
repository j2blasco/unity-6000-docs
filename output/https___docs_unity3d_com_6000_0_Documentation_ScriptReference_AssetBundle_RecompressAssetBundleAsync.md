* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.RecompressAssetBundleAsync.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).RecompressAssetBundleAsync
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
public static [AssetBundleRecompressOperation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleRecompressOperation.html) RecompressAssetBundleAsync(string inputPath, string outputPath, [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) method, uint expectedCRC, [ThreadPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ThreadPriority.html) priority); 
### Parameters
Parameter | Description  
---|---  
inputPath | Path to the [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) to recompress.  
outputPath | Path to the recompressed [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) to be generated. Can be the same as inputPath.  
method | The compression method, level and blocksize to use during recompression. Only some [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) types are supported (see note).  
expectedCRC | CRC of the [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) to test against. Testing this requires additional file reading and computation. Pass in 0 to skip this check. Unity does not compute a CRC when the source and destination [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) are the same, so no CRC verification takes place (see note).  
priority | The priority at which the recompression operation should run. This sets thread priority during the operation and does not effect the order in which operations are performed. Recompression operations run on a background worker thread.  
### Description
Asynchronously recompress a downloaded/stored AssetBundle from one [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) to another.
Method must be a [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) whose name ends with Runtime, for example LZ4Runtime, otherwise an ArgumentException is thrown. When the destination [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html) is the same as the source, this becomes a copy operation internally, and Unity does not compute a CRC of the uncompressed data. Passing in a non-zero expectedCRC in this case raises a warning, and no CRC validation takes place.
* * *
