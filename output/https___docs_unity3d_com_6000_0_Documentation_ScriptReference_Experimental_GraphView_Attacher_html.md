* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# Attacher
class in UnityEditor.Experimental.GraphView
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
Helper object that attaches a visual element next to its target, regarless of their respective location in the visual tree hierarchy.
The Attacher will monitor the position of the target and move the attached element accordingly.
### Properties
Property | Description  
---|---  
[alignment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher-alignment.html) | Relative alignment between the attached element and the target.  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher-distance.html) | The distance between the attached element and the target.  
[element](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher-element.html) | The element that is attached to the target element.  
[offset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher-offset.html) | An absolute offset added to the element position after placement.  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher-target.html) | The target element.  
### Constructors
Constructor | Description  
---|---  
[Attacher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher-ctor.html) | Attaches a visual element next to its target, regarless of their respective locations in the visual tree hierarchy.  
### Public Methods
Method | Description  
---|---  
[Detach](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher.Detach.html) | Stop monitoring the target element and postioning the attached element.  
[Reattach](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Attacher.Reattach.html) | Starts monitoring target element position changes and places the attached element accordingly.  
* * *
