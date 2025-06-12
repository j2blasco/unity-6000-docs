* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.CreatePrimitive.html

#  [ObjectFactory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.html).CreatePrimitive
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) CreatePrimitive([PrimitiveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.html) type); 
### Parameters
Parameter | Description  
---|---  
type | The type of primitive to create.  
### Description
Creates a GameObject primitive with Undo support. The created primitive will have any existing Preset applied to it, see [Preset Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PresetManager.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreatePrimitiveExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ObjectFactoryExample/Create Cube GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)")]
    public void CreateCubeEditor()
    {
        Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) = ObjectFactory.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
    }
}

```

* * *
