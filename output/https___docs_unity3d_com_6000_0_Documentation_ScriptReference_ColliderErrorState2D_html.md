* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderErrorState2D.html

# ColliderErrorState2D
enumeration
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
Indicates what (if any) error was encountered when creating a 2D Collider.
This error state can be read directly from the 2D Collider via the property: [Collider2D.errorState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-errorState.html).
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderErrorState2D.None.html) | Indicates that no error was encountered, therefore the 2D Collider was created successfully.  
[NoShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderErrorState2D.NoShapes.html) | Indicates that no physics shapes were created by the 2D Collider because the state of 2D Collider resulted in vertices too close or an area that is too small for the physics engine to handle.  
[RemovedShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderErrorState2D.RemovedShapes.html) | Indicates that some physics shapes were not created by the 2D Collider because the state of 2D Collider resulted in vertices too close or an area that is too small for the physics engine to handle.  
* * *
