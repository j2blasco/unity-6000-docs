* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.AddConfigObject.html

#  [EditorBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html).AddConfigObject
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
public static void AddConfigObject(string name, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) obj, bool overwrite); 
### Parameters
Parameter | Description  
---|---  
name | The name of the object reference in string format. This string name must be unique within your project or the overwrite parameter must be set to true.  
obj | Object reference to be stored. This object must be persisted and not `null`.  
overwrite | Boolean parameter used to specify that you want to overwrite an entry with the same name if one already exists.  
### Returns
**void** Throws an exception if the object is `null`, not persisted, or if there is a name conflict and the overwrite parameter is set to false. 
### Description
Store a reference to a config object by name. The object must be an asset in the project, otherwise it will not be saved when the editor is restarted or scripts are reloaded. To avoid name conflicts with other packages, it is recommended that names are qualified by a namespace, i.e. "company.package.name".
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.IO;  
  
public class MyConfigData : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public static MyConfigData GetDefault()
    {
        //name of config data object
        string stringName = "com.myproject.myconfigdata";
        //path to Config Object and asset name
        string stringPath = "Assets/myconfigdata.asset";
        //used to hold config data
        MyConfigData data = null;  
  
        //if a config data object exists with the same name, return its config data
        if (EditorBuildSettings.TryGetConfigObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.TryGetConfigObject.html)<MyConfigData>(stringName, out data))
            return data;  
  
        //If the asset file already exists, store existing config data
        if (File.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.Exists.html)(stringPath))
            data = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<MyConfigData>(stringPath);
        //if no previous config data exists
        if (data == null)
        {
            //show save file dialog and return user selected path name
            stringPath = EditorUtility.SaveFilePanelInProject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SaveFilePanelInProject.html)("New Config File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html)", "myconfigdata", "asset", "Select Config File[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.File.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)", "Assets");
            //initialise config data object
            data = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MyConfigData>();
            //create new asset from data at specified path
            //asset MUST be saved with the AssetDatabase[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html) before adding to EditorBuildSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html)
            AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(data, stringPath);
        }  
  
        //add the new or loaded config object to EditorBuildSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html)
        EditorBuildSettings.AddConfigObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.AddConfigObject.html)(stringName, data, false);  
  
        return data;
    }
}

```

* * *
