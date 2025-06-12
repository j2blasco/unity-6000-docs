* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter-extraUserProperties.html

#  [ModelImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html).extraUserProperties
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
extraUserProperties; 
### Description
A list of default FBX properties to treat as user properties during OnPostprocessGameObjectWithUserProperties.
Specify the names of default FBX properties to be consider as extra user properties to pass to [AssetPostprocessor.OnPostprocessGameObjectWithUserProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.OnPostprocessGameObjectWithUserProperties.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class MyPostProcessor : AssetPostprocessor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPostprocessor.html)
{
    public override uint GetVersion() => 1;  
  
    //Adding 1 FBX default properties to be considered as UserProperties + 1 not existing in the imported FBX
    private void OnPreprocessModel()
    {
        string[] extraUserPropertyNames =
        {
            "currentUVSet",
            "MyNonFbxDefaultProperty"
        };
        ((ModelImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModelImporter.html))assetImporter).extraUserProperties = extraUserPropertyNames;
    }  
  
    //Importing a FBX with a user defined Property "MyDefinedProperty"
    private void OnPostprocessGameObjectWithUserProperties(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, string[] propNames, object[] values)
    {
        foreach (var propName in propNames)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(propName);
        }
    }  
  
    // Will display :
    //  currentUVSet
    //  MyDefinedProperty
}

```

* * *
