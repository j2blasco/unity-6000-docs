* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).Find
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html "Go to GameObject Component in the Manual")
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) Find(string name); 
### Parameters
Parameter | Description  
---|---  
name | The name of the GameObject to find.  
### Description
Finds and returns a GameObject with the specified name.
Only returns active GameObjects. Returns `null` if no GameObject with `name` exists. If `name` contains a `/` character, it traverses the hierarchy like a path name.  
  
For performance reasons, it is recommended to not use this function every frame. Instead, cache the result in a member variable at startup, or use [GameObject.FindWithTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html).  
  
If the game is running with multiple scenes then `Find` will search in all of them.  
  
To find a child GameObject, it is often easier to use [Transform.Find](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.Find.html). 
```
using UnityEngine;
using System.Collections;  
  
// This returns the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) named Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html) in one of the Scenes.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hand;  
  
    void Example()
    {
        // This returns the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) named Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html).
        hand = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html)");  
  
        // This returns the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) named Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html).
        // Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html) must not have a parent in the Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Hierarchy.html) view.
        hand = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("/Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html)");  
  
        // This returns the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) named Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html),
        // which is a child of Arm > Monster.
        // Monster must not have a parent in the Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Hierarchy.html) view.
        hand = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("/Monster/Arm/Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html)");  
  
        // This returns the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) named Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html),
        // which is a child of Arm > Monster.
        hand = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("Monster/Arm/Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html)");
    }
}

```

`GameObject.Find` is useful for automatically connecting references to other objects at load time; for example, inside [MonoBehaviour.Awake](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Awake.html) or [MonoBehaviour.Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html).  
  
A common pattern is to assign a GameObject to a variable inside [MonoBehaviour.Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Start.html), and use the variable in [MonoBehaviour.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.Update.html).
```
using UnityEngine;
using System.Collections;  
  
// Find the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) named Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html) and rotate it every frame  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hand;  
  
    void Start()
    {
        hand = GameObject.Find[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.Find.html)("/Monster/Arm/Hand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.Hand.html)");
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        hand.transform.Rotate(0, 100 * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html), 0);
    }
}

```

Additional resources: [GameObject.FindGameObjectsWithTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindGameObjectsWithTag.html)
* * *
