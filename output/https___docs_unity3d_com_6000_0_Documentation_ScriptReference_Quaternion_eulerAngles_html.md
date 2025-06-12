* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-eulerAngles.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).eulerAngles
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html "Go to Quaternion Component in the Manual")
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) eulerAngles; 
### Description
Returns or sets the euler angle representation of the rotation in degrees.
Euler angles can represent a three dimensional rotation by performing three separate rotations around individual axes. In Unity these rotations are performed around the Z axis, the X axis, and the Y axis, in that order.   
  
You can set the rotation of a Quaternion by setting this property, and you can read the Euler angle values by reading this property.   
  
When using the .eulerAngles property to set a rotation, it is important to understand that although you are providing X, Y, and Z rotation values to describe your rotation, those values are not stored in the rotation. Instead, the X, Y & Z values are converted to the Quaternion's internal format.  
  
When you read the .eulerAngles property, Unity converts the Quaternion's internal representation of the rotation to Euler angles. Because, there is more than one way to represent any given rotation using Euler angles, the values you read back out may be quite different from the values you assigned. This can cause confusion if you are trying to gradually increment the values to produce animation. See bottom scripting example for more information.   
  
To avoid these kinds of problems, the recommended way to work with rotations is to avoid relying on consistent results when reading .eulerAngles particularly when attempting to gradually increment a rotation to produce animation. For better ways to achieve this, see the [Quaternion * operator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-operator_multiply.html).   
  
The following example demonstrates the rotation of a GameObject using eulerAngles based on the Input of the user. The example shows that we never rely on reading the Quanternion.eulerAngles to increment the rotation, instead we set it using our Vector3 currentEulerAngles. All rotational changes happen in the currentEulerAngles variable, which are then applied to the Quaternion avoiding the problem mentioned above.
```
using UnityEngine;
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float rotationSpeed = 45;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) currentEulerAngles;
    Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) currentRotation;
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
  
        //moving the value of the Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) into Quanternion.eulerAngle format
        currentRotation.eulerAngles = currentEulerAngles;  
  
        //apply the Quaternion.eulerAngles[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-eulerAngles.html) change to the gameObject
        transform.rotation = currentRotation;
    }  
  
    void OnGUI()
    {
        GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = new GUIStyle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html)();
        style.fontSize = 24;
        // Use eulerAngles to show the euler angles of the quaternion stored in Transform.Rotation
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 0, 0, 0), "Rotating on X:" + x + " Y:" + y + " Z:" + z, style);  
  
        //outputs the Quanternion.eulerAngles value
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 25, 0, 0), "CurrentEulerAngles: " + currentEulerAngles, style);  
  
        //outputs the transform.eulerAngles of the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 50, 0, 0), "GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) World Euler Angles: " + transform.eulerAngles, style);
    }
}

```

The following example demonstrates how the values you read out of .eulerAngles may be quite different from the values you assign, even though they represent the same rotation.
```
using UnityEngine;  
  
// demonstration of eulerAngles not returning the same values as assigned
public class EulerAnglesProblemExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private void Start()
    {
        Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) myRotation = Quaternion.identity[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-identity.html);
        myRotation.eulerAngles = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(150, 35, 45);  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(myRotation.eulerAngles);  
  
        // output is: (30.0, 215.0, 225.0)
    }
}

```

* * *
