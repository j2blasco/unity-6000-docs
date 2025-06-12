* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html

#  [Debug](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.html).Log
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Debug.html "Go to Debug Component in the Manual")
## Declaration
public static void Log(object message); 
## Declaration
public static void Log(object message, [Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) context); 
### Parameters
Parameter | Description  
---|---  
message | String or object to be converted to string representation for display.  
context | Object to which the message applies.  
### Description
Logs a message to the Unity Console.
Use [Debug.Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html) to print informational messages that help you debug your application. For example, you could print a message containing a [GameObject.name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject-name.html) and information about the object’s current state.  
  
You can format messages with string concatenation:  
`Debug.Log("Text: " + myText.text);`  
  
You can also use [Rich Text](https://docs.unity3d.com/6000.0/Documentation/Manual/StyledText.html) markup.  
  
If you pass a [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) or [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) as the optional `context` parameter, Unity momentarily highlights that object in the `Hierarchy` window when you click the log message in the `Console`. Use a `context` object when you have many instances of an object in a Scene so that you can identify which one produced the message. `Example 2`, below, illustrates how this feature works. When you run this example, first click one of the cubes it creates in the Scene. The example prints a log message to the `Console`. When you click on the message, Unity highlights the `context` object in the `Hierarchy` window — in this case, the cube you clicked on in the Scene.  
  
Example 1: Show some uses of [Debug.Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html):
```
using UnityEngine;
using System.Collections;  
  
public class MyGameClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // A Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) used in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and needed by MyGameMethod().
    public Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html) light;  
  
    void MyGameMethod()
    {
        // Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html) with a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) name.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Hello: " + gameObject.name);  
  
        // Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html) with light type. This is an Object example.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(light.type);  
  
        // Message[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Message.html) using rich text.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("<color=red>Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html): </color>AssetBundle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html) not found");
    }
}

```

Example 2: Show selection of a clicked [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html):
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
// Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html) example
//
// Create three cubes. Place them around the world origin.
// If a cube is clicked use Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html) to announce it. Use
// Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html) with two arguments. Argument two allows the
// cube to be automatically selected in the hierarchy when
// the console message is clicked.
//
// Add this script to an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] cubes;  
  
    void Awake()
    {
        // Create three cubes and place them close to the world space center.
        cubes = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[3];
        float f = 25.0f;
        float p = -2.0f;
        float[] z = new float[] {0.5f, 0.0f, 0.5f};  
  
        for (int i = 0; i < 3; i++)
        {
            // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) and rotate each cube.
            cubes[i] = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Cube[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Cube.html));
            cubes[i].name = "Cube" + (i + 1).ToString();
            cubes[i].transform.Rotate(0.0f, f, 0.0f);
            cubes[i].transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(p, 0.0f, z[i]);
            f -= 25.0f;
            p = p + 2.0f;
        }  
  
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) and rotate the camera to view all three cubes.
        Camera.main.transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(3.0f, 1.5f, 3.0f);
        Camera.main.transform.localEulerAngles = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(25.0f, -140.0f, 0.0f);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Process a mouse button click.
        if (Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(0))
        {
            var ray = Camera.main.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html));
            RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;  
  
            if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray, out hit))
            {
                // Visit each cube and determine if it has been clicked.
                for (int i = 0; i < 3; i++)
                {
                    if (hit.collider.gameObject == cubes[i])
                    {
                        // This cube was clicked.
                        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Hit " + cubes[i].name, cubes[i]);
                    }
                }
            }
        }
    }
}

```

Note: Unity also adds [Debug.Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html) messages to the Editor and Player log files. See [Log Files](https://docs.unity3d.com/6000.0/Documentation/Manual/LogFiles.html) for more information about accessing these files on different platforms.  
  
Additional resources: [MonoBehaviour.print](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour-print.html).
* * *
