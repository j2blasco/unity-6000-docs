* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetAxis
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
public static float GetAxis(string axisName); 
### Description
Returns the value of the virtual axis identified by `axisName`.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
The value will be in the range -1...1 for keyboard and joystick input devices.  
  
The meaning of this value depends on the type of input control, for example with a joystick's horizontal axis a value of 1 means the stick is pushed all the way to the right and a value of -1 means it's all the way to the left; a value of 0 means the joystick is in its neutral position.  
  
If the axis is mapped to the mouse, the value is different and will not be in the range of -1...1. Instead it'll be the current mouse delta multiplied by the axis sensitivity. Typically a positive value means the mouse is moving right/down and a negative value means the mouse is moving left/up.  
  
This is frame-rate independent; you do not need to be concerned about varying frame-rates when using this value.  
  
To set up your input or view the options for `axisName`, go to **Edit** > **Project Settings** > **Input Manager**. This brings up the Input Manager. Expand **Axis** to see the list of your current inputs. You can use one of these as the `axisName`. To rename the input or change the positive button etc., expand one of the options, and change the name in the **Name** field or **Positive Button** field. Also, change the **Type** to **Joystick Axis**. To add a new input, add 1 to the number in the **Size** field.
```
using UnityEngine;
using System.Collections;  
  
// A very simplistic car driving on the x-z plane.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float speed = 10.0f;
    public float rotationSpeed = 100.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Get the horizontal and vertical axis.
        // By default they are mapped to the arrow keys.
        // The value is in the range -1 to 1
        float translation = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Vertical") * speed;
        float rotation = Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Horizontal") * rotationSpeed;  
  
        // Make it move 10 meters per second instead of 10 meters per frame...
        translation *= Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
        rotation *= Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // Move translation along the object's z-axis
        transform.Translate(0, 0, translation);  
  
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) around our y-axis
        transform.Rotate(0, rotation, 0);
    }
}

```

```
using UnityEngine;
using System.Collections;  
  
// Performs a mouse look.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float horizontalSpeed = 2.0f;
    float verticalSpeed = 2.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Get the mouse delta. This is not in the range -1...1
        float h = horizontalSpeed * Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Mouse X");
        float v = verticalSpeed * Input.GetAxis[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxis.html)("Mouse Y");  
  
        transform.Rotate(v, h, 0);
    }
}

```

**Note:** The Horizontal and Vertical ranges change from 0 to +1 or -1 with increase/decrease in 0.05f steps. [GetAxisRaw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetAxisRaw.html) has changes from 0 to 1 or -1 immediately, so with no steps.
* * *
