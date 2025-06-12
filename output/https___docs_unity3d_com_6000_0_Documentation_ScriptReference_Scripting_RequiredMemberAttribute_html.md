* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Scripting.RequiredMemberAttribute.html

# RequiredMemberAttribute
class in UnityEngine.Scripting
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
When a type is marked, all of its members with [RequiredMember] are marked.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.Scripting;  
  
public class NewBehaviourScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        new UsedFoo();
    }
}  
  
class UsedFoo
{
    // Will survive managed code stripping because UsedFoo is used
    [RequiredMember]
    public int Field;  
  
    // Will survive managed code stripping because UsedFoo is used
    [RequiredMember]
    public void Method()
    {
    }  
  
    // The property, property getter method, and property setter method will survive managed code stripping because UsedFoo is used
    [RequiredMember]
    public int Property1 { get; set; }  
  
    // The property and property getter method will survive managed code stripping because UsedFoo is used
    public int Property2 { [RequiredMember] get; set; }  
  
    // The property and property setter method will survive managed code stripping because UsedFoo is used
    public int Property3 { get; [RequiredMember] set; }  
  
    // The event, the add method, and the remove method will survive managed code stripping because UsedFoo is used
    [RequiredMember]
    public event EventHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html) Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html);
}  
  
class UnusedFoo
{
    // Will not survive stripping because UnusedFoo is not used
    [RequiredMember]
    public int Field;  
  
    // Will not survive stripping because UnusedFoo is not used
    [RequiredMember]
    public void Method()
    {
    }  
  
    // Will not survive stripping because UnusedFoo is not used
    [RequiredMember]
    public int Property { get; set; }  
  
    // Will not survive stripping because UnusedFoo is not used
    [RequiredMember]
    public event EventHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.EventHandler.html) Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html);
}

```

* * *
