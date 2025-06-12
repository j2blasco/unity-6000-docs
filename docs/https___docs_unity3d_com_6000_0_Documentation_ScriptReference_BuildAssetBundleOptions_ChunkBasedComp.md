* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ChunkBasedCompression.html

#  [BuildAssetBundleOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.html).ChunkBasedCompression
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
Use chunk-based LZ4 compression when creating the AssetBundle.
When chunk-based compression is used, the content of the AssetBundle is broken into individual segments, which are compressed independently using the [CompressionType.Lz4HC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.Lz4HC.html) algorithm. The resulting file is typically larger than the full-file compression which is used by default, but AssetBundles built with this format can be loaded incrementally, e.g. without decompressing the full contents into memory. This is the default format used for AssetBundles stored in the AssetBundle Cache.  
  
Additional resources: [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html), [BuildCompression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildCompression.html), [CompressionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.html), [ArchiveHandle.Compression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.Compression.html), [Caching](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Caching.html), [BuildAssetBundleOptions.UncompressedAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.UncompressedAssetBundle.html), [BuildOptions.CompressWithLz4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CompressWithLz4.html). 
```
//Create a folder (right click in the Assets folder and go to **Create**>**Folder**), and name it “Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)” if it doesn’t already exist
//Place this script in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) folder  
  
//This script creates a new Menu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Menu.html) named “Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)” and new options within the menu named “Normal” and “Chunk Based Compression”. Click these menu items to build an AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    //Creates a new menu (Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles) and item (Normal) in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles/Normal")]
    static void BuildABsNone()
    {
        //Build AssetBundles with no special options
        //They will be written in the custom folder ("MyAssetBuilds") which needs to exist prior to this call.
        BuildPipeline.BuildAssetBundles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", BuildAssetBundleOptions.None[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.None.html), BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html));
    }  
  
    //Creates a new item (Chunk Based Compression) in the new Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles menu
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Build Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Bundles/Chunk Based Compression")]
    static void BuildABsChunk()
    {
        //Build the AssetBundles in this mode
        BuildPipeline.BuildAssetBundles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.BuildAssetBundles.html)("Assets/MyAssetBuilds", BuildAssetBundleOptions.ChunkBasedCompression[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildAssetBundleOptions.ChunkBasedCompression.html), BuildTarget.StandaloneOSX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.StandaloneOSX.html));
    }
}

```

* * *
