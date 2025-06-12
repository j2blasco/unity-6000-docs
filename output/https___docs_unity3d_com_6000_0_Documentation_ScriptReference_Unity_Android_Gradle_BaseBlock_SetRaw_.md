* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.SetRaw.html

#  [BaseBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.BaseBlock.html).SetRaw
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
public void SetRaw(string rawString); 
### Parameters
Parameter | Description  
---|---  
rawString | Raw string value.  
### Description
Sets a raw string value to this block.
Empty string is a valid value.  
  
Unity throws an exception if: 
  * This block has child elements.
  * The parent element has a raw value set.
  * Child elements of this block were already modified in the same script.


To override child elements, first use `Clear()` on this block to clear it.
* * *
