* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.GetDefaultReference.html

#  [MonoImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html).GetDefaultReference
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
public Object GetDefaultReference(string name); 
### Parameters
Parameter | Description  
---|---  
name | The name of a public field in the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html).  
### Returns
**Object** The Unity object to use as a default value for the given reference field. 
### Description
Gets the default value for a reference field in the imported [MonoScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoScript.html).
Additional resources: [MonoImporter.SetDefaultReferences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.SetDefaultReferences.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Get Default Reference")]
    public static void GetDefaultReference()
    {
        var assetPath = "Assets/MyMonoBehaviour.cs";
        var monoImporter = AssetImporter.GetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporter.GetAtPath.html)(assetPath) as MonoImporter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoImporter.html);
        var value = monoImporter.GetDefaultReference("MyGameObject");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Default reference for MyGameObject in {monoImporter.GetScript().GetClass().FullName} is {value}");
    }
}

```

* * *
