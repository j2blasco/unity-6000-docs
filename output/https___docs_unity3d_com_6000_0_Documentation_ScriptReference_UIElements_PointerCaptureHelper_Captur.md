* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureHelper.CapturePointer.html

#  [PointerCaptureHelper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureHelper.html).CapturePointer
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
public static void CapturePointer([UIElements.IEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IEventHandler.html) handler, int pointerId); 
### Parameters
Parameter | Description  
---|---  
handler | The VisualElement that captures the pointer.  
pointerId | The pointer to capture.  
### Description
Captures the pointer. 
When a VisualElement captures a pointer, all pointer events are sent to the element, regardless of which element is under the pointer. 
* * *
