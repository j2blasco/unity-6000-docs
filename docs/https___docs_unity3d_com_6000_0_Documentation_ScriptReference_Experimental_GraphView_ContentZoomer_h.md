* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.html

**Experimental** : this API is experimental and might be changed or removed in the future.
# ContentZoomer
class in UnityEditor.Experimental.GraphView
/
Inherits from:[UIElements.Manipulator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator.html)
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
Manipulator that allows zooming in GraphView.
### Static Properties
Property | Description  
---|---  
[DefaultMaxScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.DefaultMaxScale.html) | Default max zoom level.  
[DefaultMinScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.DefaultMinScale.html) | Default min zoom level.  
[DefaultReferenceScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.DefaultReferenceScale.html) | Default reference zoom level.  
[DefaultScaleStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.DefaultScaleStep.html) | Default zoom step.  
### Properties
Property | Description  
---|---  
[maxScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer-maxScale.html) | Max zoom level.  
[minScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer-minScale.html) | Min zoom level.  
[referenceScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer-referenceScale.html) | Reference zoom level.  
[scaleStep](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer-scaleStep.html) | Zoom step: percentage of variation between a zoom level and the next. For example, with a value of 0.15, which represents 15%, a zoom level of 200% will become 230% when zooming in.  
### Constructors
Constructor | Description  
---|---  
[ContentZoomer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer-ctor.html) | ContentZoomer constructor.  
### Protected Methods
Method | Description  
---|---  
[RegisterCallbacksOnTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.RegisterCallbacksOnTarget.html) | Called to register click event callbacks on the target element.  
[UnregisterCallbacksFromTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.ContentZoomer.UnregisterCallbacksFromTarget.html) | Called to unregister event callbacks from the target element.  
### Inherited Members
### Properties
Property | Description  
---|---  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Manipulator-target.html) |  VisualElement being manipulated.   
* * *
