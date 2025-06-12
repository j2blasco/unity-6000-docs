* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-size.html

#  [Bounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html).size
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) size; 
### Description
The total size of the box. This is always twice as large as the [extents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds-extents.html).
_size.x_ is the width, _size.y_ is the height and _size.z_ is the depth of the box. Note that _size_ is given in world size. A Bound surrounding a tall human might have _size.y_ approximately 2.0f, meaning a 2 meter height body.
```
//This script outputs the size of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) bounds to the console  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) m_Collider;
    Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_Size;  
  
    void Start()
    {
        //Fetch the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        m_Collider = GetComponent<Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)>();  
  
        //Fetch the size of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) volume
        m_Size = m_Collider.bounds.size;  
  
        //Output to the console the size of the Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) volume
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) Size : " + m_Size);
    }
}

```

* * *
