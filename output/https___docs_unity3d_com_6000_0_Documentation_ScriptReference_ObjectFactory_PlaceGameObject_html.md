* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.PlaceGameObject.html

#  [ObjectFactory](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.html).PlaceGameObject
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
public static void PlaceGameObject([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) parent); 
### Parameters
Parameter | Description  
---|---  
go | The GameObject to be initialized.  
parent | An optional GameObject to be set as the parent.  
### Description
Place the given GameObject in the Scene View using the same preferences as built-in Unity GameObjects.
Use this method to create GameObjects centered in the Scene View or at world origin, depending on user preference. This method also ensures that the GameObject has a unique name, also as defined by preferences.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Creates a new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with the same preferences that built-in GameObjects instantiate with.
class CreateGameObjectExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/3D Object/My Cube")]
    static void CreateCube(MenuCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) command)
    {
        var gameObject = ObjectFactory.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        ObjectFactory.PlaceGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectFactory.PlaceGameObject.html)(gameObject, command.context as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html));
    }
}

```

* * *
