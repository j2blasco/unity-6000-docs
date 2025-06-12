* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).ImportAsset
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
public static void ImportAsset(string path, [ImportAssetOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.html) options = ImportAssetOptions.Default); 
### Description
Import asset at path.
This imports an Asset at the specified path, and triggers a number of callbacks including [AssetModificationProcessor.OnWillSaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetModificationProcessor.OnWillSaveAssets.html) and [AssetPostprocessor.OnPostprocessAllAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessAllAssets.html)  
  
All paths are relative to the project folder, for example: "Assets/MyTextures/hello.png"  
  
Additional resources: [ImportAssetOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImportAssetOptions.html).
```
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ImportAssetExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("APIExamples/ImportAsset")]
    static void ImportAssetOnlyImportsSingleAsset()
    {
        string[] fileNames = new[] { "test_file01.txt", "test_file02.txt" };  
  
        for (int i = 0; i < fileNames.Length; ++i)
        {
            var unimportedFileName = fileNames[i];
            var assetsPath = Application.dataPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-dataPath.html) + "/Artifacts/" + unimportedFileName;
            File.WriteAllText(assetsPath, "Testing 123");
        }  
  
        var relativePath = "Assets/Artifacts/test_file01.txt";
        AssetDatabase.ImportAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html)(relativePath);
    }
}  
  
public class PostProcessImportAsset : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    //Based on this example, the output from this function should be:
    //  OnPostprocessAllAssets
    //  Imported: Assets/Artifacts/test_file01.txt
    //
    //test_file02.txt should not even show up on the Project Browser
    //until a refresh happens.
    static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("OnPostprocessAllAssets");  
  
        foreach (var imported in importedAssets)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Imported: " + imported);  
  
        foreach (var deleted in deletedAssets)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Deleted: " + deleted);  
  
        foreach (var moved in movedAssets)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Moved: " + moved);  
  
        foreach (var movedFromAsset in movedFromAssetPaths)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Moved from Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html): " + movedFromAsset);
    }
}

```

* * *
