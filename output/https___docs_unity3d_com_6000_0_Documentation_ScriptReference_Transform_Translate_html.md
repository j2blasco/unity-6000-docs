* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Translate.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).Translate
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
public void Translate([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) translation); 
## Declaration
public void Translate([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) translation, [Space](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) relativeTo = Space.Self); 
### Description
Moves the transform in the direction and distance of `translation`.
If `relativeTo` is left out or set to [Space.Self](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html) the movement is applied relative to the transform's local axes. (the x, y and z axes shown when selecting the object inside the Scene View.) If `relativeTo` is [Space.World](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html) the movement is applied relative to the world coordinate system.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Move the object forward along its z axis 1 unit/second.
        transform.Translate(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));  
  
        // Move the object upward in world space 1 unit/second.
        transform.Translate(Vector3.up[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-up.html) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
    }
}

```

* * *
## Declaration
public void Translate(float x, float y, float z); 
## Declaration
public void Translate(float x, float y, float z, [Space](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.html) relativeTo = Space.Self); 
### Description
Moves the transform by `x` along the x axis, `y` along the y axis, and `z` along the z axis.
If `relativeTo` is left out or set to [Space.Self](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.Self.html) the movement is applied relative to the transform's local axes. (the x, y and z axes shown when selecting the object inside the Scene View.) If `relativeTo` is [Space.World](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html) the movement is applied relative to the world coordinate system.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Move the object forward along its z axis 1 unit/second.
        transform.Translate(0, 0, Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));  
  
        // Move the object upward in world space 1 unit/second.
        transform.Translate(0, Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), 0, Space.World[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Space.World.html));
    }
}

```

* * *
## Declaration
public void Translate([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) translation, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) relativeTo); 
### Description
Moves the transform in the direction and distance of `translation`.
The movement is applied relative to `relativeTo`'s local coordinate system. If `relativeTo` is null, the movement is applied relative to the world coordinate system.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Move the object to the right relative to the camera 1 unit/second.
        transform.Translate(Vector3.right[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-right.html) * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), Camera.main.transform);
    }
}

```

* * *
## Declaration
public void Translate(float x, float y, float z, [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) relativeTo); 
### Description
Moves the transform by `x` along the x axis, `y` along the y axis, and `z` along the z axis.
The movement is applied relative to `relativeTo`'s local coordinate system. If `relativeTo` is null, the movement is applied relative to the world coordinate system.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Move the object to the right relative to the camera 1 unit/second.
        transform.Translate(Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), 0, 0, Camera.main.transform);
    }
}

```

* * *
