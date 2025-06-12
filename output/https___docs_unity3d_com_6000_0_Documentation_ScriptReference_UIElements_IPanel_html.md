* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html

# IPanel
interface in UnityEngine.UIElements
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
Interface for classes implementing UI panels. 
### Properties
Property | Description  
---|---  
[contextType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel-contextType.html) |  Describes in which context a VisualElement hierarchy is being ran.   
[contextualMenuManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel-contextualMenuManager.html) |  The Contextual menu manager for the panel.   
[dispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel-dispatcher.html) |  This Panel EventDispatcher.   
[focusController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel-focusController.html) |  Return the focus controller for this panel.   
[isDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel-isDirty.html) |  Checks whether any element within the panel has had any changes to its state since the panel was last rendered.   
[scaledPixelsPerPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel-scaledPixelsPerPoint.html) |  Gives the current scaled pixels per point value of the panel.   
[visualTree](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel-visualTree.html) |  Root of the VisualElement hierarchy.   
### Public Methods
Method | Description  
---|---  
[Pick](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.Pick.html) |  Returns the top element at this position. Will not return elements with pickingMode set to PickingMode.Ignore.   
[PickAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.PickAll.html) |  Returns all elements at this position. Will not return elements with pickingMode set to PickingMode.Ignore.   
* * *
