* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html

#  [AssetDatabase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html).CreateFolder
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
public static string CreateFolder(string parentFolder, string newFolderName); 
### Parameters
Parameter | Description  
---|---  
parentFolder | The path to the parent folder. Must start with "Assets/".  
newFolderName | The name of the new folder.  
### Returns
**string** The GUID of the newly created folder, if the folder was created successfully. Otherwise returns an empty string. 
### Description
Creates a new folder, in the specified parent folder.  
  
The parent folder string must start with the "Assets" folder, and all folders within the parent folder string must already exist. For example, when specifying "Assets/ParentFolder1/Parentfolder2/", the new folder will be created in "ParentFolder2" only if ParentFolder1 and ParentFolder2 already exist.
Note: When Unity attempts to create a folder, if a folder with the same name exists at the same path, Unity adds a sequential number to the end of the file name. For example, "My Folder" becomes "My Folder 1".
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateFolderExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/Create Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html) and Some Assets")]
    static void CreateFolder()
    {
        AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "My Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)");
        string guid = AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets/My Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)", "My Another Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)");
        string newFolderPath = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(newFolderPath);  
  
        // Create a simple material asset in the created folder
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Specular"));
        string newAssetPath = newFolderPath + "/MyMaterial.mat";
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, newAssetPath);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(material));
    }
}

```

* * *
