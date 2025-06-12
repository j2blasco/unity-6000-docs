* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ProjectOnPlane.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).ProjectOnPlane
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ProjectOnPlane([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vector, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) planeNormal); 
### Parameters
Parameter | Description  
---|---  
vector | The vector to project on the plane.  
planeNormal | The normal which defines the plane to project on.  
### Returns
**Vector3** The orthogonal projection of `vector` on the plane. 
### Description
Projects a vector onto a plane.
For a given plane described by `planeNormal` and a given vector `vector`, [Vector3.ProjectOnPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ProjectOnPlane.html) generates a new vector orthogonal to `planeNormal` and parallel to the plane. Note: `planeNormal` does not need to be normalized.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/Vector3ProjectOnPlane.png)  
''The red line represents `vector`, the yellow line represents `planeNormal`, and the blue line represents the projection of `vector` on the plane.''  
  
The script example below makes `Update` generate a `vector` position, and a `planeNormal` normal. The [Vector3.ProjectOnPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ProjectOnPlane.html) static method receives the arguments and returns the [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position.
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Vector3.ProjectOnPlane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ProjectOnPlane.html) - example  
  
// Generate a random plane in xy. Show the position of a random
// vector and a connection to the plane. The example shows nothing
// in the Game view but uses Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)(). The script reference example
// uses Gizmos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html) to show the positions and axes in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html).  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) vector, planeNormal;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) response;
    private float radians;
    private float degrees;
    private float timer = 12345.0f;  
  
    // Generate the values for all the examples.
    // Change the example every two seconds.
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (timer > 2.0f)
        {
            // Generate a position inside xy space.
            vector = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-1.0f, 1.0f), Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-1.0f, 1.0f), 0.0f);  
  
            // Compute a normal from the plane through the origin.
            degrees = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(-45.0f, 45.0f);
            radians = degrees * Mathf.Deg2Rad[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Deg2Rad.html);
            planeNormal = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(radians), Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(radians), 0.0f);  
  
            // Obtain the ProjectOnPlane result.
            response = Vector3.ProjectOnPlane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.ProjectOnPlane.html)(vector, planeNormal);  
  
            // Reset the timer.
            timer = 0.0f;
        }
        timer += Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }  
  
    // Show a Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) view example.
    void OnDrawGizmosSelected()
    {
        // Left/right and up/down axes.
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);
        Gizmos.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html)(transform.position - new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(2.25f, 0, 0), transform.position + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(2.25f, 0, 0));
        Gizmos.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html)(transform.position - new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1.75f, 0), transform.position + new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 1.75f, 0));  
  
        // Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) the plane.
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) angle = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-1.75f * Mathf.Sin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Sin.html)(radians), 1.75f * Mathf.Cos[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Cos.html)(radians), 0.0f);
        Gizmos.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html)(transform.position - angle, transform.position + angle);  
  
        // Show the projection on the plane as a blue line.
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
        Gizmos.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), response);
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(response, 0.05f);  
  
        // Show the vector perpendicular to the plane in yellow
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        Gizmos.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html)(vector, response);  
  
        // Now show the input position.
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(vector, 0.05f);
        Gizmos.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html)(Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html), vector);
    }
}

```

* * *
