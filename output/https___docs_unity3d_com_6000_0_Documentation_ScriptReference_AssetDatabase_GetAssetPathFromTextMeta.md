* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathFromTextMetaFilePath.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).GetAssetPathFromTextMetaFilePath
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
public static string GetAssetPathFromTextMetaFilePath(string path); 
### Description
Gets the path to the asset file associated with a text .meta file.
```
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
 public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
 {
     [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Get All Assets With Meta File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html)")]
     static void GetAllAssetsWithMetaFiles()
     {
         var files = Directory.GetFiles("Assets/", "*.meta", SearchOption.AllDirectories);  
  
         foreach (var file in files)
         {
             var path = AssetDatabase.GetAssetPathFromTextMetaFilePath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathFromTextMetaFilePath.html)(file);
             Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(path);
         }
     }
 }

```

* * *
