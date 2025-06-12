* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsValidFolder.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).IsValidFolder
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
public static bool IsValidFolder(string path); 
### Parameters
Parameter | Description  
---|---  
path | The path to the folder.  
### Returns
**bool** Returns true if the folder exists. 
### Description
Given a path to a folder, returns true if it exists, false otherwise.
The given path is relative to the project folder.
```
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetDatabaseExamples : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html)/Create Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html) Structure")]
    static void CreateFolderStructure()
    {
        var folderList = new List<string> { "Animations", "Textures", "Materials", "Prefabs", "Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html)", "Scripts" };  
  
        //Check if folder exists with IsValidFolder if it doesn't create it
        foreach (var folder in folderList)
        {
            if (AssetDatabase.IsValidFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsValidFolder.html)($"Assets/{folder}")) continue;
            AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", folder);
        }
    }
}
```

* * *
