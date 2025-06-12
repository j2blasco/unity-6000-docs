* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionEventBase_1.GetPooled.html

#  [TransitionEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TransitionEventBase_1.html).GetPooled
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
public static T GetPooled([UIElements.StylePropertyName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.StylePropertyName.html) stylePropertyName, double elapsedTime); 
### Parameters
Parameter | Description  
---|---  
stylePropertyName | The name of the style property.  
elapsedTime | The elapsed time.  
### Returns
**T** An initialized transition event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained from this method should be released back to the pool using Dispose(). 
* * *
