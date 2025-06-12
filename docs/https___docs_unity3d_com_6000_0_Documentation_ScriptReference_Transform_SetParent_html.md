* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.SetParent.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).SetParent
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html "Go to Transform Component in the Manual")
## Declaration
public void SetParent([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) p); 
## Declaration
public void SetParent([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent, bool worldPositionStays); 
### Parameters
Parameter | Description  
---|---  
parent | The parent Transform to use.  
worldPositionStays | If true, the parent-relative position, scale and rotation are modified such that the object keeps the same world space position, rotation and scale as before.  
### Description
Set the parent of the transform.
This method is the same as the [parent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-parent.html) property except that it also lets the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) keep its local orientation rather than its global orientation. This means for example, if the GameObject was previously next to its parent, setting `worldPositionStays` to false will move the GameObject to be positioned next to its new parent in the same way.  
  
The default value of `worldPositionStays` argument is true.  
  
The following images are of a scene with three GameObjects: a new parent cube, a parent sphere, and a child sphere.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/TransformSetParentOriginal.png)  
  
The new parent cube is on the left of the screen and the child sphere is in its original position, next to the parent sphere on the right of the screen.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/TransformSetParentWorldTrue.png)  
  
After calling `SetParent` with `worldPositionStays` set to true, all objects are in the same position as their original positions.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/TransformSetParentWorldFalse.png)  
  
After calling `SetParent` with `worldPositionStays` set to false, the child sphere is in the same position but is now relative to the new parent cube instead.  
  

```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) child;  
  
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) parent;  
  
    //Invoked when a button is clicked.
    public void Example(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) newParent)
    {
        // Sets "newParent" as the new parent of the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
        child.transform.SetParent(newParent);  
  
        // Same as above, except worldPositionStays set to false
        // makes the child keep its local orientation rather than
        // its global orientation.
        child.transform.SetParent(newParent, false);  
  
        // Setting the parent to ‘null’ unparents the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        // and turns child into a top-level object in the hierarchy
        child.transform.SetParent(null);
    }
}

```

* * *
