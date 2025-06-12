* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html

#  [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).FindWithTag
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) FindWithTag(string tag); 
### Parameters
Parameter | Description  
---|---  
tag | The tag to search for.  
### Description
Retrieves the first active [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) tagged with the specified tag. Returns null if no GameObject has the tag.
Tags must be declared in the tag manager before using them. A `UnityException` is thrown if the tag does not exist or if an empty string or `null` is supplied as the `tag` parameter.  
  
**Note:** This method returns the first GameObject it finds with the specified tag. If a scene contains multiple active GameObjects with the specified tag, there is no guarantee this method will return a specific GameObject.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) respawnPrefab;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) respawn;
    void Start()
    {
        if (respawn == null)
            respawn = GameObject.FindWithTag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.FindWithTag.html)("Respawn");  
  
        Instantiate(respawnPrefab, respawn.transform.position, respawn.transform.rotation);
    }
}

```

* * *
