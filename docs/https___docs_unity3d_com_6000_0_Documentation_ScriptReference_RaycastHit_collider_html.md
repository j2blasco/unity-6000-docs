* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-collider.html

#  [RaycastHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html).collider
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
[Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) collider; 
### Description
The [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) that was hit.
This property is null if the ray hit nothing and not-null if it hit a Collider.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        if (Input.GetMouseButtonDown[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.GetMouseButtonDown.html)(0))
        {
            RaycastHit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html) hit;
            Ray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray = Camera.main.ScreenPointToRay(Input.mousePosition[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePosition.html));  
  
            if (Physics.Raycast[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html)(ray, out hit))
            {
                if (hit.collider != null)
                {
                    hit.collider.enabled = false;
                }
            }
        }
    }
}

```

Additional resources: [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Physics.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Linecast.html), [Physics.RaycastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html).
* * *
