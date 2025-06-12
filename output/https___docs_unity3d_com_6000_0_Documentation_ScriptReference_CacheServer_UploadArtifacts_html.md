* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.UploadArtifacts.html

#  [CacheServer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.html).UploadArtifacts(GUID[] guids, bool uploadAllRevisions)
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
### Parameters
Parameter | Description  
---|---  
guids | Array of GUIDs to upload to the Accelerator. If array is empty, all assets are uploaded.  
uploadAllRevisions | Specifies if all revisions of the Assets corresponding to the supplied GUIDs should also be uploaded. Each time an Asset is edited, a new revision is created. Revisions also include non-primary artifacts. That is, artifacts not generated via their default importer for an asset type, but by another importer. One example of this is the Preview importer. That uses the same Asset GUID but a different importer to generate an asset preview.  
### Description
Upload the specified GUIDs to the Accelerator. If keys is empty, all assets are uploaded.
Use this method to upload assets to the Accelerator in an asynchronous way. This API can be used when an already imported project is opened with Unity but was not previously imported using the Accelerator. This method allows you to upload Assets specified by the guids array. If the supplied array is empty or null, all assets are uploaded. Additionally, the command line argument -cacheServerUploadExistingImports if you would like to run this on a Continuous Integration server. **NOTE:** Non-primary artifacts will also be uploaded when using this API. For example, if you have a Prefab with a preview, both the Prefab and its Preview will be uploaded to the Accelerator when specifying only the GUID of the Prefab.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CacheServerExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CacheServer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.html)/UploadAllAssetsToCacheServer")]
    public static void UploadAllAssetsToCacheServer()
    {
        //This will upload all Assets to Accelerator
        CacheServer.UploadArtifacts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.UploadArtifacts.html)();
    }  
  
}
```

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CacheServerExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CacheServer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.html)/UploadAllPrefabsToCacheServer")]
    public static void UploadAllPrefabsToCacheServer()
    {
        var prefabFileGUIDs = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:Prefab");
        var guids = new GUID[prefabFileGUIDs.Length];
        var counter = 0;
        foreach (var curGUID in prefabFileGUIDs)
        {
            guids[counter] = new GUID(curGUID);
            ++counter;
        }  
  
        //This will upload all Prefabs to Accelerator
        CacheServer.UploadArtifacts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.UploadArtifacts.html)(guids);
    }
}
```

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
public class CacheServerExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CacheServer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.html)/UploadAllScriptsToCacheServer")]
    public static void UploadAllScriptsToCacheServer()
    {
        var scriptFileGUIDs = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:Script");
        var guids = new GUID[scriptFileGUIDs.Length];
        var counter = 0;
        foreach (var curGUID in scriptFileGUIDs)
        {
            guids[counter] = new GUID(curGUID);
            ++counter;
        }
        //This will upload all Scripts to Accelerator
        CacheServer.UploadArtifacts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.UploadArtifacts.html)(guids);
    }
}
```

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CacheServerExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("CacheServer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.html)/UploadAllTextureVersionsToCacheServer")]
    public static void UploadAllTextureVersionsToCacheServer()
    {
        var textureGUIDs = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)");
        var guids = new GUID[textureGUIDs.Length];
        var counter = 0;
        foreach (var curGUID in textureGUIDs)
        {
            guids[counter] = new GUID(curGUID);
            ++counter;
        }  
  
        //Every time an asset is modified, and imported, a new revision
        //of that Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) is created. As such, the history of the import
        //results of an Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) are kept around, and purged when the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) 
        //is restarted.
        //Supplying the uploadAllRevisions as true, then all revisions 
        //of an asset will be uploaded.
        CacheServer.UploadArtifacts[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CacheServer.UploadArtifacts.html)(guids, true);
    }
}
```

* * *
