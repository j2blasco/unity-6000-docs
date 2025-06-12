* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureHelper.ReleasePointer.html

#  [PointerCaptureHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureHelper.html).ReleasePointer
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
public static void ReleasePointer([UIElements.IEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IEventHandler.html) handler, int pointerId); 
### Parameters
Parameter | Description  
---|---  
handler | The element which potentially captured the pointer.  
pointerId | The captured pointer.  
### Description
Tests whether an element captured a pointer and, if so, tells the element to release the pointer. 
* * *
## Declaration
public static void ReleasePointer([UIElements.IPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html) panel, int pointerId); 
### Parameters
Parameter | Description  
---|---  
panel | The panel that holds the element that captured the pointer.  
pointerId | The captured pointer.  
### Description
Releases the pointer. 
* * *
