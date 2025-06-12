* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.SetValueWithoutNotify.html

#  [Foldout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Foldout.html).SetValueWithoutNotify
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
public void SetValueWithoutNotify(bool newValue); 
### Parameters
Parameter | Description  
---|---  
newValue | The new value of the foldout  
### Description
Sets the value of the Foldout's Toggle sub-element, but does not notify the rest of the hierarchy of the change. 
This is useful when you want to change the Foldout's Toggle value without triggering events. For example, let's say you set up a Foldout to trigger an animation, but you only want to trigger the animation when a user clicks the Foldout's Toggle, not when you change the Toggle's value via code (for example, inside another validation). You could use this method change the value "silently". 
* * *
