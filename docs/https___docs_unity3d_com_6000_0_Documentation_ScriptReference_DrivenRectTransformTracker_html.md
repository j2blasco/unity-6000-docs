* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrivenRectTransformTracker.html

# DrivenRectTransformTracker
struct in UnityEngine
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
A component can be designed to drive a RectTransform. The DrivenRectTransformTracker struct is used to specify which RectTransforms it is driving.
Driving a RectTransform means that the values of the driven RectTransform are controlled by that component. These driven values cannot be edited in the Inspector (they are shown as disabled). They also won't be saved when saving a Scene, which prevents undesired Scene file changes.  
  
Whenever the component is changing values of driven RectTransforms, it should first call the Clear method and then use the Add method to add all RectTransforms it is driving. The Clear method should also be called in the OnDisable callback of the component.
### Public Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrivenRectTransformTracker.Add.html) | Add a RectTransform to be driven.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrivenRectTransformTracker.Clear.html) | Clear the list of RectTransforms being driven.  
### Static Methods
Method | Description  
---|---  
[StartRecordingUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrivenRectTransformTracker.StartRecordingUndo.html) | Resume recording undo of driven RectTransforms.  
[StopRecordingUndo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrivenRectTransformTracker.StopRecordingUndo.html) | Stop recording undo actions from driven RectTransforms.  
* * *
