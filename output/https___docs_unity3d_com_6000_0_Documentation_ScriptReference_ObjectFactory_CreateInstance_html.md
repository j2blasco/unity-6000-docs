* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.CreateInstance.html

#  [ObjectFactory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.html).CreateInstance
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
public static Object CreateInstance(Type type); 
## Declaration
public static T CreateInstance(); 
### Parameters
Parameter | Description  
---|---  
type | The type of instance to create.  
### Description
Create a new instance of the given type.
Use this method to create any type of serialized object in the Editor. The created instance uses default values.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateInstanceExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ObjectFactoryExample/Create Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)")]
    public void CreateMaterialEditor()
    {
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = ObjectFactory.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.CreateInstance.html)<Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)>();
        material.shader = Shader.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.Find.html)("Transparent/Diffuse");
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/newMaterial.mat");
    }
}

```

* * *
