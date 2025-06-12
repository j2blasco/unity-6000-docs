* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion-w.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).w
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
w; 
### Description
W component of the Quaternion. Do not directly modify quaternions.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html)-w script example
// Create a Sphere and apply a texture to help the orientation be recognised.
// At each second the sphere is rotated and the quaternion is displayed.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float timeDelay = 0.0f;
    private Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) q;
    private string label = "";  
  
    void Awake()
    {
        // Add a line that passes through the y axis of the sphere and make
        // the line as a child.
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) line = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
        line.transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.05f, 1.5f, 0.05f);
        line.transform.parent = gameObject.transform;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (timeDelay > 1.0f)
        {
            Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) v;  
  
            // generate a random euler angle
            v.x = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.0f, 360.0f);
            v.y = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.0f, 360.0f);
            v.z = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0.0f, 360.0f);  
  
            // convert the euler into a quaternion
            q = Quaternion.Euler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Euler.html)(v);  
  
            // and apply it to the sphere
            transform.rotation = q;  
  
            // generate a string
            label = q.ToString("f3");  
  
            // and start another 1 second delay
            timeDelay = 0.0f;
        }
        timeDelay += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }  
  
    // display the quaternion as a string
    void OnGUI()
    {
        GUI.skin.label.fixedHeight = 40;
        GUI.skin.label.fontSize = 24;
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(10, 10, 400, 30), label);
    }
}

```

* * *
