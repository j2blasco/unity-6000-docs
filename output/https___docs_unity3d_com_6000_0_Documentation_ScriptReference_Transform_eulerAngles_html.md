* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-eulerAngles.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).eulerAngles
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) eulerAngles; 
### Description
The rotation as Euler angles in degrees.
[Transform.eulerAngles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-eulerAngles.html) represents rotation in world space. When viewing the rotation of a GameObject in the Inspector, you may see different angle values from those stored in this property. This is because the Inspector displays local rotation, for more information see [Transform.localEulerAngles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localEulerAngles.html).   
  
Euler angles can represent a three dimensional rotation by performing three separate rotations around individual axes. In Unity these rotations are performed around the Z axis, the X axis, and the Y axis, in that order.   
  
You can set the rotation of a Quaternion by setting this property, and you can read the Euler angle values by reading this property.   
  
When using the .eulerAngles property to set a rotation, it is important to understand that although you are providing X, Y, and Z rotation values to describe your rotation, those values are not stored in the rotation. Instead, the X, Y & Z values are converted to the Quaternion's internal format.  
  
When you read the .eulerAngles property, Unity converts the Quaternion's internal representation of the rotation to Euler angles. Because, there is more than one way to represent any given rotation using Euler angles, the values you read back out may be quite different from the values you assigned. This can cause confusion if you are trying to gradually increment the values to produce animation.   
  
To avoid these kinds of problems, the recommended way to work with rotations is to avoid relying on consistent results when reading .eulerAngles particularly when attempting to gradually increment a rotation to produce animation. For better ways to achieve this, see the [Quaternion * operator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-operator_multiply.html).   
  
The following example demonstrates the rotation of a GameObject using eulerAngles based on the Input of the user. The example shows that we never rely on reading the Quanternion.eulerAngles to increment the rotation, instead we set it using our Vector3 currentEulerAngles. All rotational changes happen in the currentEulerAngles variable, which are then applied to the Quaternion avoiding the problem mentioned above.
```
using UnityEngine;
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float rotationSpeed = 45;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) currentEulerAngles;
    float x;
    float y;
    float z;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.X[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.X.html))) x = 1 - x;
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Y[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Y.html))) y = 1 - y;
        if (Input.GetKeyDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetKeyDown.html)(KeyCode.Z[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.Z.html))) z = 1 - z;  
  
        //modifying the Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html), based on input multiplied by speed and time
        currentEulerAngles += new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(x, y, z) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html) * rotationSpeed;  
  
        //apply the change to the gameObject
        transform.eulerAngles = currentEulerAngles;
    }  
  
    void OnGUI()
    {
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)();
        style.fontSize = 24;
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 0, 0, 0), "Rotating on X:" + x + " Y:" + y + " Z:" + z, style);  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 25, 0, 0), "Transform.eulerAngle: " + transform.eulerAngles, style);
    }
}

```

Do not set one of the eulerAngles axis separately (eg. eulerAngles.x = 10; ) since this will lead to drift and undesired rotations. When setting them to a new value set them all at once as shown above. Unity will convert the angles to and from the rotation stored in [Transform.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-rotation.html).
* * *
