* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).position
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position; 
### Description
The world space position of the Transform.
The [position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-position.html) property of a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html), which is accessible in the Unity Editor and through scripts. Alter this value to move a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Get this value to locate the [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in 3D world space.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //movement speed in units per second
    private float movementSpeed = 5f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //get the Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) from Horizontal axis
        float horizontalInput = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal");
        //get the Input[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html) from Vertical axis
        float verticalInput = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical");  
  
        //update the position
        transform.position = transform.position + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(horizontalInput * movementSpeed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), verticalInput * movementSpeed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), 0);  
  
        //output to log the position change
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(transform.position);
    }
}

```

The example gets the Input from Horizontal and Vertical axes, and moves the GameObject up/down or left/right by changing its position.
* * *
