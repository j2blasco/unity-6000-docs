* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterType.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetImporterType
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
public static Type GetImporterType(GUID guid); 
### Parameters
Parameter | Description  
---|---  
guid | GUID of the asset to get the importer type from.  
### Description
Returns the type of importer associated with an asset without loading the asset.
This method allows you to determine which importer is associated with an asset. This method is more efficient than [AssetImporter.GetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html), which also loads the object. If you need to check a large number of asset importers at once, you should use the batch version of this method [AssetDatabase.GetImporterTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterTypes.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/GetMatchingAssetType")]
    public static void GetMatchingAssetType()
    {
        var matchingAssets = AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("Powerup");
        var matchingAssetGuid = new GUID(matchingAssets[0]);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Importer type: {AssetDatabase.GetImporterType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterType.html)(matchingAssetGuid)}");
    }
}
```

* * *
## Declaration
public static Type GetImporterType(string assetPath); 
### Parameters
Parameter | Description  
---|---  
assetPath | Path of asset to get importer Type from.  
### Description
Returns the type of the importer associated with an asset without loading the asset.
The asset path you provide should be relative to the project folder root. For example, "Assets/MyTextures/hello.png". This method allows you to determine which importer is associated with an asset. This method is more efficient than [AssetImporter.GetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html), which also loads the object. If you need to check a large number of asset importers at once, you should use the batch version of this method [AssetDatabase.GetImporterTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterTypes.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/GetImporterTypeOfSelectedObject")]
    public static void GetImporterTypeOfSelectedObject()
    {
        var selectedObject = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html);
        var objectPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(selectedObject);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Importer type: {AssetDatabase.GetImporterType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterType.html)(objectPath)}");
    }
}
```

* * *
