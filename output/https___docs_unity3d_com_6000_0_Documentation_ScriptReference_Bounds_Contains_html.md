* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Contains.html

#  [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).Contains
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
public bool Contains([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point); 
### Description
Is `point` contained in the bounding box?
If the `point` passed into [Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Contains.html) is inside the bounding box a value of True is returned. Points on the min and max limits (corners and edges) of the bounding box are considered inside.  
  
**Note:** If [Bounds.extents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-extents.html) contains a negative value in any coordinate then [Bounds.Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Contains.html) will always return False.
```
//Attach this script to a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) with a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component
//Create an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (**Create**>**Create Empty**) and attach it in the New Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) field in the Inspector of the first GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
//This script tells if a point  you specify (the position of the empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)) is within the first GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)’s Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    //Make sure to assign this in the Inspector window
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) m_NewTransform;
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_Collider;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Point;  
  
    void Start()
    {
        //Fetch the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) this script is attached to
        m_Collider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
        //Assign the point to be that of the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) you assign in the Inspector window
        m_Point = m_NewTransform.position;
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //If the first GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) contains the Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)'s position, output a message in the console
        if (m_Collider.bounds.Contains(m_Point))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) contain the point : " + m_Point);
        }
    }
}

```

* * *
