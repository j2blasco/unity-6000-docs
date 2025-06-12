* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyboardNavigationManipulator-ctor.html

# KeyboardNavigationManipulator Constructor
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
public KeyboardNavigationManipulator(Action<KeyboardNavigationOperation,EventBase> action); 
### Parameters
Parameter | Description  
---|---  
action | This action is invoked when specific low level events are dispatched to the target <see cref="VisualElement" />, with a specific value of <see cref="KeyboardNavigationOperation" /> and a reference to the original low level event.  
### Description
Initializes and returns an instance of KeyboardNavigationManipulator, configured to invoke the specified callback. 
* * *
