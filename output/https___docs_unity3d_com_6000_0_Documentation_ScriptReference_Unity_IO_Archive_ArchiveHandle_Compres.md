* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.Compression.html

#  [ArchiveHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.html).Compression
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
[CompressionType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CompressionType.html) Compression; 
### Description
The type of compression the archive uses.
Only accessible if the archive loaded successfully.  
  
Additional resources: [AssetBundles compression](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundles-Cache.html). 
```
using Unity.Content;
using Unity.IO.Archive;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public static class ArchiveUtilities
{
#if UNITY_EDITOR
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Debug[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html)/Check Archive Compression")]
    static public void CheckCompression()
    {
        string archivePath = EditorUtility.OpenFilePanel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.OpenFilePanel.html)("Pick AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) or other Unity Archive file", "", "");
        if (archivePath.Length == 0)
            return;  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Bundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Bundle.html) {archivePath} has compression type {GetArchiveCompression(archivePath)}");
    }
#endif  
  
    static public UnityEngine.CompressionType GetArchiveCompression(string archivePath)
    {
        var archiveHandle = ArchiveFileInterface.MountAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveFileInterface.MountAsync.html)(ContentNamespace.Default[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Content.ContentNamespace.Default.html), archivePath, "temp:");
        archiveHandle.JobHandle.Complete();  
  
        if (archiveHandle.Status == ArchiveStatus.Failed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveStatus.Failed.html))
            throw new System.ArgumentException($"Failed to load {archivePath}");  
  
        var compression = archiveHandle.Compression;
        archiveHandle.Unmount().Complete();  
  
        return compression;
    }
}

```

* * *
