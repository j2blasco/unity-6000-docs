* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localScale.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).localScale
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localScale; 
### Description
The scale of the transform relative to the GameObjects parent.
The example below creates a sphere [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a scale of (1,1,1). The application then changes the [Transform.localScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-localScale.html) from 1.0 down to 0.25 and back to 1.0 repeatedly.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) sphere;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scaleChange, positionChange;  
  
    void Awake()
    {
        Camera.main.clearFlags = CameraClearFlags.SolidColor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CameraClearFlags.SolidColor.html);  
  
        // Create a sphere at the origin.
        sphere = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Sphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Sphere.html));
        sphere.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0);  
  
        // Create a plane and move down by 0.5.
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) plane = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
        plane.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, -0.5f, 0);  
  
        // Change the floor color to blue.
        // The blue material is present in Resources[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html) and not created in this script.
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = plane.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();
        rend.material = Resources.Load[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.Load.html)<Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)>("blue");  
  
        scaleChange = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-0.01f, -0.01f, -0.01f);
        positionChange = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, -0.005f, 0.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        sphere.transform.localScale += scaleChange;
        sphere.transform.position += positionChange;  
  
        // Move upwards when the sphere hits the floor or downwards
        // when the sphere scale extends 1.0f.
        if (sphere.transform.localScale.y < 0.1f || sphere.transform.localScale.y > 1.0f)
        {
            scaleChange = -scaleChange;
            positionChange = -positionChange;
        }
    }
}

```

* * *
