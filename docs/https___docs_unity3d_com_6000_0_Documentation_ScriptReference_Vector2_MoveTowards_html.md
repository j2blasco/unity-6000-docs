* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.MoveTowards.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).MoveTowards
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) MoveTowards([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) current, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) target, float maxDistanceDelta); 
### Description
Moves a point `current` towards `target`.
This is essentially the same as [Vector2.Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Lerp.html) but instead the function will ensure that the distance never exceeds `maxDistanceDelta`. Negative values of `maxDistanceDelta` pushes the vector away from `target`.
```
using UnityEngine;  
  
// 2D MoveTowards example
// Move the sprite to where the mouse is clicked
//
// Set speed to -1.0f and the sprite will move
// away from the mouse click position forever  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private float speed = 10.0f;
    private Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) target;
    private Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position;
    private Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) cam;  
  
    void Start()
    {
        target = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0.0f, 0.0f);
        position = gameObject.transform.position;  
  
        cam = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float step = speed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // move sprite towards the target location
        transform.position = Vector2.MoveTowards[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.MoveTowards.html)(transform.position, target, step);
    }  
  
    void OnGUI()
    {
        Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) currentEvent = Event.current[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-current.html);
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) mousePos = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)();
        Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)();  
  
        // compute where the mouse is in world space
        mousePos.x = currentEvent.mousePosition.x;
        mousePos.y = cam.pixelHeight - currentEvent.mousePosition.y;
        point = cam.ScreenToWorldPoint(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(mousePos.x, mousePos.y, 0.0f));  
  
        if (Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(0))
        {
            // set the target to the mouse click location
            target = point;
        }
    }
}

```

* * *
