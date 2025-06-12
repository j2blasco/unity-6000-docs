* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.AddComponent.html

#  [ObjectFactory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.html).AddComponent
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
public static [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) AddComponent([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, Type type); 
## Declaration
public static T AddComponent([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
gameObject | The GameObject to add the new component to.  
type | The type of component to create and add to the GameObject.  
### Returns
**Component** Returns the component that was created and added to the GameObject. 
### Description
Creates a new component and adds it to the specified GameObject.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateComponentExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ObjectFactoryExample/Add Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) to Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html)")]
    public void AddDefaultComponentEditor()
    {
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null)
        {
            Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera = ObjectFactory.AddComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.AddComponent.html)<Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)>(Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html));
        }
    }
}

```

* * *
