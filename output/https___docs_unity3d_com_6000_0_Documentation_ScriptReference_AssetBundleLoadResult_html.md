* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.html

# AssetBundleLoadResult
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
The result of an Asset Bundle Load or Recompress Operation.
### Properties
Property | Description  
---|---  
[Success](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.Success.html) | The operation completed successfully.  
[Cancelled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.Cancelled.html) | The operation was cancelled.  
[NotMatchingCrc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.NotMatchingCrc.html) | The decompressed Asset data did not match the precomputed CRC. This may suggest that the AssetBundle did not download correctly.  
[FailedCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.FailedCache.html) | The Asset Bundle was not successfully cached.  
[NotValidAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.NotValidAssetBundle.html) | This does not appear to be a valid Asset Bundle.  
[NoSerializedData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.NoSerializedData.html) | The Asset Bundle does not contain any serialized data. It may be empty, or corrupt.  
[NotCompatible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.NotCompatible.html) | The AssetBundle is incompatible with this version of Unity.  
[AlreadyLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.AlreadyLoaded.html) | The Asset Bundle is already loaded.  
[FailedRead](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.FailedRead.html) | Failed to read the Asset Bundle file.  
[FailedDecompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.FailedDecompression.html) | Failed to decompress the Asset Bundle.  
[FailedWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.FailedWrite.html) | Failed to write to the file system.  
[FailedDeleteRecompressionTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.FailedDeleteRecompressionTarget.html) | The target path given for the Recompression operation could not be deleted for swap with recompressed bundle file.  
[RecompressionTargetIsLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.RecompressionTargetIsLoaded.html) | The target path given for the Recompression operation is an Archive that is currently loaded.  
[RecompressionTargetExistsButNotArchive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundleLoadResult.RecompressionTargetExistsButNotArchive.html) | The target path given for the Recompression operation exists but is not an Archive container.  
* * *
