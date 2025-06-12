* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform-drivenByObject.html

#  [RectTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectTransform.html).drivenByObject
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
drivenByObject; 
### Description
The object that is driving the values of this RectTransform. Value is null if not driven.
Sometimes the values of a RectTransform can be driven by a script. When this is the case, the values should not be editable in the Inspector, and they should not be serialized either.  
  
When a script is driving the values of a RectTransform, that script can set the drivenByObject value to itself, so that the RectTransform can prevent the values from being edited in the Inspector, and from being serialized.  
  
If the script was previously driving the values but no longer is, it should set the drivenByObject value back to null.  
  
A script that is driving the values of a RectTransform should always set all the values, not just a subset; otherwise the remaining values will be undefined and also can't be edited by the user.
* * *
