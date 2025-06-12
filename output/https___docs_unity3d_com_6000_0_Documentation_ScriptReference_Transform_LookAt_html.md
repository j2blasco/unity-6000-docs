* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.LookAt.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).LookAt
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
public void LookAt([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target); 
## Declaration
public void LookAt([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) worldUp = Vector3.up); 
### Parameters
Parameter | Description  
---|---  
target | Object to point towards.  
worldUp | Vector specifying the upward direction.  
### Description
Rotates the transform so the forward vector points at /target/'s current position.
Then it rotates the transform to point its up direction vector in the direction determined by the `worldUp` parameter. If you leave out the `worldUp` parameter, the function will use the world y axis. The up vector of the rotation will only match the `worldUp` vector if the forward direction is perpendicular to `worldUp`.
```
using UnityEngine;
// This complete script can be attached to a camera to make it
// continuously point at another object.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) the camera every frame so it keeps looking at the target
        transform.LookAt(target);  
  
        // Same as above, but setting the worldUp parameter to Vector3.left[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-left.html) in this example turns the camera on its side
        transform.LookAt(target, Vector3.left[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-left.html));
    }
}

```

* * *
## Declaration
public void LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) worldPosition); 
## Declaration
public void LookAt([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) worldPosition, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) worldUp = Vector3.up); 
### Parameters
Parameter | Description  
---|---  
worldPosition | Point to look at.  
worldUp | Vector specifying the upward direction.  
### Description
Rotates the transform so the forward vector points at `worldPosition`.
Then it rotates the transform to point its up direction vector in the direction hinted at by the `worldUp` vector. If you leave out the `worldUp` parameter, the function will use the world y axis. The up vector of the rotation will only match the `worldUp` vector if the forward direction is perpendicular to `worldUp`.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Point the object at the world origin (0,0,0)
        transform.LookAt(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html));
    }
}

```

* * *
