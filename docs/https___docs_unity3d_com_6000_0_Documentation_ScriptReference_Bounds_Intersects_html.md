* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.Intersects.html

#  [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).Intersects
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
public bool Intersects([Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds); 
### Description
Does another bounding box intersect with this bounding box?
Check if the bounding box comes into contact with another bounding box. This returns a Boolean that is set to true if there is an intersection between bounds. Two bounds are intersecting if there is at least one point which is contained by both bounds.
```
//Attach this script to an empty GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html). Create 2 more GameObjects and attach a Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) component on each. Choose these as the "My Object" and "New Object" in the Inspector.
//This script allows you to move your main GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) left to right. If it intersects with the other, it outputs the message to the Console.  
  
using UnityEngine;  
  
public class BoundsIntersectExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_MyObject, m_NewObject;
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_Collider, m_Collider2;  
  
    void Start()
    {
        //Check that the first GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exists in the Inspector and fetch the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)
        if (m_MyObject != null)
            m_Collider = m_MyObject.GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();  
  
        //Check that the second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) exists in the Inspector and fetch the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)
        if (m_NewObject != null)
            m_Collider2 = m_NewObject.GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        //If the first GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) enters the second GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html), output the message
        if (m_Collider.bounds.Intersects(m_Collider2.bounds))
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) intersecting");
        }
    }
}

```

* * *
