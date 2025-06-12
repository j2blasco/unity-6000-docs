* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html

#  [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html).CompareTag
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
public bool CompareTag(string tag); 
### Parameters
Parameter | Description  
---|---  
tag | The tag to compare.  
### Returns
**bool** Returns true if GameObject has same tag. Returns false otherwise. 
### Description
Checks the GameObject's tag against the defined `tag`.
```
// Immediate death trigger.
// Destroys any colliders that enter the trigger, if they are tagged player.  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        if (other.CompareTag("Player"))
        {
            Destroy(other.gameObject);
        }
    }
}

```

* * *
## Declaration
public bool CompareTag([TagHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.html) tag); 
### Parameters
Parameter | Description  
---|---  
tag | A TagHandle representing the tag to compare.  
### Returns
**bool** Returns true if GameObject has same tag. Returns false otherwise. 
### Description
Checks the GameObject's tag against the defined `tag`.
This overload of the method, which takes a [TagHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.html), can be faster than the overload which takes a string, particularly if the same TagHandle can be reused for many calls.
```
// Immediate death trigger.
// Destroys any colliders that enter the trigger, if they are tagged "Player".  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    private TagHandle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.html) _playerTag;
    public void OnEnable()
    {
        _playerTag = TagHandle.GetExistingTag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.GetExistingTag.html)("Player");
    }  
  
    void OnTriggerEnter(Collider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) other)
    {
        if (other.CompareTag(_playerTag))
        {
            Destroy(other.gameObject);
        }
    }
}
```

* * *
