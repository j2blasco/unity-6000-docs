* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).GetTouch
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
public static [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) GetTouch(int index); 
### Parameters
Parameter | Description  
---|---  
index | The touch input on the device screen.  
### Returns
**Touch** Touch details in the struct. 
### Description
Call [Input.GetTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html) to obtain a [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) struct.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
[Input.GetTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html) returns [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) for a selected screen touch (for example, from a finger or stylus). [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) describes the screen touch. The [index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-index.html) argument selects the screen touch.  
  
[Input.touchCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html) provides the current number of screen touches. If [Input.touchCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html) is greater than zero, the [GetTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html) [index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-index.html) sets which screen touch to check. [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) returns a `struct` with the screen touch details. Each extra screen touch uses an increasing [Input.touchCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html).  
  
[GetTouch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html) returns a [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) struct. Use zero to obtain the first screen touch. As an example, [Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) includes [position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-position.html) in pixels.  
  
No temporary variables are allocated.
```
using UnityEngine;
using System.Collections;
using UnityEngine.iOS;  
  
// Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html) example.
//
// Attach to an origin based cube.
// A screen touch moves the cube on an iPhone or iPad.
// A second screen touch reduces the cube size.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position;
    private float width;
    private float height;  
  
    void Awake()
    {
        width = (float)Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 2.0f;
        height = (float)Screen.height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-height.html) / 2.0f;  
  
        // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) used for the cube.
        position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.0f, 0.0f, 0.0f);
    }  
  
    void OnGUI()
    {
        // Compute a fontSize based on the size of the screen width.
        GUI.skin.label.fontSize = (int)(Screen.width[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Screen-width.html) / 25.0f);  
  
        GUI.Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Label.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(20, 20, width, height * 0.25f),
            "x = " + position.x.ToString("f2") +
            ", y = " + position.y.ToString("f2"));
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Handle screen touches.
        if (Input.touchCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html) > 0)
        {
            Touch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) touch = Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(0);  
  
            // Move the cube if the screen has the finger moving.
            if (touch.phase == TouchPhase.Moved[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Moved.html))
            {
                Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) pos = touch.position;
                pos.x = (pos.x - width) / width;
                pos.y = (pos.y - height) / height;
                position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(-pos.x, pos.y, 0.0f);  
  
                // Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) the cube.
                transform.position = position;
            }  
  
            if (Input.touchCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html) == 2)
            {
                touch = Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(1);  
  
                if (touch.phase == TouchPhase.Began[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Began.html))
                {
                    // Halve the size of the cube.
                    transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0.75f, 0.75f, 0.75f);
                }  
  
                if (touch.phase == TouchPhase.Ended[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Ended.html))
                {
                    // Restore the regular size of the cube.
                    transform.localScale = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(1.0f, 1.0f, 1.0f);
                }
            }
        }
    }
}

```

A second example:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) projectile;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) clone;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        for (int i = 0; i < Input.touchCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html); ++i)
        {
            if (Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(i).phase == TouchPhase.Began[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Began.html))
            {
                clone = Instantiate(projectile, transform.position, transform.rotation) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
            }
        }
    }
}

```

A third example:
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) particle;
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        for (int i = 0; i < Input.touchCount[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-touchCount.html); ++i)
        {
            if (Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(i).phase == TouchPhase.Began[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TouchPhase.Began.html))
            {
                // Construct a ray from the current touch coordinates
                Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = Camera.main.ScreenPointToRay(Input.GetTouch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetTouch.html)(i).position);  
  
                // Create a particle if hit
                if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray))
                {
                    Instantiate(particle, transform.position, transform.rotation);
                }
            }
        }
    }
}

```

* * *
