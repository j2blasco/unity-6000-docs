* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.CreateContent.html

#  [Overlay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Overlay.html).CreateContent
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
public [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreateContent([Overlays.Layout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Overlays.Layout.html) requestedLayout); 
### Parameters
Parameter | Description  
---|---  
requestedLayout | The layout that contents should be styled to match.  
### Returns
**VisualElement** A new Visual Element containing the contents of the Overlay. 
### Description
Creates a new VisualElement containing the contents of this Overlay.
If the requestedLayout cannot be used, then the system uses another layout. If the layout is not able to be created, the default Panel layout content is returned.
* * *
