* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform-childCount.html

#  [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html).childCount
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
childCount; 
### Description
The number of children the parent Transform has.
**Note:** The parent is not included in the count.  
**Note:** Inactive GameObjects get included in the count.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // generate a group of connected GameObjects
    void Awake()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("top");  
  
        Random.InitState[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.InitState.html)(System.Environment.TickCount);  
  
        // add 3, 4 or 5 "middle" children that report to "top"
        for (int i = 0; i < Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(3, 6); i++)
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go2 = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("middle" + i.ToString());
            go2.transform.parent = go.transform;  
  
            // add between 1 to 8 "bottom" children that report to the above "middle"
            for (int j = 0; j < Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(1, 8); j++)
            {
                GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go3 = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("bottom" + j);
                go3.transform.parent = go2.transform;
            }
        }
    }  
  
    void Start()
    {
        // how many children does top have?
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("top");
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(go.name + " has " + go.transform.childCount + " children");  
  
        // pick a random middle group and pick a member of its children
        go = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("middle" + Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, go.transform.childCount));
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(go.name + " has " + go.transform.childCount + " children");
    }
}

```

* * *
