* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.CreateGameObject.html

#  [ObjectFactory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.html).CreateGameObject
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) CreateGameObject(string name, params Type[] types); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) CreateGameObject([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene, [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html) hideFlags, string name, params Type[] types); 
### Parameters
Parameter | Description  
---|---  
name | Name of the GameObject.  
types | The optional types to add to the GameObject when created.  
scene | Scene where the GameObject should be created.  
hideFlags | HideFlags to assign to the GameObject.  
### Returns
**GameObject** Returns the GameObject that was created. 
### Description
Creates a new GameObject.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class CreateComponentExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ObjectFactoryExample/Create Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)")]
    public void CreateCameraEditor()
    {
        Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) = ObjectFactory.CreateGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.CreateGameObject.html)("Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)", typeof(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)));
    }
}

```

* * *
