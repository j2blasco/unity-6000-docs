* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.TryGetConfigObject.html

#  [EditorBuildSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorBuildSettings.html).TryGetConfigObject
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
public static bool TryGetConfigObject(string name, out T result); 
### Parameters
Parameter | Description  
---|---  
name | The name in string format of the config object reference to be fetched.  
result | The config object reference where the returned object will be stored. This must be an object of type Object.  
### Returns
**bool** Returns true if the config object reference was found and the type matched the result parameter. Returns false if the entry is not found, the config object reference is `null`, or if the type requested does not match the type stored. 
### Description
Retrieve a config object reference by name.
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
