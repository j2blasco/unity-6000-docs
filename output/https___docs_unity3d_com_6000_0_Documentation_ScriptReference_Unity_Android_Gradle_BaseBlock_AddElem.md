* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.AddElement.html

#  [BaseBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.html).AddElement
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
public void AddElement([Unity.Android.Gradle.BaseElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseElement.html) element); 
### Parameters
Parameter | Description  
---|---  
element | Element to add as a child.  
### Description
Adds a new element as a child.
Unity throws an exception if: 
  * The provided element already has a parent.
  * A parent of this element has a raw value set.
  * This element has a raw value set.


* * *
