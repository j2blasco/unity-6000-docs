* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-ctor.html

# GameObject Constructor
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
## Declaration
public GameObject(); 
## Declaration
public GameObject(string name); 
## Declaration
public GameObject(string name, params Type[] components); 
### Parameters
Parameter | Description  
---|---  
name | The name of the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html), specified as a string. The name is stored in the [name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) property of the GameObject.  
components | The components to attach, specified as an array of types that inherit from `Component`.  
### Description
Creates a new GameObject, with optional parameters to specify a name and set of components to attach.
Use the constructor with no arguments to create a GameObject with an empty `name` property and only a `Transform` component attached.  
  
Use the constructor with `name` parameter to create a GameObject with the specified value as the name property and only a `Transform` component attached.  
  
Use the constructor with `name` and `components` parameters to create a GameObject with the specified name and the specified components attached, in addition to the `Transform` component. 
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exampleOne = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)();
        exampleOne.name = "GameObject1";
        exampleOne.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exampleTwo = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("GameObject2");
        exampleTwo.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exampleThree = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("GameObject3", typeof(Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)), typeof(BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)));
    }
}

```

* * *
