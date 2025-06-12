* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureEventBase_1.GetPooled.html

#  [PointerCaptureEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerCaptureEventBase_1.html).GetPooled
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
public static T GetPooled([UIElements.IEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IEventHandler.html) target, [UIElements.IEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IEventHandler.html) relatedTarget, int pointerId); 
### Parameters
Parameter | Description  
---|---  
target | For PointerCapture and MouseCapture events, the element that captures the pointer. For PointerCaptureOut and MouseCaptureOut events, the element that releases the pointer.  
relatedTarget | For PointerCaptureEvent and MouseCaptureEvent, returns the element that loses the pointer capture, if any. For PointerCaptureOutEvent and MouseCaptureOutEvent, returns the element that captures the pointer.  
pointerId | The pointer that is captured or released.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
